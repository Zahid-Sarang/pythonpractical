print "Enter a number:";
$n=<STDIN>;
$t=$n;
$f=1;
if($n%2==0)
{
for($i=0;$i<$t;$i++)
{
$f=$f*$n;
$n=$n-1;
}
print "Factorial is $f\n";
}
else
{
print "no. is odd"
}