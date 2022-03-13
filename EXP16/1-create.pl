my $filename = 'file1.txt';  
open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";  
print $fh "Hello!! We have created this file as an example\n";  
close $fh;  
print "done\n";  