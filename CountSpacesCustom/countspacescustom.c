#include<stdio.h>
#include<stdlib.h>
/* 	This program is similar to countspaces, but this time,
	the user gets to make the file "count.txt" and type
	whatever he wants. The program will then write to the file
	and count the number of spaces in it.
*/
int main() {
    char input;
    FILE *textfile = fopen("count.txt", "w"); // Open/make file for writing
    printf("Input:");
    scanf("%[^\n]", &input); // Will read into every input up to pressing enter
    fprintf(textfile, "%s", &input); // Write what the user wrote to 
    fclose(textfile);
    fopen("count.txt", "r"); // Reopen file for reading
    
    int c = 32; // Space character
    int i = 0; // Space counter

    while((c=fgetc(textfile))){
        if(c == EOF) break; // End loop when end of file reached
        if(c == 32) i++; // For every space, increment counter
    }

    if (i > 0){
        printf("Number of spaces: %d \n", i); // Print number of spaces found
    }
    else{
        printf("No spaces found"); // Print if no spaces found
    }
    fclose(textfile); // Close file
    return 0;
}