"use client";

import { useEffect, useState, useRef } from "react";
import dynamic from "next/dynamic";
import { XCircle, Maximize2, Minimize2 } from "lucide-react";

// Dynamically import ForceGraph3D (it uses window, so no SSR)
const ForceGraph3D = dynamic(() => import("react-force-graph-3d"), {
    ssr: false,
});

export default function MemoryGalaxy() {
    const [graphData, setGraphData] = useState({ nodes: [], links: [] });
    const [selectedNode, setSelectedNode] = useState<any>(null);
    const [isFullScreen, setIsFullScreen] = useState(false);
    const [dimensions, setDimensions] = useState({ width: 800, height: 500 });

    const fgRef = useRef<any>(null);
    const containerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        // Fetch data from Backend
        fetch("http://localhost:8000/memories")
            .then((res) => res.json())
            .then((data) => setGraphData(data))
            .catch((err) => console.error("Failed to fetch memories:", err));
    }, []);

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

    return (
        <div
            ref={containerRef}
            className={`
                transition-all duration-500 ease-in-out border border-zinc-800 overflow-hidden bg-black/80 backdrop-blur-md
                ${isFullScreen
                    ? "fixed inset-0 z-[100] w-screen h-screen rounded-none"
                    : "relative w-full h-[500px] rounded-xl"
                }
            `}
        >
            {/* Header / Controls */}
            <div className="absolute top-4 left-4 z-10 pointer-events-none">
                <h2 className="text-xl font-bold text-cyan-400 tracking-widest uppercase drop-shadow-[0_0_10px_rgba(34,211,238,0.5)]">
                    Neural Constellation
                </h2>
                <p className="text-xs text-zinc-500 font-mono">Hippocampus Visualizer v1.0</p>
            </div>

            <div className="absolute top-4 right-4 z-10 flex gap-2">
                <button
                    onClick={toggleFullScreen}
                    className="p-2 bg-zinc-900/50 hover:bg-cyan-900/50 text-cyan-400 rounded-full border border-cyan-500/30 transition-colors backdrop-blur-sm"
                    title={isFullScreen ? "Exit Full Screen" : "Enter Full Screen"}
                >
                    {isFullScreen ? <Minimize2 size={20} /> : <Maximize2 size={20} />}
                </button>
            </div>

            <ForceGraph3D
                ref={fgRef}
                width={dimensions.width}
                height={dimensions.height}
                graphData={graphData}
                nodeLabel="label"
                nodeColor={(node: any) =>
                    node.group === 1 ? "#ef4444" : // High Risk (Red)
                        node.group === 2 ? "#facc15" : // Medium Risk (Yellow)
                            "#10b981" // Low Risk (Green)
                }
                nodeRelSize={6}
                nodeResolution={16}
                linkColor={() => "#3f3f46"} // Zinc-700
                linkWidth={1}
                linkOpacity={0.3}
                backgroundColor="#00000000" // Transparent
                showNavInfo={false}
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
                <div className="absolute bottom-8 right-8 w-96 bg-black/90 border border-cyan-500/50 p-6 rounded-xl shadow-[0_0_30px_rgba(6,182,212,0.2)] backdrop-blur-xl animate-in slide-in-from-bottom-10 z-20">
                    <div className="flex justify-between items-start mb-4 border-b border-zinc-800 pb-2">
                        <h3 className="font-bold text-cyan-50 text-lg">{selectedNode.label}</h3>
                        <button onClick={() => setSelectedNode(null)} className="text-zinc-500 hover:text-red-400 transition-colors">
                            <XCircle size={20} />
                        </button>
                    </div>
                    <div className="text-sm text-zinc-300 space-y-3 font-mono">
                        <div className="flex justify-between">
                            <span className="text-cyan-600">Time</span>
                            <span className="text-zinc-400">{new Date(selectedNode.details.timestamp).toLocaleString()}</span>
                        </div>
                        <div>
                            <span className="text-cyan-600 block mb-1">Scene</span>
                            <p className="text-zinc-100 bg-zinc-900/50 p-2 rounded border border-zinc-800">
                                {selectedNode.details.scene}
                            </p>
                        </div>
                        <div>
                            <span className="text-cyan-600 block mb-1">State</span>
                            <span className="text-yellow-500">{selectedNode.details.user_state}</span>
                        </div>
                        <div>
                            <span className="text-cyan-600 block mb-1">Entities</span>
                            <div className="flex flex-wrap gap-2">
                                {selectedNode.details.entities.map((e: string, i: number) => (
                                    <span key={i} className="px-2 py-1 text-xs bg-cyan-950/50 text-cyan-300 rounded-full border border-cyan-800/50 shadow-[0_0_10px_rgba(8,145,178,0.2)]">
                                        {e}
                                    </span>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}
