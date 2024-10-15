import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom


def read_text_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

        tests = int(lines[0].strip().split(": ")[1])
        probability = float(lines[1].strip().split(": ")[1])
        theoretical_mean = float(lines[2].strip().split(": ")[1])
        means = eval(lines[3].strip().split(': ')[1])
        frequency = eval(lines[4].strip().split(': ')[1])

        return tests, probability, theoretical_mean, means, frequency


def fx_chart(frequency):
    total = sum(frequency)
    relative_frequencies = [freq / total for freq in frequency]

    plt.figure(figsize=(10, 5))
    plt.bar(range(100), relative_frequencies, color='blue', alpha=0.7)
    plt.title('f(x)')
    plt.xlabel('Num of successes')
    plt.ylabel('Probability')
    plt.xticks(range(0, 100, 5))
    plt.grid(axis='y')
    plt.show()


def px_chart(tests, probability):
    k = np.arange(0, tests + 1)
    probabilities = binom.pmf(k, tests, probability)

    plt.figure(figsize=(10, 5))
    plt.bar(k, probabilities, color='green', alpha=0.7)
    plt.title("p(x)")
    plt.xlabel("Num of successes")
    plt.ylabel("Probability")
    plt.xticks(range(0, 101, 5))
    plt.grid(axis='y')
    plt.show()


def Fx_chart(frequency):
    total = sum(frequency)
    relative_frequencies = [freq / total  for freq in frequency]

    cumulative_frequencies = np.cumsum(relative_frequencies)

    plt.figure(figsize=(10, 5))
    plt.plot(range(100), cumulative_frequencies, color='orange', marker='o', alpha=0.7)
    plt.title("F(x)")
    plt.xlabel("Num of successes")
    plt.ylabel("Cumulative probability")
    plt.xticks(range(0, 100, 5))
    plt.grid()
    plt.show()


def uniformity_check_chart(means, theoretical_mean):
    diff = [abs(theoretical_mean - mean) for mean in means]

    plt.figure(figsize=(10, 5))
    plt.plot(diff, color='red', marker='o', alpha=0.7, label = "Absolute difference")
    plt.axhline(y=theoretical_mean, color='gray', linestyle='--', label='Theoretical mean')
    plt.title('Uniformity check')
    plt.xlabel('Num of series')
    plt.ylabel('Absolute difference')
    plt.grid()
    plt.legend()
    plt.show()


def main():
    file_name = 'data.txt'
    tests, probability, theoretical_mean, means, frequency = read_text_file(file_name)

    px_chart(tests, probability)
    fx_chart(frequency)
    Fx_chart(frequency)
    uniformity_check_chart(means, theoretical_mean)
    

main()


