#!/usr/bin/perl
print "content-type:text/html ";
print "<html><title>Result of the insert operation </title>";
use CGI ':standard';
use DBI;
$dbh=DBI->connect("DBI:mysql:test","root","");
$fname=param("fname");
$lname=param("lname");
$age=param("age");
$address=param("address");
$pincode=param("pincode");
$qh=$dbh->prepare("insert into stud 
values('$fname','$lname','$age','$address','$pincode')");
$qh->execute();
$qh=$dbh->prepare("select * from stud");
$qh->execute();
print "<table border 
size=1><tr><th>Firstname</th><th>LastName</th><th>Age</th<th>Address</th><th>Pinc
ode</th></tr>";
while ( ($fname,$lname,$age,$address,$pincode)=$qh->fetchrow())
{
     print 
"<tr><td>$fname</td><td>$lname</td><td>$age</td><td>$address</td><td>$pincode</td>
</tr>";
}
print "</table>";
$qh->finish();
$dbh->disconnect();
print"</HTML>";