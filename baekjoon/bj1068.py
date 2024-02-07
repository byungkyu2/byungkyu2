node=int(input())
parents_list = [int(i) for i in input().split(' ')]
num_del = int(input())
parents_list[num_del]=-2
cnt=0
prev_cnt=-1
while prev_cnt != cnt:
    prev_cnt=cnt
    for i in range(node):
        if parents_list[i]== -2:
            for j in range(node):
                if parents_list[j]==i:
                    parents_list[j]=-2
                    cnt+=1

count=0
for i in range(len(parents_list)):
    if parents_list[i] != -2 and i not in parents_list:
        count+=1
print(count)