<!-- Displays question with number next to it -->
<!-- 8 | How are you? -->

<script>
    import init from '../lib/init.json';
    import { tweened } from "svelte/motion";
    import { cubicOut } from "svelte/easing";

    const values = [
        { label: 'never', value: 1},
        { label: '', value: 2},
        { label: '', value: 3},
        { label: '', value: 4},
        { label: '', value: 5},
        { label: '', value: 6},
        { label: 'always', value: 7}
    ];

    let selected = false;
    let index = 0;
    let total = 20;
    let question = init.survey[index].question;

    const progress = tweened(0, {
        duration: 400,
        easing: cubicOut
    });

    function onChange() {
        if (selected) {
            index += 1;
        }
        question = init.survey[index].question;
        selected = false;
        progress.set(index/total);
    }

</script>

<div class="container">
    <p>{index+1} |</p>
    <h1>{question}</h1>
</div>

<div class="form">
    {#each values as value}
    <label>
        <input type=radio name="scale" bind:group={selected} value={value} on:change={onChange}>
    </label>
    {/each}
</div>

<div class="footer">
    <progress value="{$progress}"></progress>
</div>

<style>
    .container {
        display: flex;
        justify-content: center;
    }
    p {
        font-size: 135%;
        padding-right: 10px;
    }
    .form {
        text-align: center;
    }
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
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
    }
</style>