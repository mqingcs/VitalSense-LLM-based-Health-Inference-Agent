"use client";

import { useEffect, useState } from "react";
import { socket } from "@/lib/socket";
import { Terminal, Activity, Shield, Stethoscope } from "lucide-react";
import { cn } from "@/lib/utils"; // Assumes you have a utils file, or I can inline it.

// Inline utility for now if lib/utils doesn't exist
function classNames(...classes: (string | undefined | null | false)[]) {
    return classes.filter(Boolean).join(" ");
}

type LogEntry = {
    id: string;
    agent: "Triage" | "Dr. Nexus" | "Guardian" | "Chair" | "System";
    message: string;
    timestamp: string;
};

export default function CouncilRoom() {
    const [logs, setLogs] = useState<LogEntry[]>([]);
    const [activeAgents, setActiveAgents] = useState<string[]>([]);

    useEffect(() => {
        socket.on("connect", () => {
            addLog("System", "Connected to VitalKernel.");
        });

        socket.on("sensor_data", (data: any) => {
            addLog("System", `New Signal: ${data.text}`);
            setActiveAgents(["Triage", "Dr. Nexus", "Guardian"]);
        });

        socket.on("analysis_result", (data: any) => {
            addLog("Chair", `Risk: ${data.risk_level}. Actions: ${data.actions.length} recommended.`);
            setActiveAgents([]);
        });

        return () => {
            socket.off("connect");
            socket.off("sensor_data");
            socket.off("analysis_result");
        };
    }, []);

    const addLog = (agent: LogEntry["agent"], message: string) => {
        setLogs((prev) => [
            {
                id: Math.random().toString(36).substring(7),
                agent,
                message,
                timestamp: new Date().toLocaleTimeString(),
            },
            ...prev.slice(0, 50), // Keep last 50
        ]);
    };

    return (
        <div className="flex flex-col h-full bg-black border border-zinc-800 font-mono text-sm p-4 rounded-lg shadow-2xl shadow-emerald-900/20">
            <div className="flex items-center justify-between mb-4 border-b border-zinc-800 pb-2">
                <h2 className="text-emerald-500 font-bold flex items-center gap-2">
                    <Terminal size={16} />
                    THE COUNCIL
                </h2>
                <div className="flex gap-2">
                    {["Dr. Nexus", "Guardian"].map((agent) => (
                        <div
                            key={agent}
                            className={classNames(
                                "px-2 py-0.5 text-xs rounded-full transition-colors",
                                activeAgents.includes(agent)
                                    ? "bg-emerald-500/20 text-emerald-400 animate-pulse"
                                    : "bg-zinc-900 text-zinc-600"
                            )}
                        >
                            {agent}
                        </div>
                    ))}
                </div>
            </div>

            <div className="flex-1 overflow-y-auto space-y-3 scrollbar-hide">
                {logs.map((log) => (
                    <div key={log.id} className="flex gap-3 animate-in fade-in slide-in-from-bottom-2">
                        <span className="text-zinc-600 shrink-0">[{log.timestamp}]</span>
                        <div className="flex flex-col">
                            <span
                                className={classNames(
                                    "font-bold",
                                    log.agent === "Dr. Nexus" && "text-blue-400",
                                    log.agent === "Guardian" && "text-orange-400",
                                    log.agent === "Chair" && "text-purple-400",
                                    log.agent === "System" && "text-zinc-500"
                                )}
                            >
                                {log.agent}
                            </span>
                            <span className="text-zinc-300">{log.message}</span>
                        </div>
                    </div>
                ))}
                {logs.length === 0 && (
                    <div className="text-zinc-700 text-center mt-10">
                        Waiting for signals...
                    </div>
                )}
            </div>
        </div>
    );
}
