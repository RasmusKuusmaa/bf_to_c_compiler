#include <stdio.h>
int main() {
    char memory[30000] = {0};
    char *ptr = memory;

*ptr = getchar();
	putchar(*ptr);
*ptr = getchar();
	putchar(*ptr);

    return 0;
}
