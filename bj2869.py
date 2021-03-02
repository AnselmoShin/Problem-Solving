import sys
input = sys.stdin.readline

def solution1(clime, fall, dist):
    left = dist
    date = 0
    while True:
        # print(date)
        date += 1
        left -= clime
        if left <=0:
            break
        left += fall
    return date

def solution2(clime, fall, dist):
    left = dist - clime
    if left%(clime-fall) == 0:
        date = left//(clime-fall)
    else:
        date = left//(clime-fall) + 1
    date += 1
    return date

if __name__ == "__main__":
    clime, fall, dist = map(int, input().split())
    # print(solution1(clime, fall, dist))
    print(solution2(clime, fall, dist))