<script>
  let videoSource = null;
  let loading = false;
  const startVideo = async () => {
    try {
      loading = true;
      const stream = await navigator.mediaDevices.getUserMedia({
        video: true,
      });
      videoSource.srcObject = stream;
      videoSource.play();
      loading = false;
    } catch (error) {
      console.log(error);
    }
  };
</script>

<div>
  {#if loading}
    <!-- TODO: Make this a circly thingy -->
    <h1>LOADING</h1>
  {/if}
  <!-- svelte-ignore a11y-media-has-caption -->
  <video bind:this={videoSource} />
  <button on:click={startVideo}>Start Video</button>
</div>
