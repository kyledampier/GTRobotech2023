<script lang="ts">
  import { onMount } from "svelte";
  import { writable } from "svelte/store";
  import { get } from "svelte/store";
  import type  { Message } from "../../types/Message";

  import UserProfile from "../../components/UserProfile.svelte";
  import MessagingContent from "../../components/MessagingContent.svelte";

  let messageValue: string;
  let messages: Message[];
  let container: HTMLDivElement;

  function sendMessage()
  {
    console.log("clicked")
    if (messageValue.length > 0)
    {
      messages.push(
      {
        "timestamp": Date.now().toString(),
        "to": messageValue
      }
      )
      messages = messages
      messageValue = ""
      container.scrollTop = container.scrollHeight
      
    }
  }

  const onKeyPress = e => {
    if (e.charCode === 13) sendMessage();
  }
</script>

<div class="container">
  <div class="sidebar" />
  <div class="col">
    <UserProfile
      name="John Doe"
      imgSrc="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Lion_waiting_in_Namibia.jpg/440px-Lion_waiting_in_Namibia.jpg"
    />
    <MessagingContent bind:messages bind:container />
    <div class="inputBar">
      <textarea
      on:keypress={onKeyPress}
      placeholder="Type your message here..."
      bind:value={messageValue}
    />
    <button on:click={sendMessage} class="msgBtn">
      <img class="msgIcon" width="70px" height="70px" src="https://icon-library.com/images/send-message-icon-png/send-message-icon-png-24.jpg" alt="paper_plane">
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

  .msgBtn{
    border: none;
    margin-left: 10px;
    margin-top: 10px;
    background-color: #202020;
    border-radius: 1em;
    outline: none;
  }  

  .msgIcon{
    filter: invert(60%);
  }

</style>
