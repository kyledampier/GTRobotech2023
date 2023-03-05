<script lang="ts">
  import { uid } from "$lib/example_messages.json";
  import type { Message } from "../types/Message";
  import FoundAnonymousChat from "../components/FoundAnonymousChat.svelte";

  export let container: HTMLDivElement;
  export let messages: Message[] = [];
</script>

<div class="expand" id="msgDisplay" bind:this={container}>
  {#if messages.length === 0}
    <p class="noMessages">No messages yet</p>
  {/if}
  {#each messages as message}
    {#if "to" in message}
      <p class="to">{message.to}</p>
    {/if}
    {#if "from" in message}
      <p class="from">{message.from}</p>
    {/if}
  {/each}
</div>

<!-- <FoundAnonymousChat/> -->
<style>
  div {
    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
    width: calc(100vw - 320px - 2em);
    border-bottom: 1px solid #828282;
    overflow-y: scroll;
  }

  .to {
    background-color: #444444;
    color: #fff;
    padding: 1em;
    border-radius: 1em;
    margin: 1em;
    margin-left: auto;
    max-width: 75%;
    text-align: right;
  }

  .from {
    background-color: #2c2c2c;
    color: #fff;
    padding: 1em;
    border-radius: 1em;
    margin: 1em;
    margin-right: auto;
    max-width: 75%;
    text-align: left;
  }

  .expand {
    flex: 1;
    overflow-y: scroll;
  }

  .noMessages {
    margin: 1em;
    color: #828282;
    margin: 0 auto;
    margin-top: 1em;
  }
</style>
