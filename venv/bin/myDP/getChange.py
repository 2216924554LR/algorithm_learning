
# low efficiency, use dict to record minChange
def getChangeSolution1(coinValueList, change, knowRes):
    minCoins = change
    if change in coinValueList:
        knowRes[change] = 1
        return 1
    elif change in knowRes:
        return knowRes[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + getChangeSolution1(coinValueList, change - i, knowRes)
            if numCoins < minCoins:
                minCoins = numCoins
                knowRes[change] = minCoins
    return minCoins

def getChangeSolution2(coinValueList, change, minCoins):
    for cents in range(1, change+1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        minCoins[cents] = coinCount
    return minCoins[change]

# get coin list
def getChangeSolution3(coinValueList, change, minCoins):
    for cents in range(0, change + 1):
        coinCount = cents * [1]
        for j in [c for c in coinValueList if c <= cents]:
            if len(minCoins[cents - j]) + 1 < len(coinCount):
                coinCount = minCoins[cents - j] + [j]
                minCoins[cents] = coinCount
            else:
                minCoins[cents] = coinCount
    return minCoins[change]

def getChangeSolution4(coinValueList, change, minCoins, coinsUsed):
    for cents in range(1, change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin -thisCoin

if __name__ == "__main__":
    # print(getChangeSolution1([1, 5, 10, 25], 18, {}))
    # print(getChangeSolution2([1, 5, 10, 25], 18, [0]*64))
    # print(getChangeSolution3([1, 5, 10, 21, 25], 63, {0 : []}))
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coinUsed = [0] * (amnt + 1)
    coinCount = [0] * (amnt + 1)
    print(getChangeSolution4(clist, amnt, coinCount, coinUsed), "coins")
    print("They are")
    printCoins(coinUsed, amnt)
    print(coinUsed)

