<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/style.css">
    <?php include "handler.php" ?>
    <title>Document</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="effect.js"></script>
</head>
<body>
    <!-- <div class="jumbotron text-center" style="margin-bottom:0">
        <h1>Chatbot</h1>
        <p>test avatar</p> 
    </div> -->
    <!-- <div id="usrInput" class="userInput" >
    </div> -->
    
    <div id="main-screen" class=" container-fluid mainScreen">
        <div id="chat-text" class="chatText"><?php echo($_GET["chat"]); ?></div>
        <!-- <div id="chat-text" class="chatText">test123</div> -->
    </div>
    
    <div class="confPanel">
        Confidence Level:
        <div id="bar-conf" class="confBar">
            <div id="lvl-conf" class="confLvl" style="width:<?php echo(getPercentage($_GET["percentage"]))?>"><?php echo(getPercentage($_GET["percentage"]))?></div>
        </div>
    </div>
    
    <div class="mainInput">
        <form id="chat-form" autocomplete="off" action="chatbot.php" method="get" onsubmit="return false">
            <div class="form-group center-block d-flex">
                <input class="form-control" type="text" rows="1" id="chat-box" name="chat" placeholder="Say something...">
                <input id="sendButton" class="myButton" type="submit" value="Send">
            </div>
        </form>
    </div>
</body>
</html>
