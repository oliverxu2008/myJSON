#!/usr/bin/python
import json
import sys

# 
# Author: Oliver Xu
# Version 1.0
# 2017.12.21
#
# This tool is used to convert JSON type <input_file> into 2 formats:
# 1. compact format
# 2. Pretty text format with indent=2
#
# The <input_file> could be in either format above
# usage: ./myjson.py <input_file>
#


def print_json(file_name):
    #file_name = sys.argv[1]

    print '\n# Input file name:', file_name
    #print 

    f = open(file_name, 'r')
    text = f.read()

    # using json.loads() to convert string type into python dict
    my_dict = json.loads(text)

    # using json.dumps() to convert dict to string type - compact format
    compact_txt = json.dumps(my_dict)  

    print '\n# JSON data - compact format:', file_name
    print compact_txt



    # using json.dums() to convert json dict to pretty text format - string
    pretty_txt = json.dumps(my_dict, indent=2)

    print '\n# JSON data - pretty format:', file_name
    print pretty_txt
    print

def main():
    file_name = sys.argv[1]
    print_json(file_name)

if __name__ == '__main__':
    main()

