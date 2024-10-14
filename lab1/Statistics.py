import numpy as np
from RandomNumberGenerators import *


class Statistics:
    def __init__(self, array = np.zeros(shape=100), intervals = 10, is_differentLength = False, is_standardMethod = True):
        self.array = array
        self.intervals = intervals
        self.is_differentLength = is_differentLength
        self.is_standardMethod = is_standardMethod

    
    def calculateAndPrintProperties(self):
        print(f'N = {self.array.size}')
        print(f'Мат ожидание: {self.array.mean()}', end=', ')
        print(f'Дисперсия: {self.array.var()}', end=', ')
        print(f'Стандартное отклонение: {self.array.std()}')
    

    def __calculateFrequency(self):
        frequency = np.zeros(shape=self.intervals)
        intervalSize = 1.0 / self.intervals

        for num in self.array:
            index = int(num / intervalSize)

            if index == self.intervals:
                index = self.intervals - 1
            
            frequency[index] += 1

        return frequency
    

    def printFrequency(self):
        frequencyArray = self.__calculateFrequency()

        for i in range(self.intervals):
            print(f'Интервал {i} {(frequencyArray[i] / self.array.size) * 100}')
        
        print()
        return frequencyArray
    

    def __uniformityCheck(self):
        means = np.zeros(shape=10)

        if self.is_standardMethod:
            rng = np.random.default_rng()

            for i in range(10):
                array = rng.random(1000 + 1000 * (i * int(self.is_differentLength)))
                means[i] = array.mean()
            
            return means
        
        for i in range(10):
            arrLength = 1000 + 1000 * (i * int(self.is_differentLength))
            rng = RandomNumberGenerators(arrLength, is_standardMethod=False)
            array = rng.generateArray()
            means[i] = array.mean()
        
        return means
    
    def printMeansForSequencesOfDiffLength(self):
        means = self.__uniformityCheck()

        print(f"Мат. ожидание для переменных последовательностей: ")

        for i in range(means.size):
            print(f"Последовательность {i + 1} (длина {(i + 1) * 1000}): {means[i]}")
        
    
    def getMeans(self):
        means = self.__uniformityCheck()
        return means
