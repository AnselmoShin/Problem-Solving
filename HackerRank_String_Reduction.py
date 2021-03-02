"""
Time:
10m 22s /13m

Try:
0 Debug: Fail
1 Debug: Fail
2 Debug: Fail
3 Debug: Success
"""

import sys
input = sys.stdin.readline

def solution():
    given = list(input().strip())
    flag = dict()
    for each in given:
        flag[each] = False
    answer = 0
    for each in given:
        # print(each, flag[each])
        if flag[each]:
            answer += 1
        else:
            flag[each] = True
    return answer

if __name__ == "__main__":
    print(solution())