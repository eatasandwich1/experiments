#include<stdio.h>
#include<stdlib.h>
// This program counts the amount of spaces in count.txt.
int main() {

    FILE *textfile = fopen("count.txt", "r"); // Open file for reading
    int c = 32; // Space character
    int i = 0; // Space counter

    while((c=fgetc(textfile))){
        if(c == EOF) break; // Stop when we reach the end of file
        if(c == 32) i++; // Count the amount of spaces
    }

    if (i > 0){
        printf("Number of spaces: %d \n", i);
		// If there are any spaces at all
    }
    else{
        printf("No spaces found");
    }
    fclose(textfile); // Close file
    return 0;
}