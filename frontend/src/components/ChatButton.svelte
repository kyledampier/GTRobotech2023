<script lang="ts">
  export let lastMessage: string;
  export let name: string;
  export let imgSrc: string;
  export let id: string;
  export let selectedChat: string;

  export let onClick = (id: string) => {};

  function onClickDiv() {
    onClick(id);
  }

</script>

<div on:click={onClickDiv} style="background-color: {selectedChat == id ? '#373737' : 'transparent'}">
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
