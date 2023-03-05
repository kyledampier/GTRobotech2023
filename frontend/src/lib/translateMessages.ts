import type { Message } from "../types/Message";

export function translateMessages(messages: Message[]): { role: string, content: string}[] {
    let output: { role: string, content: string}[] = [];

    messages.forEach((message) => {
        if ("from" in message) {
            output.push({ role: "assistant", content: message.from });
        } else {
            output.push({ role: "user", content: message.to });
        }
    });

    return output;
}

export function outputMessages(messages: { role: string, content: string}[]): Message[] {
    let output: Message[] = [];

    messages.forEach((message) => {
        if (message.role === "assistant") {
            output.push({ from: message.content, timestamp: Date.now() });
        } else {
            output.push({ to: message.content, timestamp: Date.now() });
        }
    });

    return output;
}