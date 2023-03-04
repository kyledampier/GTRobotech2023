<script>
    import { tweened } from "svelte/motion";
    import { cubicOut } from "svelte/easing";

    const progress = tweened(0, {
        duration: 400,
        easing: cubicOut
    });
</script>

<progress value="{$progress}"></progress>

<style>
	progress {
		display: block;
		width: 100%;
	}
</style>