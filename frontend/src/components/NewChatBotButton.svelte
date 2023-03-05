<script lang="ts">
  import { db } from "$lib/firebase";
  import type { Message } from "../types/Message";
  import { getDoc, doc } from "firebase/firestore";

  export let botProfile: { name: string; imgSrc: string };
  export let uid: string;
  export let selectedChat: string;
  let path = "http://localhost:8000/";

  export let setMessages = (messages: Message[]) => {};

  async function chatWithBot() {
    let profileReq = await fetch(path + "profile", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
    });

    let profile = await profileReq.json();
    profile.username = profile.username + " (bot)";
    console.log(profile);

    let profileDoc = doc(db, "users", uid);
    let profileSnap = await getDoc(profileDoc);
    let profileData = profileSnap.data();

    let newChatBot = await fetch(path + "start_chatbot", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
      body: JSON.stringify(profileData),
    });

    const newChatBotData = await newChatBot.json();
    let idx = newChatBotData.length - 1;

    setMessages([
      {
        from: newChatBotData[idx].content,
        timestamp: Date.now().toString(),
      },
    ]);

    botProfile = {
      name: profile.username,
      imgSrc: profile.image_path,
    };
    selectedChat = "";
  }
</script>

<button on:click={chatWithBot}>
  <span class="icon">🤖</span>Chat With Bot</button
>

<style>
  button {
    background-color: #373737;
    color: white;
    border: 1px solid #404040;
    border-radius: 0.5rem;
    padding: 0.5rem 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    padding: 0.5em;
    margin: 1em 2em;
    font-size: 1rem;
    transition: all 0.5s ease-in-out;
  }

  button:hover {
    background-color: #404040;
    filter: drop-shadow(0px 8px 5px #222);
  }

  .icon {
    font-size: 2rem;
    margin-right: 0.5rem;
  }
</style>
