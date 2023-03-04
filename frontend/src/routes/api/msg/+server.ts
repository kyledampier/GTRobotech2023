import { client } from '$lib/db';

type MessageRequest = {
    toUid: string;
    fromUid: string;
    message: string;
}

export async function POST({ request }: { request: Request }) {
    let req = await request.json() as MessageRequest;
    console.log(req);

    const db = client.db('users');
    const collection = db.collection('messages');
    collection.insertOne({ to: req.toUid, from: req.fromUid, message: req.message, timestamp: Date.now() });
    return new Response(JSON.stringify({ message: "Message sent" }));
}