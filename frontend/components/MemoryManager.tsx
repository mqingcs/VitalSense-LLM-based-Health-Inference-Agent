"use client";

import { useState, useEffect } from "react";
import { Trash2, Calendar, CheckSquare, X, AlertTriangle, RefreshCw } from "lucide-react";
import GlassPanel from "./ui/GlassPanel";

interface MemoryEntry {
    id: string;
    timestamp: string;
    scene: string;
    statement: string;
    user_state: string;
    outcome: string;
}

interface MemoryManagerProps {
    isOpen: boolean;
    onClose: () => void;
    onRefresh: () => void; // Callback to refresh graph
}

export default function MemoryManager({ isOpen, onClose, onRefresh }: MemoryManagerProps) {
    const [memories, setMemories] = useState<MemoryEntry[]>([]);
    const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set());
    const [loading, setLoading] = useState(false);

    // Range Filter
    const [startDate, setStartDate] = useState("");
    const [endDate, setEndDate] = useState("");

    useEffect(() => {
        if (isOpen) {
            fetchMemories();
        }
    }, [isOpen]);

    const fetchMemories = async () => {
        setLoading(true);
        try {
            const res = await fetch("http://localhost:8000/memories");
            const data = await res.json();
            // Sort by date desc
            data.sort((a: any, b: any) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime());
            setMemories(data);
        } catch (e) {
            console.error("Failed to fetch memories", e);
        } finally {
            setLoading(false);
        }
    };

    const toggleSelect = (id: string) => {
        const newSet = new Set(selectedIds);
        if (newSet.has(id)) newSet.delete(id);
        else newSet.add(id);
        setSelectedIds(newSet);
    };

    const toggleSelectAll = () => {
        if (selectedIds.size === memories.length) {
            setSelectedIds(new Set());
        } else {
            setSelectedIds(new Set(memories.map(m => m.id)));
        }
    };

    const handleDeleteSelected = async () => {
        if (selectedIds.size === 0) return;
        if (!confirm(`Delete ${selectedIds.size} memories?`)) return;

        setLoading(true);
        try {
            // Delete one by one for now (or could implement bulk endpoint)
            // Or use range if all selected? No, just loop.
            for (const id of Array.from(selectedIds)) {
                await fetch(`http://localhost:8000/memories/${id}`, { method: "DELETE" });
            }
            await fetchMemories();
            setSelectedIds(new Set());
            onRefresh();
        } catch (e) {
            console.error("Delete failed", e);
        } finally {
            setLoading(false);
        }
    };

    const handleClearAll = async () => {
        if (!confirm("CRITICAL WARNING: This will wipe ALL long-term memory. The agent will forget everything about you. Proceed?")) return;

        setLoading(true);
        try {
            await fetch("http://localhost:8000/memories/all", { method: "DELETE" });
            await fetchMemories();
            onRefresh();
        } catch (e) {
            console.error("Clear all failed", e);
        } finally {
            setLoading(false);
        }
    };

    const handleDeleteRange = async () => {
        if (!startDate || !endDate) return alert("Please select start and end dates.");
        if (!confirm(`Delete memories between ${startDate} and ${endDate}?`)) return;

        setLoading(true);
        try {
            // Append time to make it inclusive full day
            const startIso = new Date(startDate).toISOString();
            const endIso = new Date(endDate + "T23:59:59").toISOString();

            await fetch(`http://localhost:8000/memories/range?start=${startIso}&end=${endIso}`, { method: "DELETE" });
            await fetchMemories();
            onRefresh();
        } catch (e) {
            console.error("Range delete failed", e);
        } finally {
            setLoading(false);
        }
    };

    if (!isOpen) return null;

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4">
            <GlassPanel className="w-full max-w-4xl flex flex-col max-h-[80vh]" intensity="high">
                {/* Header */}
                <div className="p-6 border-b border-white/10 flex justify-between items-center bg-black/20">
                    <div>
                        <h2 className="text-xl font-bold text-white flex items-center gap-2">
                            <RefreshCw size={20} className="text-cyan-500" />
                            Memory Manager
                        </h2>
                        <p className="text-sm text-zinc-400">Review and prune the Hippocampus.</p>
                    </div>
                    <button onClick={onClose} className="p-2 hover:bg-white/10 rounded-full transition-colors">
                        <X size={20} className="text-zinc-400" />
                    </button>
                </div>

                {/* Toolbar */}
                <div className="p-4 border-b border-zinc-800 bg-zinc-900/30 flex flex-wrap gap-4 items-center justify-between">
                    <div className="flex items-center gap-2">
                        <button
                            onClick={toggleSelectAll}
                            className="flex items-center gap-2 px-3 py-1.5 bg-zinc-800 hover:bg-zinc-700 rounded text-xs font-mono transition-colors"
                        >
                            <CheckSquare size={14} />
                            {selectedIds.size === memories.length ? "Deselect All" : "Select All"}
                        </button>
                        <span className="text-xs text-zinc-500">{selectedIds.size} selected</span>
                    </div>

                    <div className="flex items-center gap-2">
                        <div className="flex items-center gap-1 bg-zinc-800 rounded px-2 py-1">
                            <Calendar size={14} className="text-zinc-500" />
                            <input
                                type="date"
                                className="bg-transparent text-xs text-white outline-none w-24"
                                value={startDate}
                                onChange={e => setStartDate(e.target.value)}
                            />
                            <span className="text-zinc-600">-</span>
                            <input
                                type="date"
                                className="bg-transparent text-xs text-white outline-none w-24"
                                value={endDate}
                                onChange={e => setEndDate(e.target.value)}
                            />
                        </div>
                        <button
                            onClick={handleDeleteRange}
                            className="px-3 py-1.5 bg-zinc-800 hover:bg-red-900/30 text-zinc-300 hover:text-red-400 rounded text-xs font-mono transition-colors border border-transparent hover:border-red-500/30"
                        >
                            Clear Range
                        </button>
                    </div>

                    <div className="flex items-center gap-2">
                        <button
                            onClick={handleDeleteSelected}
                            disabled={selectedIds.size === 0}
                            className="flex items-center gap-2 px-3 py-1.5 bg-red-500/10 hover:bg-red-500/20 text-red-500 border border-red-500/20 rounded text-xs font-bold transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
                        >
                            <Trash2 size={14} />
                            Delete Selected
                        </button>
                        <button
                            onClick={handleClearAll}
                            className="flex items-center gap-2 px-3 py-1.5 bg-red-600 hover:bg-red-500 text-white rounded text-xs font-bold transition-colors shadow-lg shadow-red-900/20"
                        >
                            <AlertTriangle size={14} />
                            Wipe All
                        </button>
                    </div>
                </div>

                {/* List */}
                <div className="flex-1 overflow-y-auto p-4 space-y-2 bg-zinc-950/50">
                    {loading ? (
                        <div className="text-center py-10 text-zinc-500 animate-pulse">Accessing Neural Archives...</div>
                    ) : memories.length === 0 ? (
                        <div className="text-center py-10 text-zinc-600">No memories found. The mind is clear.</div>
                    ) : (
                        memories.map(mem => (
                            <div
                                key={mem.id}
                                onClick={() => toggleSelect(mem.id)}
                                className={`
                                    flex items-start gap-4 p-3 rounded-lg border cursor-pointer transition-all
                                    ${selectedIds.has(mem.id)
                                        ? "bg-cyan-950/20 border-cyan-500/30"
                                        : "bg-zinc-900 border-zinc-800 hover:border-zinc-700"}
                                `}
                            >
                                <div className={`mt-1 w-4 h-4 rounded border flex items-center justify-center ${selectedIds.has(mem.id) ? "bg-cyan-500 border-cyan-500" : "border-zinc-600"}`}>
                                    {selectedIds.has(mem.id) && <CheckSquare size={10} className="text-black" />}
                                </div>
                                <div className="flex-1 min-w-0">
                                    <div className="flex justify-between items-start mb-1">
                                        <span className="text-sm font-bold text-zinc-200">{mem.scene}</span>
                                        <span className="text-xs text-zinc-500 font-mono">{new Date(mem.timestamp).toLocaleString()}</span>
                                    </div>
                                    <p className="text-xs text-zinc-400 line-clamp-2">{mem.statement}</p>
                                    <div className="mt-2 flex gap-2">
                                        <span className="px-1.5 py-0.5 bg-zinc-800 rounded text-[10px] text-zinc-500">{mem.user_state}</span>
                                        <span className="px-1.5 py-0.5 bg-zinc-800 rounded text-[10px] text-zinc-500 truncate max-w-[200px]">{mem.outcome}</span>
                                    </div>
                                </div>
                            </div>
                        ))
                    )}
                </div>
            </GlassPanel>
        </div>
    );
}
