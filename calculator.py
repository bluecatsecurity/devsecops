import sys

def sumar(num1:int,num2:int):
    return num1+num2

def restar(num1:int,num2:int):
    return num1-num2

if __name__ == '__main__':
    if sys.argv[1] == 'sumar':
        print(sumar(int(sys.argv[2]),int(sys.argv[3])))
    elif sys.argv[1] == 'restar':
        print(restar(int(sys.argv[2]),int(sys.argv[3])))
    