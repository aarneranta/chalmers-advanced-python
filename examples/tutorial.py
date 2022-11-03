print('*** 4.4: break and else in a loop ***')

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


print('*** 4.4: continue in a loop ***')

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)


print('*** 4.7: Fibonacci that prints ***')

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(100)

print("the type of fib is", type(fib))

print("the type of fib(100) is", type(fib(100)))

print("the value of fib(100) is", fib(100))


print('*** 4.7: Fibonacci that returns a list ***')

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print(fib2(100))

print("the type of fib2 is", type(fib2))

print("the type of fib2(100) is", type(fib2(100)))

print("the value of fib2(100) is", fib2(100))


print('*** 4.8: Default arguments ***')

def topmost(xs, number=5):
    return sorted(xs)[:number]

print(topmost([3, 4, 0, 0, 12, 5, 4, 8, 2]))

print(topmost([3, 4, 0, 0, 12, 5, 4, 8, 2], number=3))

print(topmost([3, 4, 0, 0, 12, 5, 4, 8, 2], 3))

print(topmost(xs=[3, 4, 0, 0, 12, 5, 4, 8, 2]))



print('*** 4.8: Arbitrary argument lists ***')

def print_many(*args):
    print('begin')
    for arg in args:
        print(' ', arg)
    print('end')

print_many()
print_many('hello')
print_many(1, 2, 3)

print_many(*range(10))

print('*** 4.8.6: lambda expressions ***')

def mean(x, y):
    return (x+y)/2

print(mean(3, 8))

lmean = lambda x, y: (x+y)/2

print(lmean(3, 8))

mmean = lambda *xs: sum(xs)/len(xs)

print(mmean(3, 8, 10))

nums = list(range(10))
print(sorted(nums))
print(sorted(nums, key=lambda x: -x))





