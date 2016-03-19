import argparse
import os


parser = argparse.ArgumentParser(description='search images containing provided color')
parser.add_argument('c', nargs='+', help='colors to search for')
parser.add_argument('-d', help='directory to search in')
parser.add_argument('-e', nargs='+', help='file extensions', default=['jpg'])
args = parser.parse_args()
print args.e, " ", args.d

directory = args.d or os.curdir
for f in os.listdir(directory):
    if True in map(lambda x: f.endswith(x), args.e):
        print(f)