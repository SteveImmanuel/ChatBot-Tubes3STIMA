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
    <script>
    $(document).ready(function(){
        $("sendButton").click(function(){
            $("#usrInput").show();
        });
    });
</script>

</head>
<body>
    <div class="jumbotron text-center" style="margin-bottom:0">
        <h1>Chatbot</h1>
        <p>test avatar</p> 
    </div>
    <div id="usrInput" class="userInput" >
        <?php
            echo ($_GET["name"]);
        ?>
    </div>
    <div class="mainInput">
        <label >Say something:</label>
        <form autocomplete="off" action="chatbot.php" method="get">
        <div class="form-group center-block d-flex">
            <input class="form-control" rows="1" id="name" name="name" placeholder="Hi...">
            <button id="sendButton" class="myButton" type="submit">Send</button>
        </div>
    </form>
    </div>


</body>
</html>
