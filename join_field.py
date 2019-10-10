#!/bin/env python

import sys
from optparse import OptionParser

def main():
    usage_str="usage: %prog [options] file list ..."
    parser = OptionParser(usage=usage_str)
    parser.add_option("-f", "--field_num", dest="field_num", default=1,
                      help="specify the field number", metavar="FIELD_NUM")
    parser.add_option("-z", action="store_true", dest="zero",
                      help="set 0 for undefined value")
    (options, args) = parser.parse_args()
    # 'field_num' is specified in the range from 0(key) to 1, 2, ...(values)
    field_num = 1
    default_value = ""
    if (options.field_num):
        field_num = int(options.field_num)
    if (parser.has_option("zero")):
        default_value = 0
    files = args
    
    result= {}
    num_files = len(files)
    for i in range(num_files):
        fp = open(files[i])
        for line in fp:
            line = line.rstrip('\n')
            name_value_list = line.split('\t')
            name = name_value_list[0]
            if (len(name_value_list) > field_num):
                value = name_value_list[field_num]
            else:
                value = default_value
            if name[:2] == 'k.': continue
            if not result.has_key(name):
                result[name] = [ default_value for j in range(num_files) ]
            result[name][i] = value
        fp.close()

    for name in result.keys():
        print "%s\t%s"%(name, '\t'.join(map(str, result[name])))

if __name__ == "__main__":
    main()
