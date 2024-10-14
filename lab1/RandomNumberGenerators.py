import numpy as np
from typing import Tuple


class RandomNumberGenerators:
    def __init__(self, sizeOfArray : int, is_standardMethod = True, mod = 2**31 - 1, param1 = 16807):
        self.sizeOfArray = sizeOfArray
        self.is_standardMethod = is_standardMethod
        self.mod = mod
        self.param1 = param1
    

    def generateArray(self):
        if self.is_standardMethod:
            rng = np.random.default_rng()
            array = rng.random(self.sizeOfArray)
            return array
        
        seed, param2 = self.__generate_parameters()
        array = self.__inverseCongruentialGenerator(seed, param2)
        return array

        
    def __generate_parameters(self):
        param2 = np.random.randint(0, self.mod)
        seed = np.random.randint(1, self.mod)

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        while gcd(seed, self.mod) != 1:
            seed = np.random.randint(1, self.mod)
        
        while gcd(param2, self.mod) != 1:
            param2 = np.random.randint(0, self.mod)
        
        return seed, param2
    
    def __gcdExtended(self, param1, param2):
        if param1 == 0:
            return param2, 0, 1
        
        gcd, x1, y1 = self.__gcdExtended(param2 % param1, param1)
        x = y1 - (param2 // param1) * x1
        y = x1
        return gcd, x, y
    
    def __modInverse(self, param1, mod):
        gcd, x, y = self.__gcdExtended(param1, mod)
        if gcd != 1:
            raise ValueError(f'Обратного элемента для {param1} по модулю {mod} не существует')
        return float(x) % mod
    
    def __inverseCongruentialGenerator(self, seed : int, param2 : int):
        sequence = np.zeros(self.sizeOfArray)
        x = seed

        for i in range(self.sizeOfArray):
            if x == 0:
                x = 1
            
            inv_x = self.__modInverse(x, self.mod)
            x = (self.param1 * inv_x + param2) % self.mod
            sequence[i] = float(x) / self.mod
        
        return sequence
