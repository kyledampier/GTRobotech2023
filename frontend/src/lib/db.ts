import { MONGO_URL } from './config.json';
import { MongoClient } from 'mongodb';

export const client = await new MongoClient(MONGO_URL).connect();
