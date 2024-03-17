favourites = []
numFavourites = 0
for num in range(10000, 99999):
    placeholder = 0
    numStr = str(num)
    digits = []
    isFavourite = True
    for i in numStr:
        digits.append(i)
        if (int(digits[placeholder])) % 2 != 0 and isFavourite == True:
            isFavourite = True
        else:
            isFavourite = False
        placeholder = placeholder + 1

    myset = set(digits)
    if len(digits) == len(myset) and isFavourite == True:
        isFavourite = True
    else:
        isFavourite = False
    if int(digits[1]) > int(digits[0]) and int(digits[1]) > int(digits[2]) and int(digits[3]) > int(digits[4]) and int(digits[3]) > int(digits[2]) and isFavourite == True:
        isFavourite = True
    else:
        isFavourite = False
    if isFavourite == True:
        favourites.append(num)
        numFavourites += 1 
print(favourites)
print("Adrian has " + str(numFavourites) + " favourite numbers")
