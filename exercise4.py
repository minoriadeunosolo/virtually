#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
        4rd QuestionTask of Virtually Live's Technical Test.


"""
import sys
from sys import stdin

from util_params import param_string
from util_params import param_int

from util_string_constants import MSG_EXITING
from util_string_constants import MSG_END
from util_string_constants import MSG_COMMON_TITLE

MSG_EXERCISE_TITLE = "Username Disparity"
MSG_PROMPT = "Enter the number number of items, then a string in each line"

MIN_LINES = 1
MAX_LINES = 10
MIN_ITEM = 1
MAX_ITEM = 10e5


def PrintUsageAndExit():
    print('excercise4')
    print('  Read from stdin:')
    print('     integer (number of items 1<= n <= 10)')
    print('     string (1 <= len(n) <= 10e5) (ASCII [a-z])')
    print(MSG_END)
    sys.exit(1)


def main(argv):
    print(MSG_COMMON_TITLE.format(4))
    print(MSG_EXERCISE_TITLE)
    print(MSG_PROMPT)
    num_lines = param_int(stdin.readline(), MIN_LINES, MAX_LINES)
    if num_lines:
        sample = []
        for line in range(num_lines):
            item = param_string(stdin.readline(), MIN_ITEM, MAX_ITEM, az=True)
            if item:
                sample.append(item)
            else:
                PrintUsageAndExit()

        disparities = usernameDisparity(sample)
        for d in disparities:
            print("{}".format(d))
    else:
        PrintUsageAndExit()


def usernameDisparity(inputs):
    return [Disparity(l) for l in inputs]


def Disparity(str):
    score = 0
    for sub in GenerateSuffixSubstrings(str):
        score += GetScoresubstring(sub, str)
    return score


def GenerateSuffixSubstrings(text):
    l = len(text)+1
    return [text[i:l] for i in range(l)]


def GeneratePreffixSubstrings(text):
    l = len(text)
    return [text[0:i+1] for i in range(l)]


def GetScoresubstring(sub, str):
    score = 0
    for pref in GeneratePreffixSubstrings(sub):
        if str.startswith(pref):
            score = len(pref)
        else:
            break
    return score


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except(KeyboardInterrupt, SystemExit):
        print(MSG_EXITING)
        sys.exit()
