open (FILE, ">> file1.txt") || die "problem opening $file1.txt\n";  
print FILE "This line is added in the file1.txt\n";  
# FILE array of lines is written here  
print FILE @lines1;  
# Another FILE array of lines is written here  
print FILE "A complete new file is created";  
# write a second array of lines to the file  
print FILE @lines2; 