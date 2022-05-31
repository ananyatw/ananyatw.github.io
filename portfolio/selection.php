<html>
<head><title>Selection Sort</title></head>
<body>
<?php
$nums = array(1,2,45,62,83);
function selSort ($array) { 
    $count = count($array);
    $min=0;
    for ($x = 0; $x < $count; $x++){
        for ($i = $x+1; $i<=$count;$i++){
            if ($nums[$i] < $nums[$x]){
                $min = $nums[$i];
                $nums[$i] = $nums[$x];
                $nums[$x] = $min;   
            }
        }
    echo $array[$x];
    }
}
selSort($nums);
?>