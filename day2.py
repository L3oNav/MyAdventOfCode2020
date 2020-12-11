with open("day2.txt", "r") as f:
    lines = f.readlines()

password = [x.split("\n")[0] for x in lines]
#print(password)
valid_2 = 0
valid_1 = 0
for lin in password:
    key, value = lin.split(": ")
    letter = key.split(" ")[1]
    num1, num2 = list(map(int ,key.split(" ")[0].split("-")))

    if num1 <= value.count(letter) <= num2:
        valid_1 += 1

    num1, num2 = num1-1, num2-1

    c = 0
    if value[int(num1)] == letter: c += 1
    if value[int(num2)] == letter: c += 1
    if c == 1:
        valid_2 +=1
print(f"Solution 1:{valid_1}\nSolution 2:{valid_2}")
