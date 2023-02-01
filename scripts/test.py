import os,sys
PRUEBA= os.getenv("PRUEBA")
def test():
    print("2")
    print(PRUEBA)
    return "FUNCIONA"


test(*sys.argv[1:])