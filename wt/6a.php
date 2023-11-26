<html>
<body>
<?php
$con = mysql_connect("localhost","root","") or die(mysql_error());
mysql_select_db ("test") or die(mysql_error());
$sql="insert into books (title, author, publisher) values ('$_POST[title]', r]', 
'$_POST[publisher]')";
if (!mysql_query($sql,$con))
{
die('Error: ' . mysql_error());
}
echo "1 record added";
mysql_close($con);
?>
<form action="bookresult.php" method="post">
Title: <input type="text" name="title" />
<input type="submit" />
</form>
</body></html>
