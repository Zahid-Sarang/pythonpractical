use strict;  
use warnings;  
my $filename = 'file1.txt';  
open(my $fh, '<:encoding(UTF-8)', $filename)  
  or die "Could not open file '$filename' $!";  
my $row = <$fh>;  
print "$row\n";  
print "done\n"; 