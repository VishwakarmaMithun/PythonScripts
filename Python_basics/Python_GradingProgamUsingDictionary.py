
#student scores
student_scores ={
"Harry":81,
"Ron":78,
"Hermion1":99,
"Darco":74,
"Neville":62
}

#Create a empty dictionary called student grades
student_grades ={}
print(student_grades)

for student in student_scores:
    score = student_scores[student];
    if score > 90 :
        student_grades[student]='Outstanding';
    elif score >80 :
        student_grades[student]="Exceeds Exceptions"
    elif score >70 : 
        student_grades[student]="Acceptable"
    else:
        student_grades[student]='Fail'
#print student grades
print(student_grades)