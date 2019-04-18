<!DOCTYPE html>
<html lang="en">
<head>
    <title>ChatBot TUBES 3 STIMA</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/style.css">
    <?php include "handler.php" ?>
    <title>Document</title>
    <script src="jquery.min.js"></script>
    <script src="effect.js"></script>
    <script src="//code.responsivevoice.org/responsivevoice.js?key=FfhGa0xE"></script>
</head>
<body>    
    <div class="container-fluid main-content">    
        <header class="header-page">
            Ini chatbot kita belum punya nama
        </header>
        <div class="row">
            <div class="col-md-6 videoAvatar">
                <div id="avatar-screen" class="container-fluid" style="text-align:center;margin-left:0px;margin-right:0px;">
                    <video id="avatar-video1" class="videoAvatar" autoplay>
                        <source id="video-src" src="assets/talk_avatar.mp4" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                    <video id="avatar-video2" class="videoAvatar hidden">
                        <source id="video-src" src="assets/idle_avatar.mp4" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                </div>
            </div>
            <div class="col-md-6">
                <div id="main-screen" class=" container-fluid mainScreen">
                    <div id="chat-text" class="chatText">
                        <?php 
                            $chat=$_GET["chat"];
                            if(empty($chat)){
                                echo("Halo, selamat datang..");
                            } else {
                                echo($chat);
                            }
                        ?>                    
                    </div>
                </div>
            
                <div class="confPanel">
                    Level Keyakinan:
                    <div id="bar-conf" class="confBar">
                        <?php
                            $percentage = getPercentage($_GET["percentage"]);
                            echo ("<div id='lvl-conf' class='confLvl' style='width:".$percentage."';>".$percentage."</div>");
                        ?>
                    </div>
                </div>
            
                <div class="mainInput">
                    <form id="chat-form" autocomplete="off" action="chatbot.php" method="get" onsubmit="return false">
                        <div class="form-group center-block d-flex">
                            <input class="form-control" type="text" rows="1" id="chat-box" name="chat" placeholder="Katakan sesuatu..." autofocus>
                            <input id="sendButton" class="myButton" type="submit" value="Send">
                        </div>
                    </form>
                </div>
            
            </div>
        </div>
    </div>
    <!-- <button onClick=Test()>speak</button>
    <input onclick='responsiveVoice.speak("halo nama saya ares");' type='button' value='🔊 Play' />
-->

    <footer class="footer-page">
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-4">
                    Steve Andreas Immanuel
                </div>
                <div class="col-md-4">
                    Vinsen Marselino Andreas
                </div>
                <div class="col-md-4">
                    Azhar Abdurrasyid
                </div>
            </div>
            <div>
                2019 Tubes 3 Strategi Algoritma
            </div>
        </div>
    </footer>
</body>

</html>
