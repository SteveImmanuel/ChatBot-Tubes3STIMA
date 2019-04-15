<?php
function getPercentage($percentage){
    if(empty($percentage)){
        return "0%";
    }else{
        return $percentage."%";
    }
}
?>