#include <stdio.h>
#include <stdbool.h>

bool is_prime(int N) {
    if (N < 2) { 
        return false;
    }

    for (int i = 2; i * i <= N; i++) {
        if (N % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int n;
    printf("Enter a number n: ");
    scanf("%d", &n);

    for (int i = 2; i <= n; i++) {
        if (is_prime(i)) {
            printf("%d ", i);
        }
    } 
    printf("\n");
    return 0;
}