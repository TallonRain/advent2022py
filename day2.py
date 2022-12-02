with open("inputs/day2") as f:
    lines = f.readlines()

# rock = A | X
# paper = B | Y
# scissors = C | Z

letterVal = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
losePair = {'A': 'Z', 'B': 'X', 'C': 'Y'}
winPair = {'A': 'Y', 'B': 'Z', 'C': 'X'}
partOne = 0
partTwo = 0

for i in lines:
    divided = i.split(' ')
    left = divided[0].strip()
    right = divided[1].strip()

    if letterVal[left] == letterVal[right]:  # tie
        partOne += 3 + letterVal[right]
    elif losePair[left] == right:  # lose
        partOne += 0 + letterVal[right]
    else:  # win
        partOne += 6 + letterVal[right]

    if right == 'X':  # must lose
        partTwo += 0 + letterVal[losePair[left]]
    elif right == 'Y':  # must tie
        partTwo += 3 + letterVal[left]
    elif right == 'Z':  # must win
        partTwo += 6 + letterVal[winPair[left]]

print(partOne)
print(partTwo)

# well that's embarrassingly clunky
