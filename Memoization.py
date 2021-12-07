def add_80(num):
    print("Long Time")
    return num + 80


print(add_80(5))
print(add_80(5))


# Memoization 1
cache = {}
def memoization_add_80(num):
    if num in cache:
        return num + 80
    else:
        print("Long time")
        cache[num] = num + 80
        return cache[num]


print(memoization_add_80(6))
print(memoization_add_80(6))


# Memoization 2 - better method because we don't pollute the global scope
def memoization_add_80_2():
    cache = {}

    def memoized(num):
        if num in cache:
            return num + 80
        else:
            print("Long time")
            cache[num] = 80 + num
            return cache[num]
    return memoized


memo = memoization_add_80_2()
print(memo(2))
print(memo(2))


