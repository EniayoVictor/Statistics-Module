import statistics 
import math

numbers = []

def meanFunction():
    global roundedMean
    global mean
    numbersSum = sum(numbers)
    numbersCount = len(numbers)
    mean = numbersSum/numbersCount
    if type(mean) == float:
        mean = "{:.2f}".format(mean)
        print(f"""
    The sum of data input = {numbersSum}
    The count of data input = {numbersCount}
    The mean of data input = {mean}""")
    else:
        print(f"""
    The sum of data input = {numbersSum}
    The count of data input = {numbersCount}
    The mean of data input = {mean}""")
    
def modeFunction():
    global mode
    for number in numbers:
        numberDuplicates = []
        if number not in numberDuplicates:
            numberDuplicates.append(number)
        for numberCheck in numberDuplicates:
            digitCount = numbers.count(numberCheck)
            print(digitCount)
            
def medianFunction():
    global median

    numbersSort = sorted(numbers)
    numbersCount = len(numbers)
    print(numbersSort)
    print(numbersCount)
    medianIndex = (numbersCount/2) 
    if medianIndex % 2 == 0:
        median = (int(numbers[int(medianIndex)]) + int(numbers[int(medianIndex)-1]))/2
    else:
        medianFinalIndex = math.floor(medianIndex)
        median = numbersSort[medianFinalIndex]
    print(median)

def meanDeviationFunction():
    numbersSum = sum(numbers)
    numbersCount = len(numbers)
    mean = numbersSum/numbersCount
    absoluteMeanList = []
    for number in numbers:
        absoluteMean = number - mean
        absoluteMeanList.append(abs(absoluteMean))
    meanDeviation = (sum(absoluteMeanList))/numbersCount
    print(f"Mean Deviation: {meanDeviation}")

def statisticsFunction():
    numberInput = input("""Enter a number
    >>> """)
    numbers.append(int(numberInput))
    moreNumbersInput = input("Do you want to add another number? y/n ")
    if moreNumbersInput == "y":
        statisticsFunction()
    elif moreNumbersInput == "n":
        actionInput = input("""What function would you like to perform?
        1. Calculate Mean
        2. Calculate Mode
        3. Calculate Median
        4. Calculate Mean Deviation
        5. Perform all Functions
        Your Selection: """)
        if actionInput == "1":
            meanFunction()
        elif actionInput == "2":
            modeFunction()
        elif actionInput == "3":
            medianFunction()
        elif actionInput == "4":
            meanDeviationFunction()
        elif actionInput == "5":
            meanFunction()
            modeFunction()
            medianFunction()
            print(f"Mean = {mean}")            
            print(f"Mode = {mode}")
            print(f"Median = {median}")

statisticsFunction()