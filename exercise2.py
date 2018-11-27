#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
        2nd QuestionTask of Virtually Live's Technical Test.


"""
import sys
from sys import stdin
import re

from util_params import param_int
from util_params import param_string

from util_string_constants import MSG_EXITING
from util_string_constants import MSG_END
from util_string_constants import MSG_COMMON_TITLE

MSG_EXERCISE_TITLE = ""

MIN_LINES = 1
MAX_LINES = 10e3
MIN_ITEM = 1
MAX_ITEM = 10e3

RE_EMAIL_BASE = '^[a-z]{1,6}_{0,1}[0-9]{0,4}@'

MSG_EXERCISE_TITLE = "Validating Email Addresses with Regex"
MSG_PROMPT = "Enter the number of e-mail items, then e-mails:"
MSG_RESULT_VALIDATION = "Email {} is {}"


def PrintUsageAndExit():
    print('excercise2')
    print('  Read from stdin:')
    print('     integer (number of items 1<= n <= 2 x 10e5)')
    print('     string (-10e6 <= n <= 10e6)')
    print(MSG_END)
    sys.exit(1)


def main(argv):
    print(MSG_COMMON_TITLE.format(2))
    print(MSG_EXERCISE_TITLE)
    print(MSG_PROMPT)
    num_lines = param_int(stdin.readline(), MIN_LINES, MAX_LINES)
    if num_lines:
        sample = []
        for lines in range(num_lines):
            item = param_string(stdin.readline(), MIN_ITEM, MAX_ITEM)
            if item:
                sample.append(item)
            else:
                PrintUsageAndExit()
        PrintResultValidation(ValidateEmails(sample))
        print(MSG_END)


def PrintResultValidation(validation):
    for tuple in validation:
        print(MSG_RESULT_VALIDATION.format(tuple[0], tuple[1]))


def ValidateEmails(sample):
    result = []
    for email in sample:
        result.append((email, ValidateEmail(email)))
    return result


def ValidateEmail(email_str):
    RE_EMAIL_hackerrankcom = (RE_EMAIL_BASE +
                              createcaseinsensitivepartial("hackerrank.com") +
                              '$')
    # In the question is not specified if the domain name and extesion must be
    # lowercase, so I did it match with any combination of uppercase and
    # lowercase only in the domain.extension segment

    print(RE_EMAIL_hackerrankcom)
    if re.match(RE_EMAIL_hackerrankcom, email_str):
        return True
    else:
        return False


def createcaseinsensitivepartial(string):
    result = ""
    for c in string:
        if c == ".":
            result += '\\' + c
        else:
            result += "[" + c.upper() + "|" + c.lower() + "]"
    return result


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except(KeyboardInterrupt, SystemExit):
        print(MSG_EXITING)
        sys.exit()
