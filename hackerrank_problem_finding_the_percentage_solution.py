if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a = (sum(student_marks[query_name]))/ 3
    b = format(a, ".2f")
    print(b)
    
