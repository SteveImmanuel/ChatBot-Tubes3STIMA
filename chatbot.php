<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/style.css">
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

    <div class="confPanel">
        Confidence Level:
        <div id="bar-conf" class="confBar">
            <div id="lvl-conf" class="confLvl">100%</div>
        </div>
    </div>
    
    
    <div class="mainInput">
        <form id="chatForm" autocomplete="off" action="chatbot.php" method="get">
            <div class="form-group center-block d-flex">
                <input class="form-control" rows="1" id="name" name="chat" placeholder="Say something...">
                <button id="sendButton" class="myButton" type="submit" onclick="move(80)">Send</button>
            </div>
        </form>
    </div>
    <div id="div3" style="width:80px;height:80px;display:none;background-color:blue;"></div>
    <button id="sendButton" class="myButton" onclick="move(25)">25</button>
    <button id="sendButton" class="myButton" onclick="move(50)">50</button>
    <button id="sendButton" class="myButton" onclick="move(75)">75</button>
    <button id="sendButton" class="myButton" onclick="move(100)">100</button>
</body>
</html>
