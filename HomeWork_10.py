class MinStat:
    def __init__(self):
        self.v = []
 
    def add_number(self, n):
        self.v.append(n)
 
    def result(self):
        if self.v == []:
            return None
        else:
            return min(self.v)
 
 
class MaxStat:
    def __init__(self):
        self.v = []
 
    def add_number(self, n):
        self.v.append(n)
 
    def result(self):
        if self.v == []:
            return None
        else:
            return max(self.v)
 
 
class AverageStat:
    def __init__(self):
        self.v = []
 
    def add_number(self, n):
        self.v.append(n)
 
    def result(self):
        if self.v == []:
            return None
        else:
            n = len(self.v)
            s = sum(self.v)
            return s / n



# Пример 1:
from solution import Table
 
tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()

# Пример 2:
from solution import Table
 
tab = Table(2, 2)
 
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()
 
tab.set_value(0, 0, 10)
tab.set_value(0, 1, 20)
tab.set_value(1, 0, 30)
tab.set_value(1, 1, 40)
 
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()
 
for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()

# Пример 3:

from solution import Table
 
tab = Table(1, 1)
 
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()
 
tab.set_value(0, 0, 1000)
 
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()
 
for i in range(-1, tab.n_rows() + 1):
    for j in range(-1, tab.n_cols() + 1):
        print(tab.get_value(i, j), end=' ')
    print()
print()