<script>
  import { spring } from "svelte/motion";

  export let titles;
  export let val = 0;


  let num_titles = titles.length;

  // Animation Logic
  const displayed_val = spring();
  $: displayed_val.set(val);
  $: offset = modulo($displayed_val, 1);
  function modulo(n, m) {
    // handle negative numbers
    return ((n % m) + m) % m;
  }

  function nextTitle(n) {
    return (n + 1) % num_titles;
  }
</script>

<div class="title">
  <div class="title-viewport">
    <div class="title-display" style="transform: translate(0, {100 * offset}%)">
      <strong class="hidden" aria-hidden="true">
        {titles[Math.floor(nextTitle($displayed_val))]}
      </strong>
      <strong>
        {titles[Math.floor($displayed_val)]}
      </strong>
    </div>
  </div>
</div>

<style>
  .title {
    display: flex;
    width: 66vw;
    user-select: none;
    color: #fff;
  }

  .title-viewport {
    width: 100%;
    height: 25vh;
    overflow: hidden;
    text-align: center;
    position: relative;
  }

  .title-viewport strong {
    position: absolute;
    display: flex;
    width: 100%;
    height: 100%;
    font-weight: bold;
    color: #fff;
    font-size: 1rem;
    align-items: flex-start;
    justify-content: center;
  }

  .title-display {
    position: absolute;
    width: 100%;
    height: 100%;
  }

  .hidden {
    top: -100%;
    user-select: none;
  }

  strong {
    font-weight: bold;
  }

  @media (min-width: 640px) {
    .title-viewport strong {
      font-size: 2.4em;
    }
  }
</style>
