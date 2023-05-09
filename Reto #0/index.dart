void fizzbuzz(int num) {
	for (int i = 0; i <= num; i++) {
		String resultado = "";

		if (i % 3 == 0 ) resultado += "fizz";
		if (i % 5 == 0) resultado += "buzz";

		print(resultado.isNotEmpty ? resultado : i);
	}
}

void main() {
	fizzbuzz(100);
}