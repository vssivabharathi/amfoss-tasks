package main

import "fmt"

func is_prime(n int) bool {
	if n < 2 {
		return false
	}
	for i := 2; i < n; i++ {
		if n%i == 0 {
			return false
		}
	}

	return true
}

func main() {
	var N int
	fmt.Println("Enter a number")
	fmt.Scanln(&N)

	for i := 2; i <= N; i++ {
		if is_prime(i) {
			fmt.Print(i, " ")
		}
	} 
	fmt.Println("\n")
}