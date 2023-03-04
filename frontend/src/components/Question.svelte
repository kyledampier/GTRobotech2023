<!-- Displays question with number next to it -->
<!-- 8 | How are you? -->

<script>
    import init from '../lib/init.json';

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
    let question = init.survey[index].question;

    function onChange() {
        if (selected) {
            index += 1;
        }
        question = init.survey[index].question;
        selected = false;
    }

</script>

<p>{index+1} |</p>
<h1>{question}</h1>

<div class="form">
    {#each values as value}
    <label>
        <input type=radio name="scale" bind:group={selected} value={value} on:change={onChange}>
    </label>
    {/each}
</div>


<style>
    h1 {
        text-align: center;
    }
    .form {
        text-align: center;
    }

</style>