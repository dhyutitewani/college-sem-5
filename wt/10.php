<?php
session_start();
if (!isset($_SESSION))
{
$_SESSION["count"] = 1;
echo "<p>Counter initialized</p>\n";
}
else { $_SESSION["count"]++; }
echo "<p>This page has been viewed <b>$_SESSION[count]</b> times.</p>".
"<p>reload this page to increment</p>";
?>