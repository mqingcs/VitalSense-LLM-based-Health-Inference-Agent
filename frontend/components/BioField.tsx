"use client";

import { useRef, useMemo, useEffect } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import * as THREE from "three";
import { socket } from "@/lib/socket";

// --- GLSL Shaders ---
const vertexShader = `
varying vec2 vUv;
void main() {
  vUv = uv;
  gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}
`;

const fragmentShader = `
uniform float uTime;
uniform vec3 uColor;
uniform float uTurbulence;
varying vec2 vUv;

// Simplex Noise (simplified)
vec3 permute(vec3 x) { return mod(((x*34.0)+1.0)*x, 289.0); }

float snoise(vec2 v){
  const vec4 C = vec4(0.211324865405187, 0.366025403784439,
           -0.577350269189626, 0.024390243902439);
  vec2 i  = floor(v + dot(v, C.yy) );
  vec2 x0 = v -   i + dot(i, C.xx);
  vec2 i1;
  i1 = (x0.x > x0.y) ? vec2(1.0, 0.0) : vec2(0.0, 1.0);
  vec4 x12 = x0.xyxy + C.xxzz;
  x12.xy -= i1;
  i = mod(i, 289.0);
  vec3 p = permute( permute( i.y + vec3(0.0, i1.y, 1.0 ))
  + i.x + vec3(0.0, i1.x, 1.0 ));
  vec3 m = max(0.5 - vec3(dot(x0,x0), dot(x12.xy,x12.xy), dot(x12.zw,x12.zw)), 0.0);
  m = m*m ;
  m = m*m ;
  vec3 x = 2.0 * fract(p * C.www) - 1.0;
  vec3 h = abs(x) - 0.5;
  vec3 ox = floor(x + 0.5);
  vec3 a0 = x - ox;
  m *= 1.79284291400159 - 0.85373472095314 * ( a0*a0 + h*h );
  vec3 g;
  g.x  = a0.x  * x0.x  + h.x  * x0.y;
  g.yz = a0.yz * x12.xz + h.yz * x12.yw;
  return 130.0 * dot(m, g);
}

void main() {
  vec2 uv = vUv;
  
  // Dynamic Noise Flow
  float noise = snoise(uv * 3.0 + uTime * 0.2);
  float detail = snoise(uv * 10.0 - uTime * 0.1) * uTurbulence;
  
  // Mixing
  float pattern = noise + detail;
  
  // Vignette
  float dist = distance(uv, vec2(0.5));
  float vignette = smoothstep(0.8, 0.2, dist);
  
  // Color Grading
  vec3 baseColor = uColor;
  vec3 darkColor = baseColor * 0.2;
  
  vec3 finalColor = mix(darkColor, baseColor, pattern * 0.5 + 0.5);
  finalColor *= vignette;
  
  gl_FragColor = vec4(finalColor, 1.0);
}
`;

function BioPlane() {
    const mesh = useRef<THREE.Mesh>(null);

    // Uniforms
    const uniforms = useMemo(
        () => ({
            uTime: { value: 0 },
            uColor: { value: new THREE.Color("#000000") }, // Start Black
            uTurbulence: { value: 0.1 },
            uSpeed: { value: 0.2 } // JS side control
        }),
        []
    );

    // Socket Listener
    useEffect(() => {
        socket.on("environment_update", (payload: any) => {
            // payload: { hex_color, turbulence, speed, brightness }
            if (payload.hex_color) {
                // Smooth transition handled in useFrame or GSAP? 
                // For simplicity, we lerp in useFrame, here we set targets
                // But uniforms are refs, so we need a target ref
                targetColor.current.set(payload.hex_color);
                targetTurbulence.current = payload.turbulence;
                targetSpeed.current = payload.speed;
            }
        });

        return () => {
            socket.off("environment_update");
        };
    }, []);

    // Animation State
    const targetColor = useRef(new THREE.Color("#06b6d4")); // Default Cyan
    const targetTurbulence = useRef(0.2);
    const targetSpeed = useRef(0.2);

    useFrame((state) => {
        if (mesh.current) {
            const material = mesh.current.material as THREE.ShaderMaterial;

            // Time
            material.uniforms.uTime.value += 0.01 * (1.0 + material.uniforms.uSpeed.value);

            // Lerp Values
            material.uniforms.uColor.value.lerp(targetColor.current, 0.02);
            material.uniforms.uTurbulence.value += (targetTurbulence.current - material.uniforms.uTurbulence.value) * 0.02;

            // Speed is not a uniform in shader but controls time step
            // We store it in uniform for convenience but use it in JS
            material.uniforms.uSpeed.value += (targetSpeed.current - material.uniforms.uSpeed.value) * 0.02;
        }
    });

    return (
        <mesh ref={mesh} position={[0, 0, 0]} scale={[20, 10, 1]}>
            <planeGeometry args={[1, 1, 32, 32]} />
            <shaderMaterial
                fragmentShader={fragmentShader}
                vertexShader={vertexShader}
                uniforms={uniforms}
                transparent={true}
            />
        </mesh>
    );
}

export default function BioField() {
    return (
        <div className="fixed top-0 left-0 w-full h-full -z-50 bg-black">
            <Canvas camera={{ position: [0, 0, 5] }}>
                <BioPlane />
            </Canvas>
            {/* Overlay Gradient for readability */}
            <div className="absolute inset-0 bg-gradient-to-b from-black/80 via-transparent to-black/80 pointer-events-none" />
        </div>
    );
}
