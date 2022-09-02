if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(0, n):
        name, *marks = input().split()
        marks = list(map(float, marks))
        student_marks[name] = round(sum(marks) / len(marks),2)
    query_name = input()

    print("{:.2f}".format(student_marks[query_name]))