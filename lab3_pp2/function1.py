#task1
def replace_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

'''gr = int(input('Enter grams: '))
print(replace_ounces(gr))'''


#task2
def Fahrenheit(f):
    f -= 32
    c = (5 / 9) * f
    return c

'''fr = int(input('Enter temperature: '))
print(Fahrenheit(fr))'''


#task3
def solve(numheads, numlegs):
    x = numheads * 2
    x -= numlegs
    x /= -2
    numheads -= x
    return numheads, x
    
'''nh = int(input('Enter numheads: '))
nl = int(input('Enter numlegs: '))
ch,rb  = solve(nh, nl)
print(f'chickens: {ch}, rabbits: {rb}')'''


#task4
def filter_prime(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return n

'''numbers = str(input('Enter numbers: '))
numbs = numbers.split()
numbs = [num for num in numbs if filter_prime(int(num))]
print(numbs)'''


#task5
from itertools import permutations

def print_permutations():
    text = input("Enter text: ")
    perms = permutations(text)
    for perm in perms:
        print(''.join(perm))

'''print_permutations()'''


#task6
def text_reversed(text):
    words = text.split()
    i = len(words) - 1
    while i >= 0:
        print(words[i], end=' ')
        i -= 1

'''text = input('Enter text: ')
text_reversed(text)'''


#task7
def has_33(numbs):
    i = 0
    while i < len(numbs)-1:
        if numbs[i] == 3:
            if numbs[i+1] == 3:
                return True
        i += 1
    return False

'''numbers = input('Enter numbers: ')
numbs = numbers.split()
numbs = [int(num) for num in numbs]
print(has_33(numbs))'''


#task8
def spy_game(numbs):
    s = ''
    for i in numbs:
        s += i
    if '007' in s:
        return True
    return False

'''numbers = input('Enter numbers: ')
numbs = numbers.split()
print(spy_game(numbs))'''


#task9
def v_radius(radius):
    v_sphere = 4/3*3.14*radius**3
    return v_sphere 

'''radius = int(input('Enter radius: '))
print(v_radius(radius))'''


#task10
def unique_elements(l):
    new_list = []
    i = 0
    while i < len(l):
        t_or_f = True
        j = 0
        while j < i:
            if l[i] == l[j]:
                t_or_f = False
            j += 1
        if t_or_f:
            new_list.append(l[i])
        i += 1
    return new_list

'''l = input('Enter elements: ')
elements = l.split()
new_list = unique_elements(elements)
print(new_list)'''


#task11
def palindrome(text):
    i = 0
    j = len(text)-1
    while i < len(text)/2:
        if text[i] != text[j]:
            return 'No palindrome'
        i+=1
        j-=1
    return 'palindrome'

'''text = input('Enter text: ')
print(palindrome(text))'''


#task12 
def histogram(gist):
    i = 0
    while i < len(gist):
        j = 0
        while j < gist[i]:
            print('*', end='')
            j += 1
        print()
        i += 1

'''gist = input('Enter numbers: ')
gist = gist.split()
gist = [int(num) for num in gist]
histogram(gist)'''


#task13
import random

def find_num_random(rand_num, count):
    count += 1
    num = int(input('Take a guess.\n'))
    if num == rand_num:
        print(f'Good job, KBTU! You guessed my number in {count} guesses!')
        return
    print('\nYour guess is too low.')
    return find_num_random(rand_num, count)

'''name = input('Hello! What is your name?\n')
number = random.randint(1, 20)
count = 0
print(f'Well, {name}, I am thinking of a number between 1 and 20.\n')
find_num_random(number, count)'''
