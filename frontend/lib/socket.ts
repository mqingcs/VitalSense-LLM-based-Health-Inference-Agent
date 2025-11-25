"use client";

import { io } from "socket.io-client";

// Connect to the FastAPI Backend
export const socket = io("http://localhost:8000", {
  transports: ["websocket"],
  autoConnect: true,
});
