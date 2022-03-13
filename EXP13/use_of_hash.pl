#!/usr/bin/perl
%data=('John Paul'=>45,'Lisa'=>30,'Kumar'=>40);
print"$data{'John Paul'}\n";
print"$data{'Lisa'}\n";
print"$data{'Kumar'}\n";
@array=@data{-johnPaul,-Lisa};
print "Array:@array\n";
#getting keys
@names=keys%data;
print"$names[0]\n";
print"$names[1]\n";
print"$names[2]\n";
#getting values
@ages = values%data;
print "$ages[0]\n";
print "$ages[1]\n";
print "$ages[2]\n";
#checking for existence of data
if(exists($data{'Lisa'})){
print "Lisa is $data{'Lisa'}years old\n";
}else{
print "I don't know age of Lisa\n";
}
#getting hash size
@keys = keys%data;
$size=@keys;
print "1-Hash size: is $size\n";
@values=values%data;
$size=@values;
print"2-Hash size: is $size\n";
#add and remove elements form hash
@keys=keys%data;
$size=@keys;
print "1-Hash size: is $size\n";
#adding an element to the hash;
$data{'Ali'}=55;
@keys=keys%data;
$size=@keys;
print "2-Hash size: is $size\n";
#delete the same element from the hash;
delete $data{'ali'};
@keys=keys%data;
$size=@keys;
print "3-Hash size: is $size\n";