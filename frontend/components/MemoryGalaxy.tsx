"use client";

import { useEffect, useRef, useState, useCallback } from "react";
import dynamic from "next/dynamic";
import { Maximize2, Minimize2, Database, XCircle } from "lucide-react";
import { cn } from "@/lib/utils";
import MemoryManager from "./MemoryManager";
import { socket } from "@/lib/socket";

const ForceGraph3D = dynamic(() => import("react-force-graph-3d"), { ssr: false });

export default function MemoryGalaxy() {
    const [data, setData] = useState<{ nodes: any[]; links: any[] }>({ nodes: [], links: [] });
    const [selectedNode, setSelectedNode] = useState<any>(null);
    const [isFullScreen, setIsFullScreen] = useState(false);
    const [isManagerOpen, setIsManagerOpen] = useState(false); // [NEW]
    const graphRef = useRef<any>(null);
    const containerRef = useRef<HTMLDivElement>(null);
    const [dimensions, setDimensions] = useState({ width: 800, height: 500 });

    const fetchData = useCallback(async () => {
        try {
            const res = await fetch("http://localhost:8000/memories");
            const memories = await res.json();

            // Transform to Graph Data
            const nodes: any[] = [];
            const links: any[] = [];

            memories.forEach((mem: any) => {
                // Node
                const isHighlighted = highlightedNodes.has(mem.id || mem.timestamp);
                nodes.push({
                    id: mem.id || mem.timestamp, // Fallback if ID missing
                    name: mem.scene,
                    val: isHighlighted ? 3 : 1, // Make highlighted nodes bigger
                    color: isHighlighted
                        ? "#f59e0b" // Amber for risk
                        : mem.user_state === "Anxious" ? "#ef4444" : mem.user_state === "Flow" ? "#6366f1" : "#22c55e",
                    ...mem
                });

                // Links (Simple Entity Co-occurrence)
                memories.forEach((other: any) => {
                    if (mem.id !== other.id) {
                        const shared = mem.entities.filter((e: string) => other.entities.includes(e));
                        if (shared.length > 0) {
                            links.push({
                                source: mem.id || mem.timestamp,
                                target: other.id || other.timestamp,
                                color: "#ffffff20"
                            });
                        }
                    }
                });
            });

            // Deduplicate links
            // ... (simplified for now)

            setData({ nodes, links });
        } catch (e) {
            console.error("Failed to fetch memory graph", e);
        }
    }, []);



    // ...

    const [highlightedNodes, setHighlightedNodes] = useState<Set<string>>(new Set());

    // ...

    useEffect(() => {
        fetchData();

        // Listen for Risk Analysis to highlight nodes
        const handleAnalysis = (data: any) => {
            if (data.graph_highlights && Array.isArray(data.graph_highlights)) {
                console.log("Graph Highlights:", data.graph_highlights);
                setHighlightedNodes(new Set(data.graph_highlights));

                // Optional: Auto-zoom to the first highlighted node if exists
                if (data.graph_highlights.length > 0 && graphRef.current) {
                    // We need to find the node object in the current data
                    // This might be tricky if data isn't fresh, but let's try
                    // We'll do it in a separate effect or just let the user explore
                }
            }
        };

        socket.on("analysis_result", handleAnalysis);

        return () => {
            socket.off("analysis_result", handleAnalysis);
        };
    }, [fetchData]);

    // Handle Resize
    useEffect(() => {
        const updateDimensions = () => {
            if (containerRef.current) {
                setDimensions({
                    width: containerRef.current.clientWidth,
                    height: containerRef.current.clientHeight,
                });
            }
        };

        // Initial size
        updateDimensions();

        // Observer
        const observer = new ResizeObserver(updateDimensions);
        if (containerRef.current) {
            observer.observe(containerRef.current);
        }

        return () => observer.disconnect();
    }, [isFullScreen]); // Re-run when full screen toggles

    const toggleFullScreen = () => {
        setIsFullScreen(!isFullScreen);
    };

    const handleNodeClick = (node: any) => {
        setSelectedNode(node);
        // Aim at node
        const distance = 40;
        const distRatio = 1 + distance / Math.hypot(node.x, node.y, node.z);
        graphRef.current.cameraPosition(
            { x: node.x * distRatio, y: node.y * distRatio, z: node.z * distRatio },
            node,
            3000
        );
    };

    return (
        <div
            ref={containerRef}
            className={cn(
                "relative bg-black/40 backdrop-blur-md border border-zinc-800 rounded-xl overflow-hidden transition-all duration-500",
                isFullScreen ? "fixed inset-0 z-50 rounded-none border-none" : "h-[500px] w-full"
            )}
        >
            {/* Header Controls */}
            <div className="absolute top-4 left-4 z-10 flex items-center gap-4">
                <div className="flex items-center gap-2">
                    <div className="w-2 h-2 rounded-full bg-purple-500 animate-pulse shadow-[0_0_10px_rgba(168,85,247,0.8)]" />
                    <h2 className="text-sm font-bold text-zinc-300 tracking-widest uppercase font-mono">Neural Constellation</h2>
                </div>
            </div>

            <div className="absolute top-4 right-4 z-10 flex gap-2">
                <button
                    onClick={() => setIsManagerOpen(true)}
                    className="p-2 bg-black/50 hover:bg-zinc-800 text-zinc-400 hover:text-white rounded-lg transition-colors border border-white/10 backdrop-blur-sm"
                    title="Manage Memories"
                >
                    <Database size={18} />
                </button>
                <button
                    onClick={toggleFullScreen}
                    className="p-2 bg-black/50 hover:bg-zinc-800 text-zinc-400 hover:text-white rounded-lg transition-colors border border-white/10 backdrop-blur-sm"
                >
                    {isFullScreen ? <Minimize2 size={18} /> : <Maximize2 size={18} />}
                </button>
            </div>

            {/* Graph */}
            {/* Graph */}
            <ForceGraph3D
                ref={graphRef}
                width={dimensions.width}
                height={dimensions.height}
                graphData={data}
                nodeLabel="name"
                nodeColor="color"
                nodeRelSize={6}
                linkColor="color"
                linkOpacity={0.3}
                backgroundColor="#00000000" // Transparent
                onNodeClick={handleNodeClick}
                enableNodeDrag={true}
                onNodeDragEnd={node => {
                    // Lock node on drag end to keep structure, or unfix to let it float
                    node.fx = node.x;
                    node.fy = node.y;
                    node.fz = node.z;
                }}
                d3VelocityDecay={0.1} // Lower friction for more movement
                d3AlphaDecay={0.01} // Slower cooling
                cooldownTicks={100}
                onEngineStop={() => graphRef.current.zoomToFit(400, 100)}
            />

            {/* Detail Popup */}
            {selectedNode && (
                <div className="absolute bottom-8 right-8 w-96 bg-black/90 border border-cyan-500/50 p-6 rounded-xl shadow-[0_0_30px_rgba(6,182,212,0.2)] backdrop-blur-xl animate-in slide-in-from-bottom-10 z-20">
                    <div className="flex justify-between items-start mb-4 border-b border-zinc-800 pb-2">
                        <h3 className="font-bold text-cyan-50 text-lg">{selectedNode.name}</h3>
                        <button onClick={() => setSelectedNode(null)} className="text-zinc-500 hover:text-red-400 transition-colors">
                            <XCircle size={20} />
                        </button>
                    </div>
                    <div className="text-sm text-zinc-300 space-y-3 font-mono">
                        <div className="flex justify-between">
                            <span className="text-cyan-600">Time</span>
                            <span className="text-zinc-400">{new Date(selectedNode.timestamp).toLocaleString()}</span>
                        </div>
                        <div>
                            <span className="text-cyan-600 block mb-1">Scene</span>
                            <p className="text-zinc-100 bg-zinc-900/50 p-2 rounded border border-zinc-800">
                                {selectedNode.scene}
                            </p>
                        </div>
                        <div>
                            <span className="text-cyan-600 block mb-1">State</span>
                            <span className="text-yellow-500">{selectedNode.user_state}</span>
                        </div>
                        <div>
                            <span className="text-cyan-600 block mb-1">Entities</span>
                            <div className="flex flex-wrap gap-2">
                                {selectedNode.entities && selectedNode.entities.map((e: string, i: number) => (
                                    <span key={i} className="px-2 py-1 text-xs bg-cyan-950/50 text-cyan-300 rounded-full border border-cyan-800/50 shadow-[0_0_10px_rgba(8,145,178,0.2)]">
                                        {e}
                                    </span>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Memory Manager Modal */}
            <MemoryManager
                isOpen={isManagerOpen}
                onClose={() => setIsManagerOpen(false)}
                onRefresh={fetchData}
            />
        </div>
    );
}
