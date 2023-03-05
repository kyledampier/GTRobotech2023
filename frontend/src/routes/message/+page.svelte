<script lang="ts">
  import { onMount } from "svelte";
  import {
    collection,
    query,
    onSnapshot,
    doc,
    arrayUnion,
    setDoc,
  } from "firebase/firestore";
  import type { Message } from "../../types/Message";
  import type { Match } from "../../types/Match";
  import { db } from "$lib/firebase";
  import { translateMessages, outputMessages } from "$lib/translateMessages";

  import UserProfile from "../../components/UserProfile.svelte";
  import ChatButton from "../../components/ChatButton.svelte";
  import MessagingContent from "../../components/MessagingContent.svelte";
  import NewChatButton from "../../components/NewChatButton.svelte";
  import NewChatBotButton from "../../components/NewChatBotButton.svelte";

  let messageValue: string;
  let messages: Message[] = [];
  let container: HTMLDivElement;
  let uid = "eZslI0Kmwnm4f6bZYNUq";
  let selectedChat: string = "Ty7FnLqr1NwiNAFi752S";
  let botProfile: { name: string; imgSrc: string } | {};

  let path = "http://localhost:8000/";

  onMount(() => {
    uid = localStorage.getItem("uid") as string;
  });

  function switchUsers() {
    let tmp = uid;
    uid = selectedChat;
    selectedChat = tmp;
  }
  //switchUsers();

  let matches: Match[] = [];

  onMount(async () => {
    let userMessages = collection(db, `users/${uid}/messages`);
    let messagesQuery = query(userMessages);
    onSnapshot(messagesQuery, (snapshot) => {
      matches = [];
      snapshot.docChanges().forEach((change) => {
        let tmp = change.doc.data() as Match;
        matches.push({
          id: change.doc.id,
          name: tmp.name,
          imgSrc: tmp.imgSrc,
          messages: tmp.messages,
        });

        if (selectedChat === change.doc.id) {
          messages = tmp.messages as Message[];
        }
        container.scrollTop = container.scrollHeight;
      });
    });
  });

  function setMessages(msgs: Message[]) {
    messages = msgs;
  }

  function onClick(id: string) {
    selectedChat = id;
    messages = matches.find((match) => match.id === id)?.messages as Message[];
    botProfile = {};
  }

  async function sendMessage() {
    if (Object.keys(botProfile).length !== 0) {
      let botMsg = {
        timestamp: Date.now().toString(),
        to: messageValue,
      };
      const translatedMsgs = translateMessages(messages);

      messages = [...messages, botMsg];

      let botReq = await fetch(path + "chat_with_bot", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
        body: JSON.stringify({ messages: translatedMsgs, input: messageValue }),
      });

      let chatData = await botReq.json();
      let chatResult = outputMessages(chatData);

      messages = chatResult;

      messageValue = "";
      container.scrollTo({ top: container.scrollHeight });
      return;
    }

    // Update my messages
    let msgRef = doc(db, `users/${uid}/messages/${selectedChat}`);
    if (messageValue.length > 0) {
      setDoc(
        msgRef,
        {
          messages: arrayUnion({
            timestamp: Date.now().toString(),
            to: messageValue,
          }),
        },
        { merge: true }
      );
    }

    // Update other user's messages
    let otherRef = doc(db, `users/${selectedChat}/messages/${uid}`);
    if (messageValue.length > 0) {
      setDoc(
        otherRef,
        {
          messages: arrayUnion({
            timestamp: Date.now().toString(),
            from: messageValue,
          }),
        },
        { merge: true }
      );
    }
    container.scrollTo({ top: container.scrollHeight });
  }

  const onKeyPress = (e: any) => {
    if (e.charCode === 13) sendMessage();
  };
</script>

<div class="container">
  <div class="sidebar">
    {#each matches as match}
      <ChatButton
        name={match.name}
        imgSrc={match.imgSrc}
        id={match.id}
        lastMessage={"Last Message"}
        {onClick}
        bind:selectedChat
      />
    {/each}
    <NewChatButton bind:uid />
    <NewChatBotButton
      bind:uid
      {setMessages}
      bind:botProfile
      bind:selectedChat
    />
  </div>
  <div class="col">
    <UserProfile
      name={botProfile ? botProfile.name : "Bot"}
      imgSrc={botProfile ? botProfile.imgSrc : "/pfps/unicorn.png"}
    />
    <MessagingContent bind:messages bind:container />
    <div class="inputBar">
      <textarea
        on:keypress={onKeyPress}
        placeholder="Type your message here..."
        bind:value={messageValue}
      />
      <button on:click={sendMessage} class="msgBtn">
        <img
          class="msgIcon"
          width="48px"
          height="48px"
          src="/icons/send.png"
          alt="paper_plane"
        />
      </button>
    </div>
  </div>
</div>

<style>
  .container {
    display: flex;
    width: 100vw;
    height: calc(100vh - 12px);
    border-top: 12px solid #69ff5188;
    overflow: hidden;
  }

  .container {
    background-color: #373737;
  }

  .sidebar {
    display: flex;
    flex-direction: column;
    gap: 0px;
    width: 320px;
    background-color: #202020;
  }

  .col {
    display: flex;
    flex-direction: column;
    overflow: scroll;
    padding: 1em;
  }

  .inputBar {
    display: flex;
    flex-direction: row;
  }

  textarea {
    border: none;
    background-color: #202020;
    color: #fff;
    padding: 1em;
    font-size: 1.2em;
    resize: none;
    outline: none;
    border-radius: 1em;
    font-family: "Poppins", sans-serif;
    font-weight: 300;
    width: calc(100% - 2em);
    margin-top: 10px;
  }

  .msgBtn {
    border: none;
    margin-left: 10px;
    margin-top: 10px;
    background-color: #202020;
    border-radius: 1em;
    padding: 12px;
    outline: none;
  }

  .msgIcon {
    filter: invert(60%);
  }
</style>
