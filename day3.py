import string

with open("inputs/day3") as f:
    lines = set(f.readlines())

partOne = 0
partTwo = 0
letterScore = dict()
for index, letter in enumerate(string.ascii_letters):
    letterScore[letter] = index + 1

for i in lines:
    pocket1, pocket2 = set(i[:len(i) // 2]), set(i[len(i) // 2:])
    for n in pocket1:
        if n in pocket2:
            partOne += letterScore[n]

with open("inputs/day3") as f:
    while True:
        s1 = f.readline().strip()
        if s1 == '':
            break
        s2 = f.readline().strip()
        s3 = f.readline().strip()
        final = list(set(s1) & set(s2) & set(s3))
        for j in final:
            partTwo += letterScore[j]

print(partOne)
print(partTwo)
