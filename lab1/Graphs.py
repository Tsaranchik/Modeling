import numpy as np
import matplotlib.pyplot as plt
from importlib import reload
plt = reload(plt)



class Graphs:
    def __init__(self, frequencies = np.zeros(shape=10), arraySize = 100, intervals = 10, means = np.zeros(shape=10)):
        self.frequencies = frequencies
        self.means = means
        self.intervals = intervals
        self.arraySize = arraySize
    
    def createHistogramOfFrequencies(self):
        interval_edges = np.linspace(0, 1, self.intervals + 1)
        frequenciesPercent = self.frequencies / self.arraySize * 100
        theoreticalFrequency = 100 / self.intervals

        plt.bar(interval_edges[:-1], frequenciesPercent, width=1.0/self.intervals, edgecolor='black', align='edge')
        plt.axhline(y = theoreticalFrequency, color='red', linestyle='--', label=f'Теоретическое распределение ({theoreticalFrequency:.2f}%)')

        plt.title=(f'N = {self.arraySize}')
        plt.xlabel('Интервалы')
        plt.ylabel('Частота')
        plt.grid(True)
        plt.legend()
        plt.show()
    

    def createLinePlot(self, is_diffLength=True):
        theoreticalMean = 0.5
        standardError = 1 / np.sqrt(12)
        meanDiff = np.abs(theoreticalMean - self.means)

        plt.plot(np.arange(1, 11), meanDiff, marker='o', color='blue' if is_diffLength == True else 'yellow', alpha=0.7, label='|M - M_i|', linestyle='-')
        plt.axhline(y=standardError, color='green', linestyle='--', label='Теоретическая ошибка')

        plt.title='Зависимость разности |M - M_i| от номера последовательности i' if is_diffLength == True else 'Зависимость разности |M - M_i| от номера последовательности с переменной длиной i'
        
        if is_diffLength == True: plt.xlabel('Номер последовательности i') 
        else: plt.xlabel('Номер последовательности i (переменая длина)')

        plt.ylabel('|M - M_i|')
        plt.grid(True)
        plt.legend()
        plt.show()
        