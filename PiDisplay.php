<?php 

$Pi = file_get_contents('http://bertie.io/Pi.txt');
$len = rand(1,20);
$pos = rand(0,strlen($Pi) - $len);

$out = substr($Pi, $pos, $len);

echo "The ";
echo  $len;
echo  " decimals at ";
echo $pos;
echo "to ";
echo $pos+$len;
echo " out of 4194294 ";
echo " are ";
echo $out;

?>
