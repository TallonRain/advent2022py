with open("inputs/day1") as f:
    lines = f.readlines()

maxCal = 0
elf = []
totalElf = 0
topElfTotal = 0
topElf = []
for i in lines:
    if i == "\n":
        for n in elf:
            totalElf += n
        if totalElf > maxCal:
            maxCal = totalElf
        elf = []
        topElf.append(int(totalElf))
        totalElf = 0
    else:
        elf.append(int(i))


topElf.sort()
topElf.reverse()
topElfTotal += topElf[0]
topElfTotal += topElf[1]
topElfTotal += topElf[2]

print(maxCal)
print(topElfTotal)
