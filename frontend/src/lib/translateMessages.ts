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