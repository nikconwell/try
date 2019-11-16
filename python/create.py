#!/usr/bin/python3

# Simple wrapper for createstack.  Use --help for usage.

import argparse
import re
from pathlib import Path

parser = argparse.ArgumentParser(description='Create stack at AWS')
parser.add_argument('JSON', nargs=1, type=argparse.FileType('r'), help='JSON parameters file for overriding template')
parser.add_argument('--template', type=argparse.FileType('r'),    help='Stack template (if not specified assumes $CWD or parent)')
parser.add_argument('--stackname', type=str,                      help='Name of stack, normally determined from JSON filename but can override here')
parser.add_argument('--region',   type=str, default='us-east-1',  help='Region to create in (%(default)s)')
parser.add_argument('--iam', action='store_true',                 help='Use IAM security credentials')

args = parser.parse_args()

# if (not (args.stuff or args.integer)):
#     print("\nYou must enter one of stuff or integer\n")
#     parser.print_usage()
#     exit()

JSON = args.JSON[0]
template=args.template
stackname = args.stackname
region = args.region
iam = args.iam

#
# Default the template to main.yaml in CWD or parent dir.
#

if (template == None):
    if (Path('main.yaml').is_file()):
        template = "main.yaml"
    elif (Path('../main.yaml').is_file()):
        template = "../main.yaml"
    # I am thinking here we can also get the path of the JSON file and look in that directory, that way we do not have
    # to necessarily run the commands directly from any directory...  Future option.

if (template == None):
    print("\nUnable to determine template, no main.yaml found in current or parent directory.  Override with --template if necessary...")
    exit(1)

#
# Default the stack name to substring of JSON filename - {stackname}-parameters.json
#

if (stackname == None):
    m = re.search(r'([\w-]+)-parameters.json',JSON.name)
    if (m.group(1)):
        stackname=m.group(1)

if (stackname == None):
    print("\nUnable to determine stackname from JSON filename ({}).  Filename should be stackname-parameters.json.  Override with --stackname if necessary...".format(JSON.name))
    exit(1)



print("You entered JSON={} template={} stackname={} region={} iam={}".format(JSON.name,template,stackname,region,iam))