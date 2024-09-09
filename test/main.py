import os,sys

def calc(num1:int, num2:int):
    return num1/num2

if __name__ == '__main__':
    result = calc(int(sys.argv[1]),int(sys.argv[2]))
    print(result)