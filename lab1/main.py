from RandomNumberGenerators import *
from Statistics import *
from Graphs import *
    

def printStats(is_standardMethod=True):
    N = [100, 1000, 10000]
    for n in N:
        rng = RandomNumberGenerators(n, False)
        array = rng.generateArray()

        stats = Statistics(array, is_standardMethod=False)
        stats.calculateAndPrintProperties()
        frequencies = stats.printFrequency()

        graphs = Graphs(frequencies, n)
        graphs.createHistogramOfFrequencies()
    
    stats = Statistics(is_standardMethod=is_standardMethod)
    means = stats.getMeans()

    graphs = Graphs(means=means)
    graphs.createLinePlot()

    stats = Statistics(is_standardMethod=is_standardMethod)
    means = stats.getMeans()

    graphs = Graphs(means=means)
    stats.printMeansForSequencesOfDiffLength()
    graphs.createLinePlot(False)

    print()


def main():
    printStats()
    printStats(False)

        
main()
