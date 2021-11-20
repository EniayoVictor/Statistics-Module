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

    mode = statistics.mode(numbers)
    print(mode)

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
        4. Print Numbers List
        5. Perform all Functions
        Your Selection: """)
        if actionInput == "1":
            meanFunction()
        elif actionInput == "2":
            modeFunction()
        elif actionInput == "3":
            medianFunction()
        elif actionInput == "4":
            print(numbers)
        elif actionInput == "5":
            meanFunction()
            modeFunction()
            medianFunction()
            print(f"Mean = {mean}")            
            print(f"Mode = {mode}")
            print(f"Median = {median}")

statisticsFunction()