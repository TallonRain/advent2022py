with open("inputs/day2") as f:
    lines = f.readlines()

# rock = A | X
# paper = B | Y
# scissors = C | Z

letterVal = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
losePair = {'A': 'Z', 'B': 'X', 'C': 'Y'}
winPair = {'A': 'Y', 'B': 'Z', 'C': 'X'}
totalScore = 0
partTwo = 0
for i in lines:
    divided = i.split(' ')
    left = divided[0].strip()
    right = divided[1].strip()
    score = letterVal.get(right)
    tieLeft = letterVal.get(left)

    if tieLeft == score:
        totalScore += 3 + score
    elif (left == 'A' and right == 'Z') or (left == 'B' and right == 'X') or (left == 'C' and right == 'Y'):
        totalScore += 0 + score
    else:
        totalScore += 6 + score

    if right == 'X':  # must lose
        loseValue = letterVal.get(losePair.get(left))
        partTwo += 0 + loseValue
    elif right == 'Y':  # must tie
        partTwo += 3 + tieLeft
    elif right == 'Z':  # must win
        winValue = letterVal.get(winPair.get(left))
        partTwo += 6 + winValue

print(totalScore)
print(partTwo)

# well that's embarrassingly clunky
