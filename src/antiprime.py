import sys

def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def main(x):
    divisors_x = count_divisors(x)

    for i in range(1, x):
        if count_divisors(i) >= divisors_x:
            return "not anti-prime"
    
    return "antiprime"

if len(sys.argv) != 2:
    print(f"error: {sys.argv[0]} <x>")
else:
    x = int(sys.argv[1])
    
    print(main(x))
