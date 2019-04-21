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
    <script src="js/jquery.min.js"></script>
    <script src="js/effect.js"></script>
</head>
<body>    
    <div class="container-fluid mainContent">    
        <header class="headerPage">
            <p style='font-size:30px;margin-bottom:0px;'>VSAZ-BOT</p>
            <p>Chatbot sederhana menggunakan algoritma KMP, BM, dan Regex
        </header>
        <div class="row" >
            <div class="col-md-6">
                <div id="avatar-screen" class="container-fluid avatarScreen">
                    <video id="avatar-video1" class="videoAvatar" autoplay muted>
                        <source id="video-src" src="assets/talk_avatar.mp4" type="video/mp4">
                    </video>
                    <video id="avatar-video2" class="hidden" preload="auto">
                        <source id="video-src" src="assets/idle_avatar.mp4" type="video/mp4">
                    </video>
                </div>
            </div>
            <div class="col-md-6" >
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
                    <br>
                    <div id="answer-text" class="ansText">
                        <?php 
                            if(!empty($chat)){
                                exec("python controller.py ".$chat,$result);
                                if(count($result)==1){
                                    echo("Coba tanya yang lain");
                                }else if(count($result)==2){
                                    echo($result[0]);
                                }else if(count($result)==3){
                                    echo("Mungkin maksud anda:<br>");
                                    echo($result[0]);
                                    echo("<br>");
                                    echo($result[1]);
                                }else if(count($result)==4){
                                    echo("Mungkin maksud anda:<br>");
                                    echo($result[0]);
                                    echo("<br>");
                                    echo($result[1]);
                                    echo("<br>");
                                    echo($result[2]);
                                }
                                $percentage=$result[count($result)-1];
                            }
                        ?>                    
                    </div>
                </div>
            
                <div class="confPanel">
                    Level Keyakinan:
                    <div id="bar-conf" class="confBar">
                        <?php
                            if($percentage!="regex"){
                                $percentage=round($percentage);
                                echo ("<div id='lvl-conf' class='confLvl' style='width:0%';>0%</div>");
                            }else{
                                echo ("<div id='lvl-conf' class='confLvl' style='width:100%;background-color:red';>Persentase tidak dapat ditentukan</div>");
                            }
                        ?>
                        <script>
                            var perc="<?php echo($percentage); ?>";
                            move(perc);
                        </script>
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

    <footer class="footerPage">
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
