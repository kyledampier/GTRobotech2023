<script lang="ts">
  import { db } from "$lib/firebase";
  import { setDoc, doc } from "firebase/firestore";

  export let uid: string;
  let path = "http://localhost:8000/";
  let newChatUid: string;

  async function newChat() {
    let profileReq = await fetch(path + "profile", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
    });

    let uidReq = await fetch(path + "get_partner", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
      body: JSON.stringify({
        uid: uid,
      }),
    });

    let profileUid = await uidReq.json();
    let profile = await profileReq.json();

    setDoc(doc(db, `users/${uid}/messages`, profileUid), {
      name: profile.name,
      imgSrc: profile.imgSrc,
      messages: []
    });

    console.log("new profile", await profileReq.json());
  }
</script>

<button on:click={newChat}> <span class="icon">+</span>New Chat</button>

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
