"use client";

import { useState, useEffect, useRef } from "react";
import { socket } from "@/lib/socket";
import { Send, User, Bot, X, Minimize2, Maximize2, AlertTriangle, CheckCircle, ThumbsUp, ThumbsDown } from "lucide-react";
import { cn } from "@/lib/utils";
import GlassPanel from "./ui/GlassPanel";

type RiskCardData = {
    title: string;
    summary: string;
    risk_level: string;
    actions: string[];
    risk_type: string; // e.g. "sedentary"
};

type Message = {
    id: string;
    role: "user" | "assistant" | "system";
    content: string;
    timestamp: number;
    cardData?: RiskCardData;
};

// Risk Card Component
const RiskCard = ({ data, onDismiss, onAcknowledge }: { data: RiskCardData, onDismiss: () => void, onAcknowledge: () => void }) => (
    <div className="relative overflow-hidden bg-gradient-to-br from-amber-950/80 to-black/80 border border-amber-500/30 rounded-xl p-5 space-y-4 w-full shadow-xl backdrop-blur-md group transition-all hover:border-amber-500/50">
        {/* Ambient Glow */}
        <div className="absolute -top-10 -right-10 w-32 h-32 bg-amber-500/10 rounded-full blur-3xl pointer-events-none group-hover:bg-amber-500/20 transition-all" />

        <div className="flex items-start gap-4 relative z-10">
            <div className="p-2 bg-amber-500/10 rounded-lg border border-amber-500/20 shrink-0 animate-pulse">
                <AlertTriangle className="text-amber-500" size={24} />
            </div>
            <div>
                <h4 className="font-bold text-amber-100 text-lg tracking-tight">{data.title}</h4>
                <div className="flex items-center gap-2 mt-1">
                    <span className="px-2 py-0.5 bg-amber-500/20 border border-amber-500/30 rounded text-[10px] font-bold text-amber-300 uppercase tracking-wider">
                        {data.risk_level} Risk
                    </span>
                    <span className="text-xs text-zinc-500">Just now</span>
                </div>
            </div>
        </div>

        <p className="text-sm text-zinc-300 leading-relaxed relative z-10">
            {data.summary}
        </p>

        <div className="space-y-2 bg-black/20 rounded-lg p-3 border border-white/5 relative z-10">
            <p className="text-xs font-semibold text-zinc-400 uppercase tracking-wider mb-2">Suggested Actions</p>
            {data.actions.map((action, i) => (
                <div key={i} className="flex items-start gap-2 text-xs text-zinc-300">
                    <div className="w-1.5 h-1.5 bg-amber-500 rounded-full mt-1 shrink-0" />
                    {action}
                </div>
            ))}
        </div>

        <div className="flex gap-3 pt-2 relative z-10">
            <button
                onClick={onAcknowledge}
                className="flex-1 bg-emerald-600/20 hover:bg-emerald-600/30 border border-emerald-500/30 hover:border-emerald-500/50 text-emerald-400 text-xs font-medium py-2.5 rounded-lg transition-all flex items-center justify-center gap-2 group/btn"
            >
                <CheckCircle size={14} className="group-hover/btn:scale-110 transition-transform" />
                I'll fix it
            </button>
            <button
                onClick={onDismiss}
                className="flex-1 bg-zinc-800/40 hover:bg-zinc-800/60 border border-white/10 hover:border-white/20 text-zinc-400 hover:text-zinc-300 text-xs font-medium py-2.5 rounded-lg transition-all flex items-center justify-center gap-2 group/btn"
            >
                <ThumbsDown size={14} className="group-hover/btn:scale-110 transition-transform" />
                Not now
            </button>
        </div>
    </div>
);

