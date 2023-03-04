import { MONGO_URL } from "$lib/config.json"
import { MongoClient } from 'mongodb';

const client = new MongoClient(MONGO_URL);
client.connect().then(() => console.log('connected to db')).catch(err => console.log(err));

type MessageRequest = {
    toUid: string;
    fromUid: string;
    message: string;
}

export async function put({ params }) {
    console.log(params);
    const db = client.db();
    const collection = db.collection('messages');
    const message = await collection.findOne({ id: params.id });
    console.log(message);
    return { body: message };
}