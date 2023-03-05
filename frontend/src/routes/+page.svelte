
<header>
    <img style="padding-left:30px" width="150px" height="150px" src="./static/logo_white.png" alt="logo">
    <a href="/questions">
        <p><b>Start Networking</b></p>
        <img class="arrow" width=32px height=32px src="https://cdn-icons-png.flaticon.com/512/32/32213.png" alt="arrow">
    </a>
</header>

<div>
    <h1>Welcome to The Neural Network</h1>
    <div class="horizontal">
        <div>
            <p>The Neural Network is a safe space that reminds you that you are not alone; where you can feel comfortable and supported, even during difficult times. It's a virtual space where you can express yourself freely without fear of judgment, criticism, or discrimination.</p>
            <p>This safe space is designed to provide a sense of community and belonging, where individuals can come together to share their experiences, thoughts, and emotions anonymously without feeling isolated or disconnected. It's a place where you can find others who have been through similar struggles and can offer support and understanding.</p>
            <p>It's a reminder that you are not alone in your struggles and that there are others who care about you and are ready to support you on your journey.</p>
        </div>
        
        <img class="graphic" width=500px height=500px src="https://static.vecteezy.com/system/resources/thumbnails/011/032/492/small/head-icon-for-mental-health-and-emotion-symbol-png.png" alt="logo">      
    </div>
</div>

<style>

    @keyframes appear {
    from 
    {
        display:none;
        opacity: 0; 
    }
    to 
    {
        display: block;
        opacity: 1;
    }
    }

    @keyframes slide {
    from 
    {
        padding-right: 30px;
    }
    to 
    {
        padding-right: 35px;
    }
    }

    h1
    {
        margin: 0;
    }

    header
    {
        border-bottom: solid;
        border-color: white;
        border-width: 3px;
        margin-right: 30px;
        margin-left:30px;
        align-items: center;
        justify-content: center;
    }

    header a
    {
        text-decoration: none;
        display: flex;
        flex-direction: row;
        background: none;
        border: none;
        float: right;
        margin-top: 35px;
        padding-right: 30px;
    }

    header a:hover
    {
        animation-name: slide;
        animation-duration: 1000ms;
        padding-right: 35px;
    }

    header a:hover  .arrow
    {
        animation-name: appear;
        animation-duration: 1000ms;
        display: block;
    }

    .graphic
    {
        filter: saturate(0);
    }

    .arrow
    {
        display: none;
        padding-right: -10px;
        padding-top: 30px;
        filter: invert();
    }

    header a p
    {
        font-size: 28px;
        color: white;
        padding-right: 30px;
    }

    h1
    {
        font-size: 64px;
    }
    div
    {
        display: flex;
        flex-direction: column;
        align-content: center;
        justify-content: center;
        padding: 30px
    }
    p
    {
        font-size: 24px;
    }

    .horizontal
    {
        flex-direction: row;
    }

    .horizontal p
    {
        margin: 10px;
        padding: 0;
    }
</style>