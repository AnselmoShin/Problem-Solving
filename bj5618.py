import sys
input = sys.stdin.readline

def solution1(para): # TimeOut Solution
    for candi in range(1, min(para)+1):
        flag = True
        for num in para:
            if num%candi != 0:
                flag = False
        if flag:
            print(candi)

def Euclid(num1, num2):
    if num1 == 0:
        return num2
    return Euclid(num2%num1, num1)

def solution2(para):
    if len(para) == 2:
        gcd = Euclid(para[0], para[1])
    else:
        gcd = Euclid(para[2], Euclid(para[0], para[1]))
    for candi in range(1, gcd//2+1):
        if gcd%candi == 0:
            print(candi)
    print(gcd)

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int,input().split(" ")))
    solution1(nums)
    print()
    solution2(nums)