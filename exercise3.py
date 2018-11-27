#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
        3rd QuestionTask of Virtually Live's Technical Test.


"""

import sys
from sys import stdin

from util_params import param_string

from util_string_constants import MSG_EXITING
from util_string_constants import MSG_END
from util_string_constants import MSG_COMMON_TITLE

MSG_EXERCISE_TITLE = "Approximate Matching"
MSG_PROMPT = "Entre text, prefix and suffix in three separate lines:"

MIN_ITEM = 1
MAX_ITEM = 50


def PrintUsageAndExit():
    print('excercise3')
    print('  Read from stdin:')
    print('     text   ( 1<= len(n) <= 50 (ASCII [a-z])')
    print('     prefix ( 1<= len(n) <= 50 (ASCII [a-z])')
    print('     suffix ( 1<= len(n) <= 50 (ASCII [a-z])')
    print(MSG_END)
    sys.exit(1)


def main(argv):
    print(MSG_COMMON_TITLE.format(3))
    print(MSG_EXERCISE_TITLE)
    print(MSG_PROMPT)
    text = param_string(stdin.readline(), 1, MAX_ITEM)
    if not text:
        PrintUsageAndExit()
    prefixString = param_string(stdin.readline(), az=True)
    if not prefixString:
        PrintUsageAndExit()
    suffixString = param_string(stdin.readline(), az=True)
    if not suffixString:
        PrintUsageAndExit()

    (maxsub, score) = MaxScoredSubstring(text, prefixString, suffixString)
    print("{}".format(maxsub))
    print(MSG_END)


def MaxScoredSubstring(text, prefixString, suffixString):
    maxscore = 0
    maxsubstring = ""

    for sub in GenerateSubstrings(text):
        p_score = max([i for i in range(1, len(prefixString)+1)
                      if sub.startswith(prefixString[-i:])], default=0)
        s_score = max([i for i in range(1, len(suffixString)+1)
                      if sub.endswith(suffixString[0:i])], default=0)
        score = p_score + s_score
        if score == maxscore:
            if sub < maxsubstring:
                maxsubstring = sub
        elif score > maxscore:
            maxscore = score
            maxsubstring = sub
    return (maxsubstring, maxscore)


def GenerateSubstrings(text):
    l = len(text)
    return [text[i:j+1] for i in range(l) for j in range(i, l)]


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except(KeyboardInterrupt, SystemExit):
        print(MSG_EXITING)
        sys.exit()
