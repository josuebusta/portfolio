#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define CHARS "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

int main(int argc, char *argv[]) {
    if (argc != 2) {
        exit(1);
    }
    int keylength = atoi(argv[1]);

    srand(time(NULL));

    for (int i = 0; i < keylength; i++){
        putchar(CHARS[rand() % 27]);
    }

    putchar('\n');
    return 0;
}