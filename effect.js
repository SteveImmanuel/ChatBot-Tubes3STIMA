$(document).ready(function(){
    $("#chat-text").fadeIn(1000);

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
