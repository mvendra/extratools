
#include <stdio.h>
#include <time.h>

unsigned int good_random(unsigned int index){

    index = (index << 11) ^ index;
    return (((index * index * 13409 + 543112) + 2156423419) & 0x7fffffff);

}

int main(int argc, char *argv[]){

    (void)argc; (void)argv;
    printf("out: [%d]\n", good_random(time(NULL)));

    return 0;

}
