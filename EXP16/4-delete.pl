#!/usr/bin/perl
use strict;
use warnings;
my $file_to_remove='file1.txt';
my $num_removed = unlink $file_to_remove;
print "$num_removed file were removed\n";
