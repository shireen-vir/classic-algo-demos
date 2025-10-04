#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to perform Caesar Cipher encryption (shift by 3)
char caesarEncrypt(char ch) {
    if (ch >= 'A' && ch <= 'Z') {
        return ((ch - 'A' + 3) % 26) + 'A';
    } else if (ch >= 'a' && ch <= 'z') {
        return ((ch - 'a' + 3) % 26) + 'a';
    } else {
        return ch; // Non-alphabetic characters remain unchanged
    }
}

int main() {
    char srcFile[100], destFile[100];
    FILE *src, *dest;
    char ch, choice;

    printf("Enter Source File Name: ");
    scanf("%s", srcFile);

    // Check if source file exists
    src = fopen(srcFile, "r");
    if (src == NULL) {
        printf("Source file does not exist.\n");
        printf("Creating a new source file: %s\n", srcFile);

        // Create new source file and write user data into it
        src = fopen(srcFile, "w");
        if (src == NULL) {
            perror("Error creating source file");
            exit(1);
        }

        printf("Enter content to write into %s (end with ~ on a new line):\n", srcFile);
        getchar(); // clear leftover newline from scanf
        while ((ch = getchar()) != '~') {
            fputc(ch, src);
        }
        fclose(src);

        // Re-open in read mode for encryption
        src = fopen(srcFile, "r");
        if (src == NULL) {
            perror("Error reopening source file");
            exit(1);
        }
    }

    printf("Enter Destination File Name: ");
    scanf("%s", destFile);

    // Check if destination file already exists
    dest = fopen(destFile, "r");
    if (dest != NULL) {
        fclose(dest);
        printf("Destination file already exists. Overwrite? (y/n): ");
        scanf(" %c", &choice);
        if (choice != 'y' && choice != 'Y') {
            printf("Encryption cancelled. File not overwritten.\n");
            fclose(src);
            exit(0);
        }
    }

    // Open destination file in write mode
    dest = fopen(destFile, "w");
    if (dest == NULL) {
        perror("Error opening destination file");
        fclose(src);
        exit(1);
    }

    // Encrypt and copy content
    while ((ch = fgetc(src)) != EOF) {
        fputc(caesarEncrypt(ch), dest);
    }

    printf("\nFile encrypted successfully!\n");
    printf("Encrypted content saved in: %s\n", destFile);

    fclose(src);
    fclose(dest);
    return 0;
}
