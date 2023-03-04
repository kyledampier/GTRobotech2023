<script lang="ts">
  import { onMount } from "svelte";
  import { writable } from "svelte/store";
  import { get } from "svelte/store";

  import UserProfile from "../../components/UserProfile.svelte";
  import MessagingContent from "../../components/MessagingContent.svelte";

  let messageValue: string;
</script>

<div class="container">
  <div class="sidebar" />
  <div class="col">
    <UserProfile
      name="John Doe"
      imgSrc="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Lion_waiting_in_Namibia.jpg/440px-Lion_waiting_in_Namibia.jpg"
    />
    <MessagingContent />
    <textarea
      placeholder="Type your message here..."
      bind:value={messageValue}
    />
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
</style>
