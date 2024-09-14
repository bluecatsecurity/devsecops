import os,sys

def calc(num1:int, num2:int):
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("No se puede dividir un nro por 0")

if __name__ == '__main__':
    calc(int(sys.argv[1]),int(sys.argv[2]))
    