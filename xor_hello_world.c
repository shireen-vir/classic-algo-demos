#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello World";
    int len = strlen(str);

    // XOR with 0
    printf("XOR with 0:\n");
    for (int i = 0; i < len; i++) {
        char xored = str[i] ^ 0;   // XOR with 0 doesn't change the character
        printf("%c", xored);
    }
    printf("\n");

    // XOR with 1
    printf("XOR with 1:\n");
    for (int i = 0; i < len; i++) {
        char xored = str[i] ^ 1;   // XOR each character with 1
        printf("%c", xored);
    }
    printf("\n");

    return 0;
}