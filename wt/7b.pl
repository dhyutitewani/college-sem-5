#!/usr/bin/perl 
print "content-type:text/html ";
$count_file="/var/www/cgi-bin/ru.txt";
if(open(FILE,'<'.$count_file))
{
$no_accesses=<FILE>;
close(FILE);
if(open(FILE,'>'.$count_file))
{
$no_accesses++;
print FILE $no_accesses;
close(FILE);
print "no. of visitors:",$no_accesses;
}
else
{
print "[can't write to data file]";
}
}
else
{
print "[sorry]";
}
exit(0);