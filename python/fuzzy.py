#!/usr/bin/python3

# pip3 install jaro-winkler
import jaro
import argparse
# Drive with:
# ./fuzzy.py --check "stuff"



# For REST API
# pip3 install flask
from flask import Flask, jsonify, request
# Drive with:
# ./fuzzy.py --rest
# curl -X PUT 'http://localhost:5000/check/'$( echo "This is a test string"|sed 's/ /%20/g')

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



#
# Check against list
#

def check_list(check,list):
    best_match = -1
    best_match_index = -1

    for index in range(len(list)):
        match = jaro.jaro_winkler_metric(check,list[index])
        if match > best_match:
            best_match = match
            best_match_index = index
            if best_match == 1: break   # 100% match, just end loop now
    return(best_match, list[best_match_index])


#
# Main processing
#

# Single check arg
if (args.check): 
    print(f'Input: {args.check}')
    (best_match,best_string) = check_list(args.check,known_good)
    print(f'{(best_match*100):.0f}% {best_string}')
elif (args.rest):
    print("Running as rest service")
    app = Flask('fuzzy')
    @app.route("/check/<string:string_to_check>", methods=['PUT'])
    def check_handler(string_to_check):
        (best_match,best_string) = check_list(string_to_check,known_good)
        return f'Received: {string_to_check}, fuzzy match is {(best_match*100):.0f}% {best_string}\n'
    
    app.run(debug=False)
