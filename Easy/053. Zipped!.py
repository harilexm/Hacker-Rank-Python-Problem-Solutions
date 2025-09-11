N,X = map(int, input().split())
marks = list()

for i in range(X):
    marks.append(map(float, input().split()))
    
for student_marks in list(zip(*(marks))):
    print(sum(student_marks)/X)
