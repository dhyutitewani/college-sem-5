<html>
<body>
<?php
$con = mysql_connect("localhost","root","") or die(mysql_error());
mysql_select_db("test") or die(mysql_error());
$result = mysql_query("select * from books where title= '$_POST[title]'");
if(!$result)
{
echo "There is no record";
}
echo "<table border='1'><tr><th>Title</th><th>Author</th>th>Publisher</th></tr>";
while($row = mysql_fetch_array($result))
{
echo "<tr>";
echo "<td>" . $row['title'] . "</td>";
echo "<td>" . $row['author'] . "</td>";
echo "<td>" . $row['publisher'] . "</td>";
echo "</tr>";
}
echo "</table>";
mysql_close($con);
?> 
</body>
</html>