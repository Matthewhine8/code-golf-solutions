#include <stdio.h>

int main(int argc, char* argv[]) {
for(int i=99;i>=1;i--){
if(i>1 && i!=2){
printf("%i bottles of beer on the wall, %i bottles of beer.\nTake one down and pass it around, %i bottles of beer on the wall.\n\n",i,i,i-1);
}
else if(i==2){
printf("%i bottles of beer on the wall, %i bottles of beer.\nTake one down and pass it around, %i bottle of beer on the wall.\n\n",i,i,i-1);
}
else{
printf("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.");
}
}
}
