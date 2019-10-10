#!/bin/env python

def main(files):
	result= {}
	num_files = len(files)
	for i in range(num_files):
		fp = open(files[i])
		for line in fp:
			name, val = line.split('\t')
			if name[:2] == 'k.': continue
			if not result.has_key(name):
				result[name] = [ 0 for j in range(num_files)]
			result[name][i] = int(val)
		fp.close()

	for name in result.keys():
		print "%s\t%s"%(name, '\t'.join(map(str, result[name])))

import sys
if __name__ == "__main__":
	main(sys.argv[1:])
