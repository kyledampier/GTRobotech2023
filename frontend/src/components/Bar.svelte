<script>
    import { tweened } from "svelte/motion";
    import { cubicOut } from "svelte/easing";
    
    const progress = tweened(0, {
        duration: 400,
        easing: cubicOut
    });
</script>

<progress value="{$progress}"></progress>
<button on:click="{() => progress.set(0.25)}">
	25%
</button>


<style>
	progress {
		display: block;
		width: 100%;
        background-color: #373737;
	}

    progress::-webkit-progress-value {
        background-color: rgba(105, 255, 81, .75);
    }

    progress::-moz-progress-bar {
        background-color: rgba(105, 255, 81, .75);
    }
</style>