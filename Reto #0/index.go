package main

import (
	"fmt"
)

func fizzbuzz(num int) {
	for i := 1; i <= num; i++ {
		result := ""

		if i % 3 == 0 {
			result += "fizz"
		}

		if i % 5 == 0 {
			result += "buzz"
		}

		fmt.Println(func(r string, n int) string {
			if r == "" {
				return fmt.Sprint(n)
			}
			return r
		}(result, i))
	}
}

func main() {
	fizzbuzz(100)
}