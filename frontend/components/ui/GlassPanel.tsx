import { cn } from "@/lib/utils";
import { ReactNode } from "react";

interface GlassPanelProps {
    children: ReactNode;
    className?: string;
    intensity?: "low" | "medium" | "high";
}

export default function GlassPanel({ children, className, intensity = "medium" }: GlassPanelProps) {
    const intensityMap = {
        low: "bg-black/40 backdrop-blur-sm border-white/5",
        medium: "bg-black/60 backdrop-blur-md border-white/10",
        high: "bg-black/80 backdrop-blur-xl border-white/20"
    };

    return (
        <div className={cn(
            "relative overflow-hidden rounded-xl border shadow-xl transition-all duration-300",
            intensityMap[intensity],
            className
        )}>
            {/* Dynamic Noise/Gradient Overlay */}
            <div className="absolute inset-0 pointer-events-none opacity-20 bg-[url('/noise.png')] mix-blend-overlay" />
            <div className="absolute -inset-[100%] bg-gradient-to-br from-cyan-500/5 via-transparent to-purple-500/5 animate-slow-spin pointer-events-none blur-3xl" />

            {/* Content */}
            <div className="relative z-10 h-full w-full">
                {children}
            </div>
        </div>
    );
}
