"use client";

import { useEffect, useState, useRef } from "react";
import { socket } from "@/lib/socket";
import { Clock, Activity } from "lucide-react";

interface TimelineEvent {
    id: number;
    timestamp: Date;
    image: string; // Base64
    category: string;
    description: string;
    risk: boolean;
    duration: number;
}

export default function SessionTimeline() {
    const [events, setEvents] = useState<TimelineEvent[]>([]);
    const scrollRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        socket.on("sensor_data", (payload: any) => {
            if (payload.type === "screen_observer" && payload.image_base64) {
                const newEvent: TimelineEvent = {
                    id: Date.now(),
                    timestamp: new Date(),
                    image: `data:image/jpeg;base64,${payload.image_base64}`,
                    category: payload.raw_category,
                    description: payload.text.split("Screen Analysis: ")[1]?.split(".")[0] || "Activity Detected",
                    risk: payload.text.includes("Risk: True") || false, // Simple heuristic from text if raw boolean missing
                    duration: payload.duration
                };

                setEvents(prev => {
                    const updated = [...prev, newEvent];
                    // Keep last 20 events
                    if (updated.length > 20) return updated.slice(updated.length - 20);
                    return updated;
                });
            }
        });

        return () => {
            socket.off("sensor_data");
        };
    }, []);

    // Auto-scroll to right
    useEffect(() => {
        if (scrollRef.current) {
            scrollRef.current.scrollLeft = scrollRef.current.scrollWidth;
        }
    }, [events]);

    return (
        <div className="fixed bottom-0 left-0 w-full z-40 p-4 pointer-events-none">
            <div className="max-w-7xl mx-auto pointer-events-auto">
                <div className="bg-black/80 backdrop-blur-xl border border-zinc-800 rounded-xl p-4 shadow-[0_-10px_40px_rgba(0,0,0,0.5)]">
                    <div className="flex items-center gap-2 mb-3 text-xs text-zinc-500 font-mono uppercase tracking-widest">
                        <div className="w-2 h-2 rounded-full bg-cyan-500 animate-pulse shadow-[0_0_10px_rgba(6,182,212,0.8)]" />
                        <span className="text-cyan-500 font-bold">Live Session Feed</span>
                        <div className="h-px flex-1 bg-gradient-to-r from-cyan-900/50 to-transparent" />
                        <span className="text-zinc-600">
                            {events.length > 0 ? `${events.length} Snapshots` : "Waiting for signal..."}
                        </span>
                    </div>

                    <div
                        ref={scrollRef}
                        className="flex gap-4 overflow-x-auto pb-2 scrollbar-hide snap-x min-h-[140px] items-center"
                        style={{ scrollBehavior: 'smooth' }}
                    >
                        {events.length === 0 && (
                            <div className="w-full flex flex-col items-center justify-center text-zinc-600 py-8 animate-pulse">
                                <Activity size={24} className="mb-2 opacity-50" />
                                <p className="text-xs font-mono">Scanning visual cortex...</p>
                            </div>
                        )}

                        {events.map((event) => (
                            <div
                                key={event.id}
                                className={`
                                    flex-shrink-0 w-56 group relative snap-start
                                    bg-zinc-900/90 rounded-lg overflow-hidden border transition-all duration-300 hover:scale-105 hover:z-10 hover:shadow-xl
                                    ${event.risk ? "border-red-500/50 shadow-[0_0_15px_rgba(239,68,68,0.2)]" : "border-zinc-800 hover:border-cyan-500/50"}
                                `}
                            >
                                {/* Image */}
                                <div className="relative h-32 w-full overflow-hidden bg-zinc-950">
                                    <img
                                        src={event.image}
                                        alt="Screen Capture"
                                        className="object-cover w-full h-full opacity-70 group-hover:opacity-100 transition-opacity duration-500"
                                    />
                                    <div className="absolute top-2 right-2 px-1.5 py-0.5 bg-black/70 rounded text-[10px] text-white font-mono border border-white/10 backdrop-blur-sm">
                                        {event.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                                    </div>
                                    {event.risk && (
                                        <div className="absolute top-2 left-2 px-1.5 py-0.5 bg-red-500/80 rounded text-[10px] text-white font-bold tracking-wider backdrop-blur-sm shadow-lg">
                                            RISK
                                        </div>
                                    )}
                                </div>

                                {/* Info */}
                                <div className="p-3 border-t border-white/5">
                                    <div className="flex justify-between items-center mb-1">
                                        <span className={`text-xs font-bold truncate max-w-[120px] ${event.risk ? "text-red-400" : "text-cyan-400"}`}>
                                            {event.category}
                                        </span>
                                        <span className="text-[10px] text-zinc-500 flex items-center gap-1 bg-zinc-950/50 px-1.5 py-0.5 rounded-full border border-white/5">
                                            <Activity size={10} />
                                            {event.duration}m
                                        </span>
                                    </div>
                                    <p className="text-[10px] text-zinc-400 line-clamp-2 leading-tight h-8">
                                        {event.description}
                                    </p>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    );
}
