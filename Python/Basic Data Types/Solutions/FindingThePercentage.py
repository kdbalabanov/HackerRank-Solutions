if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    query_result = student_marks[query_name]
    avg_score = sum(query_result) / len(query_result)
    print("%.2f" % avg_score)