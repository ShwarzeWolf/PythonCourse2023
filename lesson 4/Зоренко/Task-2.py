numbers = list(map(int, input().split()))
for purpose in numbers:
    if numbers.count(purpose) == 1:
        print(purpose)
        break
