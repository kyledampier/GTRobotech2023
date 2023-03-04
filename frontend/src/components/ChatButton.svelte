<script lang="ts">
  export let lastMessage: string;
  export let name: string;
  export let imgSrc: string;
  export let selectedChat;
</script>

<div>
  <img src={imgSrc} alt={name} />
  <p>{lastMessage}</p>
</div>

<style>
  div {
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 10px;
    border-bottom: 1px solid #e6e6e666;
    height: 120px;
  }

  p {
    margin-left: 10px;
    font-weight: 300;
  }

  img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
  }
</style>
