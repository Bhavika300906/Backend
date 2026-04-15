def fibonacci (n):
    a,b=0,1
    for i in range (n):
        yield a
        a,b=b,a+b

# Create a fib generator
fib = fibonacci(10)

#Iterate and print the Fibonacci numbers

print(list(fib))

