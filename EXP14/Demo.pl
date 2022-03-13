#!/usr/bin/perl
use strict;
use warnings;
 
use File::Basename qw(dirname);
use Cwd  qw(abs_path);
use lib dirname(dirname abs_path $0) . '/lib';
 
use Math qw(add);
 
print add(19, 23);