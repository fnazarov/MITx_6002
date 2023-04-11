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

testGreedies(foods, 750)