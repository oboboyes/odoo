L = [
    ['Apple', 'Orange'],
    [],
    []
]
print(L[0][1])

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])

height = 1.75
weight = 80.5
BMI = weight / (height ** 2)
if BMI < 18.5:
    print("过轻")
elif 18.5 <= BMI < 25:
    print("正常")
elif 28 > BMI >= 25:
    print("过重")

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

x = list(range(10))

for x in list(range(10)):
    sum = sum + x
print(sum)

L = ['Bart', 'Lisa', 'Adam']
print("Hello, " + L[0] + "!")
print("Hello, " + L[1] + "!")
print("Hello, " + L[2] + "!")


def bobo22(X, Y):
    qq = X * Y
    return qq


bobo22(5, 6)