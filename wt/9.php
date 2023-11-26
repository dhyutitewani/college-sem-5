<?php
$present_time=date(“H:i:s-m/d/y”);
$expiry= 60 * 60 *24 *60 + time();
setcookie("Lastvisit",$present_time, $expiry);
if(isset($_COOKIE[“Lastvisit”]))
{
echo "Cookie has been set";
echo “The current time of the system is”;
echo $present_time;
echo "The Last visited Time and Date";
echo $_COOKIE["Lastvisit"];
}
else
echo ”You’ve got some old cookies!”;
?>