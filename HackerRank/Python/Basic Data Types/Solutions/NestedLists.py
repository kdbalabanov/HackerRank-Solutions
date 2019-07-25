if __name__ == '__main__':

    num_students = int(input())
    student_list = []

    for student in range(num_students):
        name = input()
        score = float(input())
        student_list.append(list((name, score)))
    
    result=[]
    counter = 0
    student_list.sort(key=lambda x: x[1])

    for student in student_list:
        if student[1] == student_list[0][1]:
            counter += 1

    student_list = student_list[counter:]

    for student in student_list:
        if student[1] == student_list[0][1]:
            result.append(student)
    
    result.sort(key=lambda x: x[0])
    
    for student in result:
        print(student[0])