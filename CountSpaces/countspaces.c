#include<stdio.h>
#include<stdlib.h>
// This program counts the amount of spaces in count.txt.
int main() {

    FILE *textfile = fopen("count.txt", "r");
    int c = 32; // Space character
    int i = 0;

    while((c=fgetc(textfile))){
        if(c == EOF) break;
        if(c == 32) i++;
    }

    if (i > 0){
        printf("Number of spaces: %d \n", i);
    }
    else{
        printf("No spaces found");
    }
    fclose(textfile);
    return 0;
}