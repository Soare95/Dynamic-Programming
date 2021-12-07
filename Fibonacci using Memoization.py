def fibonacci_recursive(num):  # O(2^n)..
    if num < 2:
        return num
    return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)


def memoization_fibonacci():  # O(n)
    cache = {}

    def memoized(num):
        if num in cache:
            return cache[num]
        else:
            if num < 2:
                return num
            else:
                cache[num] = memoized(num-1) + memoized(num-2)
                return cache[num]
    return memoized


print(fibonacci_recursive(10))
memo = memoization_fibonacci()
print(memo(10))
