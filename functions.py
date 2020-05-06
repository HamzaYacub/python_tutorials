def grade(name, homework, assessment, exam):
    hwPercent = homework / 25 
    assessmentPercent = assessment / 50
    examPercent = exam / 100

    final_grade = (hwPercent + assessmentPercent + examPercent) / 3
    final_grade = round(final_grade * 100)

    return name + " recieved a grade of: " + str(final_grade)

g = grade("Hamza", 21, 37, 78)

print(g)