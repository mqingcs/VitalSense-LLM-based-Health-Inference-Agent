"use client";

import { Canvas } from "@react-three/fiber";
import { OrbitControls, Sphere, MeshDistortMaterial } from "@react-three/drei";
import { useEffect, useState } from "react";
import { socket } from "@/lib/socket";

export default function DigitalTwin() {
    const [riskLevel, setRiskLevel] = useState<"LOW" | "MEDIUM" | "HIGH">("LOW");

    useEffect(() => {
        socket.on("analysis_result", (data: any) => {
            setRiskLevel(data.risk_level);
        });
        return () => {
            socket.off("analysis_result");
        };
    }, []);

    const getColor = () => {
        switch (riskLevel) {
            case "HIGH": return "#ef4444"; // Red
            case "MEDIUM": return "#f59e0b"; // Amber
            case "LOW": return "#10b981"; // Emerald
            default: return "#10b981";
        }
    };

    return (
        <div className="h-full w-full relative bg-zinc-950 rounded-lg border border-zinc-800 overflow-hidden">
            <div className="absolute top-4 left-4 z-10">
                <h2 className="text-zinc-400 font-mono text-xs uppercase tracking-widest">Digital Twin Status</h2>
                <div className="text-2xl font-bold font-mono" style={{ color: getColor() }}>
                    {riskLevel} RISK
                </div>
            </div>

            <Canvas>
                <ambientLight intensity={0.5} />
                <directionalLight position={[10, 10, 5]} intensity={1} />
                <OrbitControls enableZoom={false} />

                {/* The "Brain" / Core */}
                <Sphere args={[1, 32, 32]} scale={2}>
                    <MeshDistortMaterial
                        color={getColor()}
                        attach="material"
                        distort={0.6}
                        speed={2}
                        roughness={0.2}
                        metalness={0.8}
                    />
                </Sphere>
            </Canvas>
        </div>
    );
}
