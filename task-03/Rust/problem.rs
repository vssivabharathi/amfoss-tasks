use std::io;

fn is_prime(n: u32) -> bool {
    if n < 2 {
        return false;
    }
    let max_divisor = (n as f64).sqrt() as u32;
    for i in 2..=max_divisor {
        if n % i == 0 {
            return false;
        }
    }
    true
}

fn print_primes_less_than_n(n: u32) {
    for i in 2..n {
        if is_prime(i) {
            println!("{}", i);
        }
    }
}

fn main() {
    println!("Enter a number:");
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let input: u32 = input.trim().parse().expect("Please enter a valid number");
    
    print_primes_less_than_n(input);
}
