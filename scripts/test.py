import os,sys

def test():
    print("2")
    return "FUNCIONA"

test(*sys.argv[1:])