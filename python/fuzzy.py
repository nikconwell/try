#!/usr/bin/python3

import jaro
import argparse

known_good = [
    "This is a test string",
    "This is another string",
    "This is something else",
]

argParser = argparse.ArgumentParser()
argParser.add_argument('string')

args = argParser.parse_args()

input = args.string
print(f'Input: {input}')

best_match = -1
best_match_index = -1
check_index=0

for check in known_good:
    difference = jaro.jaro_winkler_metric(input,check)
    if difference > best_match:
        best_match_index = check_index
        best_match = difference
        if best_match == 1:
            break
    check_index = check_index + 1

print(f'{(best_match*100):.0f}% {known_good[best_match_index]}')



