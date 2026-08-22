#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* convert(char* s, int numRows) {
    int len = strlen(s);
    if (numRows == 1 || numRows >= len) {
        return s;
    }

    // Allocate memory for rows
    char **rows = (char **)malloc(numRows * sizeof(char *));
    int *rowSizes = (int *)calloc(numRows, sizeof(int));

    for (int i = 0; i < numRows; i++) {
        rows[i] = (char *)malloc((len + 1) * sizeof(char));
    }

    int currRow = 0;
    int direction = 1; // 1 = down, -1 = up

    for (int i = 0; i < len; i++) {
        rows[currRow][rowSizes[currRow]++] = s[i];

        if (currRow == 0)
            direction = 1;
        else if (currRow == numRows - 1)
            direction = -1;

        currRow += direction;
    }

    // Combine rows
    char *result = (char *)malloc((len + 1) * sizeof(char));
    int index = 0;

    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < rowSizes[i]; j++) {
            result[index++] = rows[i][j];
        }
        free(rows[i]);
    }

    result[index] = '\0';
    free(rows);
    free(rowSizes);

    return result;
}
