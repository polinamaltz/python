from matplotlib.pyplot import plot
from matplotlib import pyplot as plt
import numpy as np


def collatz_sequence(number):
    l = []
    while number > 1:
        l.append(number)
        number = number // 2 if number % 2 == 0 else number * 3 + 1
    l.append(1)
    return l

numbers = range(1, 1000)
seq = []
for number in numbers:
    seq.append(collatz_sequence(number))
max_ = []
for num in seq:
    max_.append(max(num))
nums_for_legend = np.argpartition(max_, -6)[-6:]
for n in nums_for_legend:
    print(n, max_[n])
my_legend = [seq.index(num) if seq.index(num) in nums_for_legend else '_nolegend_' for num in seq]
my_colors = ['b', 'g', 'r', 'c', 'm', 'k']

plt.figure(figsize=(16, 10))
color_ind = 0
for num in seq:
    x = range(seq.index(num)+1,seq.index(num)+len(num)+1)
    if seq.index(num) in nums_for_legend:
        my_color = my_colors[color_ind]
        color_ind += 1
    else:
        my_color = 'y'
    plot(x, num, my_color)
    if seq.index(num) in nums_for_legend:
        plt.text(x[np.argmax(num)], num[np.argmax(num)], f'{seq.index(num)}')
plt.title('Collatz Conjecture')
plt.legend(my_legend)
plt.savefig('collatz_conjecture.pdf')
