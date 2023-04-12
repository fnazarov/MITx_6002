class Food(object):
    def __init__(self,n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):

        return self.name + ': Value: ' + str(self.value)\
                + ', Calories: ' + str(self.calories)

def buildMenu(name,value,calories):
    menu = []
    for n in range(len(value)):
        menu.append(Food(name[n], value[n], calories[n]))
    return menu

def greedy(items, maxCost, keyFuntion):
    """Assumes items a list, maxCost >= 0,
    keyFunction maps elements of items to numbers"""
    itemsCopy = sorted(items, key = keyFuntion, reverse= True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost() <= maxCost):
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue, totalCost)

def testGreedy(items, constraints, keyFuntion):
    taken, val, total_cost = greedy(items, constraints, keyFuntion)

    for item in taken:
        print ('  ', item)
    print ( 'Total Value of items taken = ',val )
    print('Total Calories used: ', total_cost)


def testGreedies(foods,maxUnits):

    print ('Use greedy by VALUE allocate: ', maxUnits, ' calories')
    testGreedy(foods, maxUnits, Food.getValue )


    print('\nUse greedy by COST to allocate:', maxUnits, 'calories')
    testGreedy(foods,maxUnits, lambda x:1/Food.getCost(x))

    print('\nUse greedy by DENSITY to allocate:', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)

names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)

def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total weight of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if toConsider == [] or avail ==[]:
        result = (0, [])
    elif toConsider[0].getCost() > avail:
        #Explore the right branche only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()

        #Explore right branch

        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)

        #Choose better branch
        if withVal> withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def testMaxVal(foods, maxUnits, printItems = True):

    print("Use SEARCH TREE to allocate: ", maxUnits, ' calories')

    val, taken = maxVal(foods, maxUnits)

    print('Total VALUE of items taken = ', val)
    if printItems:
        for item in taken:
            print( '  ', item)
def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxCost)))
    return items
import random
for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45):
    print('Try a menu with', numItems, 'items')
    items = buildLargeMenu(numItems, 90, 250)
    testMaxVal(items, 750, False)


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib ( n - 1 ) + fib ( n - 2 )


# for i in range(121):
#    print('fib(' + str(i) + ') =', fib(i))


def fastFib(n,memo={}):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[ n ]
    except KeyError:
        result = fastFib ( n - 1,memo ) + fastFib ( n - 2,memo )
        memo[ n ] = result
        return result


for i in range ( 121 ):
    print ( 'fib(' + str ( i ) + ') =',fastFib ( i ) )


def genFib():
    fib1 = 1  # fib(n-1)
    fib2 = 0  # fib(n-2)

    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fib1 + fib2
        yield next
        fib2 = fib1
        fib1 = next


# generate all combinations of N items
def powerSet(items):
    N = len ( items )
    # enumerate the 2**N possible combinations
    for i in range ( 2 ** N ):
        combo = [ ]
        for j in range ( N ):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append ( items[ j ] )
        yield combo