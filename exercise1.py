#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
        1st QuestionTask of Virtually Live's Technical Test.


"""

import sys
from sys import stdin
import argparse

from numpy.random import seed
from numpy.random import randint
from time import time

from util_params import param_int
from util_string_constants import MSG_EXITING
from util_string_constants import MSG_END
from util_string_constants import MSG_COMMON_TITLE

MSG_EXERCISE_TITLE = "Maximum Difference in an Array"
MSG_PROMPT = "Enter the number of items in array, then the numbers in array:"
MSG_MAX_DIFFERENCE = "Max Difference:{}"

MSG_DIFFERENCE = "DIFFERENCE in Iter.{} R1:{} R2:{}"
MSG_SAMPLE = "Iter.{} {}"
MSG_ITERATIONS_MAX_OK_KO = "Iterations:{} OK:{} KO:{}"
MSG_AVERAGE_TIME = "Method {} Time:{:10.6f} Iter:{}. Average time: {:10.6f}"
MSG_COMPARING = 'Comparing...'


MSG_HELP_P1 = "Method to use 1=Strict Implementation 2=Other Implementation"

MIN_LINES = 1
MAX_LINES = 2*10e5
MIN_ITEM = -10e6
MAX_ITEM = 10e6


def PrintUsageAndExit():
    print('excercise1 [-t] [-m (1|2)]')
    print('  Read from stdin:')
    print('     integer (number of items 1<= n <= 2 x 10e5)')
    print('     integer (-10e6 <= n <= 10e6)')
    print(MSG_END)
    sys.exit(1)


def main(argv):
    print(MSG_COMMON_TITLE.format(1))
    print(MSG_EXERCISE_TITLE)
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--method", type=int, choices=[1, 2],
                        default=1,
                        help=MSG_HELP_P1)

    parser.add_argument("-t", "--test", action="store_true")
    args = parser.parse_args()
    if args.test:
        CompareMethods()
    else:
        if args.method and args.method == 2:
            MaxDifference_selectedmethod = MaxDifference_opt
        else:
            MaxDifference_selectedmethod = MaxDifference
        print(MSG_PROMPT)

        num_lines = param_int(stdin.readline(), MIN_LINES, MAX_LINES)
        if num_lines:
            sample = []
            for lines in range(num_lines):
                item = param_int(stdin.readline(), MIN_ITEM, MAX_ITEM)
                if item and MIN_ITEM <= item <= MAX_ITEM:
                    sample.append(item)
                else:
                    PrintUsageAndExit()

            d = MaxDifference_selectedmethod(sample)
            print(MSG_MAX_DIFFERENCE.format(d))
            print(MSG_END)
        else:
            PrintUsageAndExit()


def MaxDifference(a):
    #return max([aix-s for ix, aix in enumerate(a) for s in a[0:ix] if s < aix], default=-1)
    return max([a[ix]-s for ix in range(len(a)) for s in a[0:ix] if s<a[ix]], default=-1)


def MaxDifference_opt(a):
    if len(a) <= 1:
        return -1

    d = -1
    minimum = a[0]

    for ai in a:
            d1 = ai - minimum
            if d1 > 0 and d1 > d:
                d = d1
            if ai < minimum:
                minimum = ai
    return d


def GenerateBigSample():
    len_array = randint(MIN_LINES, 2*1000)  # MAX_LINES !!!
    return randint(MIN_ITEM, MAX_ITEM, len_array)


def CompareMethods():
    print(MSG_COMPARING)
    seed(1)
    maximo = 1000
    t1_sum = 0
    t2_sum = 0
    ok = 0
    ko = 0
    for iteration in range(maximo):
        sample = GenerateBigSample()
        t1 = time()
        r1 = MaxDifference(sample)
        t2 = time()
        t1_sum += t2-t1
        t1 = time()
        r2 = MaxDifference_opt(sample)
        t2 = time()
        t2_sum += t2-t1
        if r1 == r2:
            ok += 1
        else:
            print(MSG_DIFFERENCE.format(iteration, r1, r2))
            print(MSG_SAMPLE.format(iteration, sample))
            ko += 1

    print(MSG_ITERATIONS_MAX_OK_KO.format(maximo, ok, ko))
    print(MSG_AVERAGE_TIME.format(1, t1_sum, maximo, t1_sum/maximo))
    print(MSG_AVERAGE_TIME.format(2, t2_sum, maximo, t2_sum/maximo))
    print(MSG_END)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except(KeyboardInterrupt, SystemExit):
        print(MSG_EXITING)
        sys.exit()
