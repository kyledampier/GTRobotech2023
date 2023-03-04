import { FIREBASE_CONFIG } from "./config.json";
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

// Initialize Firebase
export const app = initializeApp(FIREBASE_CONFIG);
export const db = getFirestore(app);