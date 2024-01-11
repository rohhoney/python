import sys

args = sys.argv[1:]
args = map(int, args)
sum_args = sum(args)
print(sum_args)