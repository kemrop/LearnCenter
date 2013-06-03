from student import student

grades = {'Math': 80, 'English': 85, 'Science': 80, 'Agriculture':75, 'Art,Craft & Music': 82}
student = student('Mark', grades, 'Male')
print student.getStudentInfo()
print "\n\n\n"
print student.getGrades()