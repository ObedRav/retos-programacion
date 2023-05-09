#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
 * Función que realiza el mapeo de una letra a su equivalente en el lenguaje leet.
 * @letter: la letra a mapear.
 * Retorna el equivalente leet de la letra.
 */
char* fleetDictionary(char letter) {
    switch(letter) {
        case 'a': return "4";
        case 'b': return "I3";
        case 'c': return "[";
        case 'd': return ")";
        case 'e': return "3";
        case 'f': return "|=";
        case 'g': return "&";
        case 'h': return "#";
        case 'i': return "1";
        case 'j': return ",_|";
        case 'k': return ">|";
        case 'l': return "1";
        case 'm': return "/\\/\\";
        case 'n': return "^/";
        case 'o': return "0";
        case 'p': return "|*";
        case 'q': return "(_,)";
        case 'r': return "I2";
        case 's': return "5";
        case 't': return "7";
        case 'u': return "(_)";
        case 'v': return "\\/";
        case 'w': return "\\/\\/";
        case 'x': return "><";
        case 'y': return "j";
        case 'z': return "2";
        case '1': return "L";
        case '2': return "R";
        case '3': return "E";
        case '4': return "A";
        case '5': return "S";
        case '6': return "b";
        case '7': return "T";
        case '8': return "B";
        case '9': return "g";
        case '0': return "o";
        default: return "";
    }
}

/*
 * Función que realiza la traducción de un texto al lenguaje leet.
 * @text: texto a traducir
 * Retorna el texto traducido al lenguaje leet.
 * Nota: La memoria asignada para el resultado debe ser liberada por el llamador.
 */
char* leetTranslator(const char* text) {
    int textLength = strlen(text);
    char* leet = malloc((textLength + 1) * sizeof(char));
    int i;

    for (i = 0; text[i] != '\0'; i++) {
        char* result = fleetDictionary(text[i]);

        if (strcmp(result, "") == 0) strncat(leet, &text[i], 1);
        else strcat(leet, result);
    }

    return leet;
}

int main() {
    const char* text = "I'm good and you?";

    char* leet = leetTranslator(text);
    printf("%s\n", leet);
    free(leet);
    return 0;
}

