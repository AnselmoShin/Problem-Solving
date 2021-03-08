"""
Time:
10m/13m

Try:
0 Debug: Fail
1 Debug: Success
"""

import sys
input = sys.stdin.readline

def solution(para):
    if para == 1:
        return False
    for i in range(2,para):
        if i**2 > para:
            break
        if para%i == 0:
            return False
    return True

if __name__ =="__main__":
    print(solution(int(input())))