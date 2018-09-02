''' num1 = 1
num2 = 1
num3 = 0
nums = 100
count = 2

print(num1)
print(num2)

while count < nums:
    count += 1
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3)
'''

fib = [1, 1]
i = 0
count = 20
while i <= count:
    fib.append(fib[i]+fib[i+1])
    i += 1

print("Fibonacci numbers: ")
print(fib)
