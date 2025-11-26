import CouncilRoom from "@/components/CouncilRoom";
import DigitalTwin from "@/components/DigitalTwin";
import InterventionModal from "@/components/InterventionModal";
import MemoryGalaxy from "@/components/MemoryGalaxy";
import SessionTimeline from "@/components/SessionTimeline";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-6 bg-black text-white pb-64">
      <InterventionModal />
      <SessionTimeline />

      <div className="z-10 w-full max-w-7xl items-center justify-between font-mono text-sm lg:flex mb-8">
        <p className="fixed left-0 top-0 flex w-full justify-center border-b border-zinc-800 bg-black pb-6 pt-8 backdrop-blur-2xl lg:static lg:w-auto lg:rounded-xl lg:border lg:bg-zinc-900/50 lg:p-4">
          <span className="font-bold text-emerald-500 mr-2">VitalOS</span>
          <span className="text-zinc-500">Health Intelligence Platform</span>
        </p>
      </div>

      <div className="w-full max-w-7xl grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Left Column: Visualization */}
        <div className="flex flex-col gap-8">
          <div className="h-[500px] w-full bg-zinc-900/20 rounded-xl border border-zinc-800 overflow-hidden relative">
            <DigitalTwin />
            <div className="absolute bottom-4 left-4 text-xs text-zinc-500 font-mono">
              DIGITAL TWIN v2.0
            </div>
          </div>

          <MemoryGalaxy />
        </div>

        {/* Right Column: Cognition */}
        <div className="h-full">
          <CouncilRoom />
        </div>
      </div>
    </main>
  );
}
