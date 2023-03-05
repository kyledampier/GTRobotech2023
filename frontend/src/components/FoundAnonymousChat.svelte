<script lang="ts">
    // Get anaonymous name and photo
    let randomName: string = "Lucious Lion";
  </script>
  
  <div class="chatBubble">
    <p><b>{randomName}</b> has been facing similar struggles, would you like to chat with them?</p>
    <div style="display: flex">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Lion_waiting_in_Namibia.jpg/440px-Lion_waiting_in_Namibia.jpg">
    </div>
    <button class="startChatBtn">
        <p><b>Sure</b></p>
    </button>
    <button style="color: white">
        <p>I want to talk more...</p>
    </button>
  </div>
  
  <style>
    p 
    {
       margin: 10;
       border: none;
       text-align: center;
    }

    img
    {
        display: flex;
        width: 80px;
        height: 80px;
        border-radius: 50%;
        margin: 0 auto;
        object-fit: cover;
        margin-top: 10px;
    }

    button
    {
        background: none;
        border: none;
    }

    .chatBubble
    {
        padding-bottom: 10px;
        display: flex;
        flex-direction: column;
        height: auto;
        width: auto;
        border: none;
        border-radius: 20px;
        background-color: #2c2c2c;
        margin-bottom: 30px;
        justify-content: center;
    }

    .startChatBtn
    {
        margin-top: 10px;
        align-self: center;
        align-items: center;
        background-color: #96e4b6;
        width: 100px;
        height: auto;
        border-radius: 10px;
        opacity: 0.6;
    }

    .startChatBtn p 
    {
        opacity: 1;
        color: #1d422d;
        font-size: 15px;
    }

  </style>
  