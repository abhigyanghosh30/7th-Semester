#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{   
    if(argc<2){
        printf("number of blocks not provided");
        return 1;
    }
    FILE * bFile;
    char blocks[4096];
    bFile = fopen ("test.bin", "wb+");
    long arg = strtol(argv[1], NULL, 10);
    for(long i=1;i<=arg;i++){
        fread(blocks , sizeof(char), sizeof(blocks), bFile);
    }
    fclose(bFile);
    return 0;
}
