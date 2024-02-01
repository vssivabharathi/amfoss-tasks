defmodule Prime do
  def is_prime(n) when n < 2, do: false
  def is_prime(n) do
    max_divisor = round(:math.sqrt(n))
    Enum.all?(2..max_divisor, fn i ->
      rem(n, i) != 0
    end)
  end

  def print_primes_less_than_n(n) do
    for i <- 2..(n - 1) do
      if is_prime(i) do
        IO.puts("#{i}")
      end
    end
  end
end

IO.puts("Enter a number")
n_str = String.trim(IO.gets(""))
n = String.to_integer(n_str)
Prime.print_primes_less_than_n(n)
