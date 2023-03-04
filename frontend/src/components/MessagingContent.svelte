<script lang="ts">
  import { uid } from "$lib/example_messages.json";

  const messages = [
    {
      timestamp: "2009-11-10T22:00:00Z",
      from: "some message",
    },
    {
      timestamp: "2009-11-10T23:00:00Z",
      to: "some response to the message",
    },
    {
      timestamp: "2009-11-11T00:00:00Z",
      from: "some message",
    },
    {
      timestamp: "2009-11-11T01:00:00Z",
      to: "some response to the message",
    },
  ];

  //   console.log(uid);
</script>

<div class="expand">
  {#each messages as message}
    {#if "to" in message}
      <p class="to">{message.to}</p>
    {/if}
    {#if "from" in message}
      <p class="from">{message.from}</p>
    {/if}
  {/each}
</div>

<style>
  div {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: flex-end;
    /* height: 120px; */
    width: calc(100vw - 320px - 2em);
    border-bottom: 1px solid #828282;
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
    overflow: scroll;
  }
</style>
