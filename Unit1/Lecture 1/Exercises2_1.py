# generate all combinations of N items
import random
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

def yieldAllCombos(items):

    """

    This generator uses base 3 instead of base 2, where each trit (ternary digit) in the number i represents
     whether the corresponding item is in bag1, bag2, or neither. Here are the meanings of the trits:

    0: the item is not in either bag
    1: the item is in bag1 only
    2: the item is in bag2 only

    Note that the range of the outer loop is 3**N instead of 2**N because there are three possible values for each
  trit. The inner loop iterates through the items in the list and extracts the trit for each item using
   integer division and modulus. If the trit is 1, the item is added to bag1; if it's 2, the item is
   added to bag2. Finally, the generator yields a tuple of the two bags.
    :param items:
    :yield: combinations of all items if it is in bag1 or bag2 or neither
    """
    N = len(items)
    # generate all possible combinations for one bag
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            # test trit j-th of integer i in base 3
            trit = (i // 3**j) % 3
            if trit == 1:
                bag1.append(items[j])
            elif trit == 2:
                bag2.append(items[j])
        yield (bag1, bag2)

class Item ( object ):
    def __init__(self,n,v,w):
        self.name = n
        self.value = float ( v )
        self.weight = float ( w )

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        return '<' + self.name + ', ' + str ( self.value ) + ', ' \
                   + str ( self.weight ) + '>'

def buildItems():
    return [ Item ( n,v,w ) for n,v,w in (('clock',175,10),
                                              ('painting',90,9),
                                              ('radio',20,4),
                                              ('vase',50,2),
                                              ('book',10,1),
                                              ('computer',200,20)) ]

def buildRandomItems(n):
    return [ Item ( str ( i ),10 * random.randint ( 1,10 ),random.randint ( 1,10 ) )
                 for i in range ( n ) ]



