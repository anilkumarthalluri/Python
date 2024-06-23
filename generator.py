def TopTen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

nums = TopTen()
print(nums.__next__())
print(nums.__next__())

print(next(nums))

for i in nums:
    print(i)