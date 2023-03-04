<script>
  export let name = "Anonymous Lion";
  export let imgSrc = "";
</script>

<div>
  <img src={imgSrc} alt={name} />
  <h1>{name}</h1>
</div>

<style>
  img {
    display: flex;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin: 0 auto;
    object-fit: cover;
    margin-top: 10px;
  }

  h1 {
    font-size: 1rem;
    font-weight: normal;
    margin-top: 5px;
    margin-bottom: 10px;
  }

  div {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    /* height: 120px; */
    width: calc(100vw - 320px - 2em);
    border-bottom: 1px solid #828282;
  }
</style>
