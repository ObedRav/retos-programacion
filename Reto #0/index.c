# include <stdio.h>
# include <string.h>


/*
 * Esta funcion se encarga del manejo de fizzbuzz
 * @num: Numero hasta el cual se espera se imprima fizzbuzz el numero debe ser mayor a 1
*/
void fizzbuzz(int num)
{
	for (int i = 1; i <= num; i++)
	{
		char result[10] = "";

		if (i % 3 == 0) strcat(result, "fizz");

		if (i % 5 == 0) strcat(result, "buzz");

		if (strlen(result) > 0) printf("%s\n", result);
		else printf("%d\n", i);
	}
}

/*
 * Funcion principal
 */
int main(void)
{
	fizzbuzz(100);

	return (0);
}
