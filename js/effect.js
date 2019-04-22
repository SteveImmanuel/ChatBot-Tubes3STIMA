$(document).ready(function(){
    $("#chat-text").fadeIn(1000);
    $("#answer-text").fadeIn(1000);
    
    var video1=document.getElementById("avatar-video1");
    var video2=document.getElementById("avatar-video2");

    video1.addEventListener("ended", changeAvatar, false);
    function changeAvatar() {
        video2.play();
        video2.muted=true;
        video2.loop=true;
        video2.setAttribute("class","videoAvatar");
        video1.setAttribute("class","hidden");
    }

    var outHeight=document.getElementById("avatar-screen").offsetHeight;
    document.getElementById("main-screen").style.minHeight=outHeight*0.7+"px";
    window.addEventListener("resize",resizePanel,false);
    function resizePanel(){
        outHeight=document.getElementById("avatar-screen").offsetHeight;
        document.getElementById("main-screen").style.minHeight=outHeight*0.7+"px";
    }
    
    $("#sendButton").click(
        function(){
            $("#chat-text").fadeOut(1000);
            $("#answer-text").fadeOut(1000);
            var textInput=document.getElementById("chat-box").value;           
            
            var radios = document.getElementsByName('algo');
            for (var i = 0, length = radios.length; i < length; i++)
            {
                if (radios[i].checked)
                {
                    var algo=radios[i].value;
                    break;
                }
            }
            
            window.location.href = "chatbot.php?chat="+textInput+"&algo="+algo;
        }
        );
});

function move(max) {
    var elem = document.getElementById("lvl-conf");   
    var elemParent=document.getElementById("bar-conf");
    var width = (parseFloat(getComputedStyle(elem).width)/parseFloat(getComputedStyle(elemParent).width))*100;
    width=Math.round(width);
    var id = setInterval(frame, 10);
    function frame() {
        if (width == max) {
            clearInterval(id);
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