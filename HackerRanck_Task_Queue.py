"""
Time:
6m 18s/13m

Try:
0 Debug: Success
"""
import sys
input = sys.stdin.readline

def ceiling(num):
    if num - int(num)> 0:
        return int(num)+1
    else:
        return int(num)

def solution():
    num_que = int(input().strip())
    batch_size = []
    for i in range(num_que):
        batch_size.append(int(input().strip()))
    
    num_que = int(input().strip())
    processing_time = []
    for i in range(num_que):
        processing_time.append(int(input().strip()))
    
    num_que = int(input().strip())
    num_task = []
    for i in range(num_que):
        num_task.append(int(input().strip()))

    answer = -1
    for i in range(num_que):
        task_time = ceiling(num_task[i]/batch_size[i]) * processing_time[i]
        if task_time > answer:
            answer = task_time
        else:
            pass
    return answer

if __name__ == "__main__":
    print(solution())