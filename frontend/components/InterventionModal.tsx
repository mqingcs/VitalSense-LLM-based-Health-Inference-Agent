"use client";

import { useEffect, useState } from "react";
import { socket } from "@/lib/socket";
import { AlertTriangle, XCircle } from "lucide-react";

export default function InterventionModal() {
    const [isOpen, setIsOpen] = useState(false);
    const [data, setData] = useState<any>(null);

    useEffect(() => {
        socket.on("intervention", (payload: any) => {
            setData(payload);
            setIsOpen(true);
            // Play alert sound
            const audio = new Audio("/alert.mp3"); // Placeholder, browser might block auto-play
            audio.play().catch(e => console.log("Audio play failed", e));
        });

        return () => {
            socket.off("intervention");
        };
    }, []);

    if (!isOpen || !data) return null;

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-red-950/90 backdrop-blur-sm animate-in fade-in duration-300">
            <div className="bg-black border-2 border-red-500 rounded-lg p-8 max-w-2xl w-full shadow-[0_0_50px_rgba(239,68,68,0.5)] text-center relative">

                <div className="absolute top-0 left-0 w-full h-1 bg-red-500 animate-pulse" />

                <div className="flex justify-center mb-6">
                    <AlertTriangle size={64} className="text-red-500 animate-bounce" />
                </div>

                <h1 className="text-4xl font-bold text-red-500 mb-2 tracking-widest uppercase">
                    CRITICAL ALERT
                </h1>

                <h2 className="text-xl text-red-200 mb-8 font-mono">
                    HIGH RISK DETECTED
                </h2>

                <div className="bg-red-900/20 border border-red-800 p-6 rounded-md mb-8 text-left">
                    <p className="text-lg text-white mb-4 font-bold">
                        {data.summary}
                    </p>
                    <ul className="space-y-2">
                        {data.actions.map((action: string, i: number) => (
                            <li key={i} className="flex items-start gap-2 text-red-100">
                                <span className="text-red-500 mt-1">➤</span>
                                {action}
                            </li>
                        ))}
                    </ul>
                </div>

                <button
                    onClick={() => setIsOpen(false)}
                    className="bg-red-600 hover:bg-red-700 text-white font-bold py-3 px-8 rounded-full transition-all hover:scale-105 flex items-center gap-2 mx-auto"
                >
                    <XCircle size={20} />
                    I COMPLY / DISMISS
                </button>
            </div>
        </div>
    );
}
