import random as rnd

# csv creator
#

dict = {
    "random3Digit": "int",
    "randomBetweenrange": "float",
    "String random from set": "string"
}


def lohi(noOfDigits):
    lo = 10 ** (noOfDigits - 1)
    hi = 10 ** (noOfDigits) - 1
    print((lo, hi))
    return (lo, hi)


rows = 35
noOfDigits = 10
(lo, hi) = lohi(noOfDigits)
floatRange = (2.5, 3.5)
roundPrecision = 3
stringSet = ["MP", "UP", "MAH", "JK"]

for i in range(35):
    print(rnd.randint(lo, hi), round(rnd.uniform(floatRange[0], floatRange[1]), roundPrecision),
          rnd.choice(stringSet))
