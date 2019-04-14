// $(document).ready(function(){
//     $("#sendButton").click(
//         function(){
//             $("#div3").fadeIn("slow");
//             $(document).forms["chatForm"].submit();
//         }
        // var elem = document.getElementById("myBar");   
        // var width = 20;
        // var id = setInterval(frame, 10);
        // function frame() {
        //     if (width >= 100) {
        //     clearInterval(id);
        //     } else {
        //     width++; 
        //     elem.style.width = width + '%'; 
        //     elem.innerHTML = width * 1  + '%';
        //     }
        // }
//     );
// });

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