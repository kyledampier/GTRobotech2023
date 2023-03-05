<!-- 8 | How are you? -->
<script>
  // @ts-nocheck

  import { survey } from "../lib/init.json";
  import { tweened } from "svelte/motion";
  import { cubicOut } from "svelte/easing";
  import { onMount } from "svelte";
  import { db } from "$lib/firebase";
  import { addDoc, collection } from "firebase/firestore";
  import { goto } from "$app/navigation";
  import TitleAnimated from "./TitleAnimated.svelte";

  let selected;
  let index = 0;
  let total = 20;

  let questions = [];
  for (let q in survey) {
    questions.push(survey[q].question);
  }

  let scale = survey[index].scale;

  let path = "http://localhost:8000/";
  let uid = "";

  const progress = tweened(0, {
    duration: 400,
    easing: cubicOut,
  });

  onMount(() => {
    if (localStorage.getItem("uid") !== null) {
        goto("/message");
    }
  });

  async function sendData() {
    let newUserDoc = await addDoc(collection(db, "users"), {
      survey: survey,
    });

    uid = newUserDoc.id;
    localStorage.setItem("uid", uid);

    const res = await fetch(path + "submit_form", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
      body: JSON.stringify({
        uid,
        survey,
      }),
    });
    const json = await res.json();
    result = JSON.stringify(json);
  }

  function onChange() {
    survey[index].answer = selected;
    if (index != 19) {
      if (selected !== null) {
        index += 1;
        progress.set(index / total);
      }
      selected = null;
      scale = survey[index].scale;
    } else {
      progress.set(100);
      sendData();
      goto('/message');
    }
  }
</script>

<div class="survey-item">
    <div class="container">
        <p>{index + 1} |</p>
        <!-- <h1>{question}</h1> -->
        <TitleAnimated bind:val={index} titles={questions} />

    </div>
    
    <div class="form">
        <div class="scale" style="justify-content: right;">
            {#if scale==="change"}
                <p>No change</p>
            {:else if scale==="never"}
                <p>Never</p>
            {:else if scale==="significant"}
                <p>No</p>
            {:else}
                <p>Bad</p>
            {/if}
        </div>

            <input type=radio class="radio-lg pink" name="scale" bind:group={selected} value={1} on:change={onChange}>
            <input type=radio class="radio-md pink" name="scale" bind:group={selected} value={2} on:change={onChange}>
            <input type=radio class="radio-sm pink" name="scale" bind:group={selected} value={3} on:change={onChange}>
            <input type=radio class="radio-ne gray" name="scale" bind:group={selected} value={4} on:change={onChange}>
            <input type=radio class="radio-sm green" name="scale" bind:group={selected} value={5} on:change={onChange}>
            <input type=radio class="radio-md green" name="scale" bind:group={selected} value={6} on:change={onChange}>
            <input type=radio class="radio-lg green" name="scale" bind:group={selected} value={7} on:change={onChange}>

        <div class="scale">
            {#if scale==="change"}
                <p>Significant change</p>
            {:else if scale==="never"}
                <p>Always</p>
            {:else if scale==="significant"}
                <p>Very significant</p>
            {:else}
                <p>Good</p>
            {/if}
        </div>
    </div>
    <div class="footer">
        <progress value="{$progress}"></progress>
    </div>
</div>


<style>
    .survey-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 100vh;
    }
    .container {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        width: 70vw;
    }
    p {
        font-size: 120%;
        padding-right: 10px;
        justify-content: left;
        margin-top: 10px;
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
        margin: 0px;
        outline: none;
        position: relative;
        z-index: 1000;
        border-radius: 50%;
    }
    .radio-lg {
        height: 9vw;
        width: 9vw;
    }
    .radio-md {
        height: 7.5vw;
        width: 7.5vw;
    }
    .radio-sm {
        height: 6vw;
        width: 6vw;
    }
    .radio-ne {
        height: 4.5vw;
        width: 4.5vw;
    }
    .pink {
        border: solid #B804B1;
        transition: all 1.0s ease-in-out; 
    }
    .pink:hover {
        border: 6px solid #B804B1;
        background-color: #B804B166;
    }
    .green {
        border: solid #69FF51;
        transition: all 1.0s ease-in-out;
    }
    .green:hover {
        border: 6px solid #69FF51;
        background-color: #69FF5166;
    }
    .gray {
        border: solid gray;
        transition: all 1.0s ease-in-out;
    }
    .gray:hover {
        border: 6px solid #808080;
        background-color: #80808066;
    }
    .scale {
        display: flex;
        height: 100%;
        align-items: center;
        gap: 50vw;
        width: 250px;
    }
    .scale > p {
        margin: 0px;
        margin-top: 27px;
        font-size: 1.4em;
    }
    .form {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 25vh;
        width: 100vw;
        gap: 1em;
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
        height: 12px;
    }
</style>
