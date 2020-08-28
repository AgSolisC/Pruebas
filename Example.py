
def rango ():
    numbers = []
    for num in range (5):
        if num%15 == 0:
            result = "FIZZBUZZ"
        elif num%5 == 0:
            result = "BUZZ"
        elif num%3 == 0:
            result = "FIZZ"
        else:
            result = num
        numbers.append(result)
    print (numbers)
    return numbers