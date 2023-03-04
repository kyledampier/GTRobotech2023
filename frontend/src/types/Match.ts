import type { Message } from "./Message";

export type Match = {
    id: string;
    name: string;
    imgSrc: string;
    messages?: Message[];
}