$(document).ready(function(){
    $("#chat-text").fadeIn(1000);
    
    var video1=document.getElementById("avatar-video1");
    var video2=document.getElementById("avatar-video2");
    video1.addEventListener("ended", changeAvatar, false);
    function changeAvatar() {
        video2.play();
        video2.loop=true;
        video2.setAttribute("class","videoAvatar");
        video1.setAttribute("class","hidden");
    }
    
    $("#sendButton").click(
        function(){
            $("#chat-text").fadeOut(1000);
            var textInput=document.getElementById("chat-box").value;
            move(textInput);
            function move(max) {
                var elem = document.getElementById("lvl-conf");   
                var elemParent=document.getElementById("bar-conf");
                var width = (parseFloat(getComputedStyle(elem).width)/parseFloat(getComputedStyle(elemParent).width))*100;
                width=Math.round(width);
                var id = setInterval(frame, 10);
                function frame() {
                    if (width == max) {
                        clearInterval(id);
                        window.location.href = "chatbot.php?chat=" + textInput+"&percentage="+max;
                    } else if(width<max) {
                        width++; 
                        elem.style.width = width + '%'; 
                        elem.innerHTML = width  + '%';
                    } else if(width>max){
                        width--; 
                        elem.style.width = width + '%'; 
                        elem.innerHTML = width  + '%';   
                    }
                }
            }
        }
        );
});

function Test(){
    var msg = new SpeechSynthesisUtterance('Halo nama saya dicky');
    var voices = window.speechSynthesis.getVoices();
    msg.voice = voices[10];
    msg.voiceURI = "native";
    msg.volume = 1;
    msg.rate = 1;
    msg.pitch = 0.8;
    msg.text = "awdad";
    msg.lang = '-US';
    speechSynthesis.speak(msg);
}
        
