#!/usr/bin/python3

# pip3 install jaro-winkler
import jaro
import argparse

known_good = [
    "This is a test string",
    "This is another string",
    "This is something else",
]

#
# Args
#

argParser = argparse.ArgumentParser()
argParser.add_argument('--check', dest='check', help='String to check against known good')
argParser.add_argument('--rest', dest='rest', action='store_true', help='Run in REST mode answering queries')

args = argParser.parse_args()

if (args.check): 
    check = args.check
    print(f'Input: {check}')


#
# Check against known_good
#

best_match = -1
best_match_index = -1

for index in range(len(known_good)):
    match = jaro.jaro_winkler_metric(check,known_good[index])
    if match > best_match:
        best_match = match
        best_match_index = index
        if best_match == 1:   # 100% match, just end loop now
            break

#
# Output results
#

print(f'{(best_match*100):.0f}% {known_good[best_match_index]}')



