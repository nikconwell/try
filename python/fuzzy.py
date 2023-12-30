#!/usr/bin/python3


import re

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
flask_host='127.0.0.1'
flask_port='5000'
argParser = argparse.ArgumentParser()
argParser.add_argument('--check', dest='check', help='String to check against known good')
argParser.add_argument('--rest', dest='rest', nargs='?', const=f'{flask_host}:{flask_port}', help=f'Run in REST mode answering queries, defaults to {flask_host}:{flask_port}')
argParser.add_argument('--debug', dest='debug', default=False, action='store_true', help='Debug mode for Flask and other things')

args = argParser.parse_args()

#
# Allow to override the REST flask host and port
#
if (args.rest):
    match = re.search('([^:]*):?(\d*)',args.rest)
    if (match):
        flask_host = match.group(1)
        flask_port = match.group(2)

#
# Check a string against list of known good strings
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
# Flask request handler
#
def check_handler(string_to_check):
    (best_match,best_string) = check_list(string_to_check,known_good)
    return f'Received: {string_to_check}, fuzzy match is {(best_match*100):.0f}% {best_string}\n'


#
# Main processing
#

#
# Single check of a string
#
if (args.check): 
    print(f'Input: {args.check}')
    (best_match,best_string) = check_list(args.check,known_good)
    print(f'{(best_match*100):.0f}% {best_string}')
elif (args.rest):
    #
    # Run in REST mode, call with something like: curl -X PUT 'http://localhost:5000/check/'$( echo "This is a test string"|sed 's/ /%20/g')
    #
    print("Running as rest service")
    app = Flask('fuzzy')
    app.add_url_rule("/check/<string:string_to_check>", view_func=check_handler, methods=['PUT'])
    
    app.run(debug=args.debug, host=flask_host, port=flask_port)
