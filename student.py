class student:
    def __init__(self, name, grades,  grade):
        """ """
        self.name = name
        self.grades = grades
        self.grade = grade
    def getStudentInfo(self):
        student_info = {"Name": self.name, "Grade": self.grade}
        return student_info;
    def getGrades(self):
        grade_alpha = {}
        for grade in self.grades.keys():
            if self.grades[grade] > 0 and self.grades[grade] < 50:
                alpha = "E"
                grade_alpha[grade] = alpha
            elif self.grades[grade] > 50 and self.grades[grade] < 60:
                alpha = "D"
                grade_alpha[grade] = alpha
            elif self.grades[grade] > 60 and self.grades[grade] < 70: 
                alpha = "C"
                grade_alpha[grade] = alpha
            elif self.grades[grade] > 70 and self.grades[grade] < 80: 
                alpha = "B"
                grade_alpha[grade] = alpha
            elif self.grades[grade] >= 80: 
                alpha = "A"
                grade_alpha[grade] = alpha
        sorted(grade_alpha, key=grade_alpha.get)
        return grade_alpha
