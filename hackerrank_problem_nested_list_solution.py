if __name__ == '__main__':
    l1 = []
    l2 = []
    for _ in range(int(input())):
        name = str(input())
        score = float(input())
        l1.append([name, score])
        l2.append(score)
l2.sort()
second_lowest = sorted(set(l2))
# print(second_lowest[1])
name = []
# sorted_name = []
for names, scores in l1[0:]:
    if scores == second_lowest[1]:
        name.append(names)
        name.sort()
for e in name:
    print(e)
