"use client";

import { useEffect, useState, useRef } from "react";
import dynamic from "next/dynamic";
import { XCircle } from "lucide-react";

// Dynamically import ForceGraph3D (it uses window, so no SSR)
const ForceGraph3D = dynamic(() => import("react-force-graph-3d"), {
    ssr: false,
});

export default function MemoryGalaxy() {
    const [graphData, setGraphData] = useState({ nodes: [], links: [] });
    const [selectedNode, setSelectedNode] = useState<any>(null);
    const fgRef = useRef<any>(null);

    useEffect(() => {
        // Fetch data from Backend
        fetch("http://localhost:8000/memories")
            .then((res) => res.json())
            .then((data) => setGraphData(data))
            .catch((err) => console.error("Failed to fetch memories:", err));
    }, []);

    return (
        <div className="relative w-full h-[500px] border border-zinc-800 rounded-xl overflow-hidden bg-black/50 backdrop-blur-sm">
            <div className="absolute top-4 left-4 z-10">
                <h2 className="text-xl font-bold text-cyan-400 tracking-widest uppercase">
                    Neural Constellation
                </h2>
                <p className="text-xs text-zinc-500">Hippocampus Visualizer v1.0</p>
            </div>

            <ForceGraph3D
                ref={fgRef}
                graphData={graphData}
                nodeLabel="label"
                nodeColor={(node: any) =>
                    node.group === 1 ? "#ef4444" : // High Risk (Red)
                        node.group === 2 ? "#facc15" : // Medium Risk (Yellow)
                            "#10b981" // Low Risk (Green)
                }
                nodeRelSize={6}
                linkColor={() => "#3f3f46"} // Zinc-700
                linkWidth={1}
                backgroundColor="#00000000" // Transparent
                onNodeClick={(node: any) => {
                    setSelectedNode(node);
                    // Aim at node
                    const distance = 40;
                    const distRatio = 1 + distance / Math.hypot(node.x, node.y, node.z);
                    fgRef.current.cameraPosition(
                        { x: node.x * distRatio, y: node.y * distRatio, z: node.z * distRatio },
                        node,
                        3000
                    );
                }}
            />

            {/* Detail Popup */}
            {selectedNode && (
                <div className="absolute bottom-4 right-4 w-80 bg-zinc-900/90 border border-cyan-500/50 p-4 rounded-lg shadow-2xl backdrop-blur-md animate-in slide-in-from-bottom-10">
                    <div className="flex justify-between items-start mb-2">
                        <h3 className="font-bold text-white text-sm">{selectedNode.label}</h3>
                        <button onClick={() => setSelectedNode(null)} className="text-zinc-400 hover:text-white">
                            <XCircle size={16} />
                        </button>
                    </div>
                    <div className="text-xs text-zinc-300 space-y-2 font-mono">
                        <p><span className="text-cyan-500">Time:</span> {new Date(selectedNode.details.timestamp).toLocaleString()}</p>
                        <p><span className="text-cyan-500">Scene:</span> {selectedNode.details.scene}</p>
                        <p><span className="text-cyan-500">State:</span> {selectedNode.details.user_state}</p>
                        <div className="flex flex-wrap gap-1 mt-2">
                            {selectedNode.details.entities.map((e: string, i: number) => (
                                <span key={i} className="px-1.5 py-0.5 bg-cyan-900/30 text-cyan-300 rounded border border-cyan-800/50">
                                    {e}
                                </span>
                            ))}
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}
