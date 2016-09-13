#include <stdio.h>

void secret()
{
    //tells a secret
    printf("I like donuts\n");
    while(1);
}

void main()
{
    char type[32];
    char name[32];

    strcpy(type, "fire type pokemon");

    gets(name);

    //printf("A%200x");
    printf("This is %s a %s.\n", name, type);
}
