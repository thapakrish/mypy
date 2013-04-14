import pylab
import random


def generateHT(trials):
    """
    (int)-> int list
    
    Runs trials number of times and flips coin.

    Returns: A random list of Head and Tail as either 10 or 5
    """

    Head_Tail = []
    for i in range(trials):
        num = random.randint(1,10)
        if num % 2 == 0:
            Head_Tail.append(10)
        else:
            Head_Tail.append(5)
    return Head_Tail                
    

def plotHT():
    trials = 1000
    pylab.figure()
    pylab.hist(generateHT(trials),2)
    pylab.xlabel("HT distribution")
    pylab.ylabel("Number of trials")
    pylab.title("Head and Tail Coins toss")
    pylab.legend(loc = 0)
    pylab.show()
