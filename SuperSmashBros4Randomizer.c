#include <stdio.h>
#include <stdlib.h>
/*
This is an 8-player character randomizer for the video game Super Smash Bros. for Wii U (Smash 4)
before I realized that there is already a "Random" option in the selection screen. Oh well.
*/
int main()
{
char ch_arr[54][17] = {
                         "Mario",
                         "Luigi",
                         "Peach",
                         "Boswer",
                         "Dr. Mario",
                         "Yoshi",
                         "DK",
                         "Diddy Kong",
                         "Link",
                         "Zelda",
                         "Shiek",
                         "Ganon",
                         "Toon Link",
                         "Samus",
                         "Zero Suit Samus",
                         "Kirby",
                         "Meta Knight",
                         "King Dedede",
                         "Fox",
                         "Falco",
                         "Pikachu",
                         "Jigglypuff",
                         "Mewtwo",
                         "Charizard",
                         "Lucario",
                         "Captain Falcon",
                         "Ness",
                         "Lucas",
                         "Marth",
                         "Roy",
                         "Ike",
                         "Game And Watch",
                         "Pit",
                         "Wario",
                         "Olimar",
                         "Rob",
                         "Sonic",
                         "Rosalina",
                         "Bowser Jr",
                         "Greninja",
                         "Robin",
                         "Lucina",
                         "Corrin",
                         "Palutena",
                         "Dark Pit",
                         "Villager",
                         "Little Mac",
                         "Wii Fit Trainer",
                         "Shulk",
                         "Duck Hunt",
                         "Mega Man",
                         "Pac Man",
                         "Ryu",
                         "Cloud",
                         "Any Mii"
                     };
                    
char * random;
int i;
srand(time(0));
for (i = 0; i < 8; i++){
    random = ch_arr[rand() % 54];
    printf("%s\n", random);
}
return 0;
}