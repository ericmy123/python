x = range(100)
countOnes = 0
for i in x:
    tempString = str(i)
    amountOfOnes = tempString.count('1')
    countOnes = countOnes + amountOfOnes
print(countOnes)