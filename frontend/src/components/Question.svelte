<!-- Displays question with number next to it -->
<!-- 8 | How are you? -->

<script>
// @ts-nocheck

    import { survey } from '../lib/init.json';
    import { tweened } from "svelte/motion";
    import { cubicOut } from "svelte/easing";

    let selected;
    let index = 0;
    let total = 20;
    let question = survey[index].question;

    const progress = tweened(0, {
        duration: 400,
        easing: cubicOut
    });

    function onChange() {
        if (index != 19) {
            if (selected !== null) {
                index += 1;
            }
            question = survey[index].question;
            selected = null;
            progress.set(index/total);
        } else {
            progress.set(100);
            // reroute
        }
    }

</script>

<div class="container">
    <p>{index+1} |</p>
    <h1>{question}</h1>
</div>

<div class="form">
    <input type=radio class="radio-lg pink" name="scale" bind:group={selected} value={1} on:change={onChange}>
    <input type=radio class="radio-md pink" name="scale" bind:group={selected} value={2} on:change={onChange}>
    <input type=radio class="radio-sm pink" name="scale" bind:group={selected} value={3} on:change={onChange}>
    <input type=radio class="radio-ne gray" name="scale" bind:group={selected} value={4} on:change={onChange}>
    <input type=radio class="radio-sm green" name="scale" bind:group={selected} value={5} on:change={onChange}>
    <input type=radio class="radio-md green" name="scale" bind:group={selected} value={6} on:change={onChange}>
    <input type=radio class="radio-lg green" name="scale" bind:group={selected} value={7} on:change={onChange}>
</div>

<div class="footer">
    <progress value="{$progress}"></progress>
</div>

<style>
    .container {
        display: flex;
        justify-content: center;
        align-items: flex-start;
    }

    h1 {
        max-width: 75vw;
        text-align: center;
    }
    p {
        font-size: 135%;
        padding-right: 10px;
        justify-content: left;
    }
    input[type=radio] {
        -webkit-appearance: none;
        -moz-appearance: none;
        -ms-appearance: none;
        -o-appearance: none;
        appearance: none;
        position: relative;
        top: 13.33333px;
        right: 0;
        bottom: 0;
        left: 0;
        transition: all 0.15s ease-out 0s;
        background: #373737;
        cursor: pointer;
        display: inline-block;
        margin-right: 0.5rem;
        outline: none;
        position: relative;
        z-index: 1000;
        border-radius: 50%;
    }
    .radio-lg {
        height: 50px;
        width: 50px;
    }
    .radio-md {
        height: 42px;
        width: 42px;
    }
    .radio-sm {
        height: 34px;
        width: 34px;
    }
    .radio-ne {
        height: 25px;
        width: 25px;
    }
    .pink {
        border: solid #B804B1;
    }
    .green {
        border: solid #69FF51;
    }
    .gray {
        border: solid gray;
    }
    .form {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    progress {
		display: block;
		width: 100%;
        border: none;
        background-color: #635f5f;
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