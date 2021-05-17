#!/usr/bin/env python3

import itertools, re, math, operator, functools

alphabet = "abcdefghijklmnopqrstuvwxyz"

PRIME = 1000000007

def check_str(s):
    for c in alphabet:
        if len(re.split(c + '+', s)) > 2:
            return False
    return True

def typeof(s, c):
    if s[0] == c and s[-1] == c:
        return 'both'
    elif s[0] == c:
        return 'head'
    elif s[-1] == c:
        return 'tail'
    else:
        return 'none'

def product(iterable):
    return functools.reduce(operator.mul, iterable, 1)

def multi_delete(list_, *args):
    indexes = sorted(list(args), reverse=True)
    for index in indexes:
        del list_[index]
    return list_

def count(cars):
    for c in alphabet:
        types = [(car_id, typeof(car, c)) for (car_id, car) in enumerate(cars)]
        heads = [s for s in types if s[1] == 'head']
        tails = [s for s in types if s[1] == 'tail']
        boths = [s for s in types if s[1] == 'both']

        if len(heads) > 1 or len(tails) > 1:
            return 0

        if len(boths) > 1: #merge all boths
            merged = " ".join(cars[b[0]] for b in boths)
            cars = [car for car in cars if typeof(car, c) != 'both']
            cars += [merged]

        types = [(car_id, typeof(car, c)) for (car_id, car) in enumerate(cars)]
        heads = [s for s in types if s[1] == 'head']
        tails = [s for s in types if s[1] == 'tail']
        boths = [s for s in types if s[1] == 'both']

        if len(heads) == 1 and len(tails) == 1 and len(boths) == 0: #merge tail-head
            t_id = tails[0][0]
            h_id = heads[0][0]
            cars[t_id] = cars[t_id] + cars[h_id]
            del cars[h_id]
        elif len(heads) == 1 and len(tails) == 1 and len(boths) == 1: #merge tail-both-head
            t_id = tails[0][0]
            b_id = boths[0][0]
            h_id = heads[0][0]
            cars[t_id] = cars[t_id] + cars[b_id] + cars[h_id]
            multi_delete(cars, b_id, h_id)
        elif len(heads) == 1 and len(tails) == 0 and len(boths) == 1: #merge both-head
            b_id = boths[0][0]
            h_id = heads[0][0]
            cars[b_id] = cars[b_id] + cars[h_id]
            del cars[h_id]
        elif len(heads) == 0 and len(tails) == 1 and len(boths) == 1: #merge tail-both
            t_id = tails[0][0]
            b_id = boths[0][0]
            cars[t_id] = cars[t_id] + cars[b_id]
            del cars[b_id]

    test_str = ''.join(cars).replace(' ', '')
    if check_str(test_str):
        ret = math.factorial(len(cars)) % PRIME
        ret = (ret * product([math.factorial(len(car.split(' ')) % PRIME) % PRIME for car in cars])) % PRIME
        return ret
    else:
        return 0

for t in range(int(input(''))):
    N = int(input(''))
    cars = input('').split(' ')

    print("Case #%i: %i" % (t + 1, count(cars)))