export default function ChatInterface() {
    const [isOpen, setIsOpen] = useState(true);
    const [messages, setMessages] = useState<Message[]>([]);
    const [input, setInput] = useState("");
    const [isTyping, setIsTyping] = useState(false);
    const scrollRef = useRef<HTMLDivElement>(null);

    const [position, setPosition] = useState({ x: 0, y: 0 });
    const [isDragging, setIsDragging] = useState(false);
    const dragStartRef = useRef({ x: 0, y: 0 });

    const addMessage = (role: Message["role"], content: string, cardData?: RiskCardData) => {
        setMessages((prev) => [
            ...prev,
            {
                id: Math.random().toString(36).substring(7),
                role,
                content,
                timestamp: Date.now(),
                cardData
            },
        ]);
    };

    useEffect(() => {
        // Initial Greeting
        setMessages([
            {
                id: "init",
                role: "assistant",
                content: "Hello! I'm your Liaison. I'm here to help you manage your health and productivity. How are you feeling right now?",
                timestamp: Date.now(),
            },
        ]);

        socket.on("chat_reply", (data: any) => {
            setIsTyping(false);
            addMessage("assistant", data.message);
        });

        // Listen for System Alerts to inject into chat
        socket.on("analysis_result", (data: any) => {
            if (data.risk_level === "HIGH" || data.risk_level === "MEDIUM") {
                // Use RiskCard instead of text
                addMessage("system", "", {
                    title: "Health Alert",
                    summary: data.summary,
                    risk_level: data.risk_level,
                    actions: data.actions,
                    risk_type: "sedentary" // Defaulting to sedentary for now as it's the main risk
                });
            }
        });

        // Listen for Risk Cards (Legacy/Direct support)
        socket.on("risk_card", (data: any) => {
            addMessage("system", "", {
                title: data.title || "Health Alert",
                summary: data.summary,
                risk_level: data.risk_level,
                actions: data.actions,
                risk_type: data.risk_type || "sedentary"
            });
        });

        return () => {
            socket.off("chat_reply");
            socket.off("analysis_result");
            socket.off("risk_card");
        };
    }, []);

    // Drag Handlers
    const handleMouseDown = (e: React.MouseEvent) => {
        setIsDragging(true);
        dragStartRef.current = { x: e.clientX - position.x, y: e.clientY - position.y };
    };

    useEffect(() => {
        const handleMouseMove = (e: MouseEvent) => {
            if (isDragging) {
                setPosition({
                    x: e.clientX - dragStartRef.current.x,
                    y: e.clientY - dragStartRef.current.y
                });
            }
        };

        const handleMouseUp = () => {
            setIsDragging(false);
        };

        if (isDragging) {
            window.addEventListener("mousemove", handleMouseMove);
            window.addEventListener("mouseup", handleMouseUp);
        }

        return () => {
            window.removeEventListener("mousemove", handleMouseMove);
            window.removeEventListener("mouseup", handleMouseUp);
        };
    }, [isDragging]);

    useEffect(() => {
        if (scrollRef.current) {
            scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
        }
    }, [messages, isTyping]);

    const handleSend = () => {
        if (!input.trim()) return;

        const msg = input;
        setInput("");
        addMessage("user", msg);
        setIsTyping(true);

        socket.emit("chat_message", { message: msg });
    };

    const handleKeyDown = (e: React.KeyboardEvent) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSend();
        }
    };

    const handleCardAction = (action: "dismiss" | "acknowledge", riskType: string) => {
        if (action === "dismiss") {
            // Feedback Loop: Increase tolerance
            socket.emit("adjust_tolerance", { risk_type: riskType, amount: 0.1 });
            addMessage("user", "Not now. I need to focus.");
        } else {
            addMessage("user", "On it. Thanks.");
        }
    };

    if (!isOpen) {
        return (
            <button
                onClick={() => setIsOpen(true)}
                className="fixed bottom-6 right-6 bg-emerald-500 hover:bg-emerald-600 text-white p-4 rounded-full shadow-lg transition-all z-50"
            >
                <Bot size={24} />
            </button>
        );
    }

    return (
        <div
            className="fixed bottom-6 right-6 z-50"
            style={{ transform: `translate(${position.x}px, ${position.y}px)` }}
        >
            <GlassPanel className="w-96 h-[600px] shadow-2xl border border-emerald-500/30" intensity="high">
                <div className="flex flex-col h-full">
                    {/* Header - Draggable Area */}
                    <div
                        className="flex items-center justify-between p-4 border-b border-white/10 bg-emerald-900/20 cursor-move select-none shrink-0"
                        onMouseDown={handleMouseDown}
                    >
                        <div className="flex items-center gap-2 pointer-events-none">
                            <Bot className="text-emerald-400" size={20} />
                            <span className="font-bold text-emerald-100">Liaison AI</span>
                        </div>
                        <div className="flex gap-2">
                            <button onClick={() => setIsOpen(false)} className="text-zinc-400 hover:text-white">
                                <Minimize2 size={16} />
                            </button>
                        </div>
                    </div>

                    {/* Messages */}
                    <div className="flex-1 overflow-y-auto p-4 space-y-4 scrollbar-hide min-h-0" ref={scrollRef}>
                        {messages.map((msg) => (
                            <div
                                key={msg.id}
                                className={cn(
                                    "flex gap-3 max-w-[90%]",
                                    msg.role === "user" ? "ml-auto flex-row-reverse" : ""
                                )}
                            >
                                <div
                                    className={cn(
                                        "w-8 h-8 rounded-full flex items-center justify-center shrink-0",
                                        msg.role === "user" ? "bg-zinc-700" : msg.role === "system" ? "bg-amber-500/20 text-amber-500" : "bg-emerald-500/20 text-emerald-400"
                                    )}
                                >
                                    {msg.role === "user" ? <User size={14} /> : msg.role === "system" ? <Bot size={14} /> : <Bot size={14} />}
                                </div>
                                <div
                                    className={cn(
                                        "p-3 rounded-2xl text-sm whitespace-pre-wrap",
                                        msg.role === "user"
                                            ? "bg-emerald-600 text-white rounded-tr-none"
                                            : msg.role === "system"
                                                ? "bg-amber-900/30 border border-amber-500/30 text-amber-100 rounded-tl-none"
                                                : "bg-zinc-800/80 text-zinc-200 rounded-tl-none"
                                    )}
                                >
                                    {msg.role === "system" && msg.cardData ? (
                                        <RiskCard
                                            data={msg.cardData}
                                            onDismiss={() => handleCardAction("dismiss", msg.cardData!.risk_type)}
                                            onAcknowledge={() => handleCardAction("acknowledge", msg.cardData!.risk_type)}
                                        />
                                    ) : (
                                        msg.content
                                    )}
                                </div>
                            </div>
                        ))}
                        {isTyping && (
                            <div className="flex gap-3">
                                <div className="w-8 h-8 rounded-full bg-emerald-500/20 flex items-center justify-center shrink-0">
                                    <Bot size={14} className="text-emerald-400" />
                                </div>
                                <div className="bg-zinc-800/80 p-3 rounded-2xl rounded-tl-none flex gap-1 items-center">
                                    <span className="w-2 h-2 bg-zinc-500 rounded-full animate-bounce" style={{ animationDelay: "0ms" }} />
                                    <span className="w-2 h-2 bg-zinc-500 rounded-full animate-bounce" style={{ animationDelay: "150ms" }} />
                                    <span className="w-2 h-2 bg-zinc-500 rounded-full animate-bounce" style={{ animationDelay: "300ms" }} />
                                </div>
                            </div>
                        )}
                    </div>

                    {/* Input */}
                    <div className="p-4 border-t border-white/10 bg-black/20 shrink-0">
                        <div className="relative flex items-end gap-2">
                            <textarea
                                value={input}
                                onChange={(e) => setInput(e.target.value)}
                                onKeyDown={handleKeyDown}
                                placeholder="Type a message..."
                                className="w-full bg-zinc-900/50 border border-zinc-700 rounded-xl py-3 pl-4 pr-12 text-sm text-white focus:outline-none focus:border-emerald-500/50 resize-none h-12 max-h-32 scrollbar-hide"
                            />
                            <button
                                onClick={handleSend}
                                disabled={!input.trim()}
                                className="absolute right-2 top-2 p-2 text-emerald-500 hover:text-emerald-400 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                            >
                                <Send size={18} />
                            </button>
                        </div>
                    </div>
                </div>
            </GlassPanel>
        </div>
    );
}