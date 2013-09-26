import unittest
from student import student

class TestStudent(unittest.TestCase):
    def setUp(self):
        grades = {"Math": 80, "English": 85, "Science": 59, "Agriculture":75, "Art,Craft & Music": 82}
        name = "Mark"
        grade = "Grade 8"
        unittest.TestCase.setUp(self)
        self.student = student(name, grades, grade)

    def test_get_student_info_succeeds(self):
        expected = {"Name": "Mark", "Grade": "Grade 8"}
        actual = self.student.getStudentInfo()
        self.assertEqual(expected, actual)

    def test_get_student_grade_succeeds(self):
        expected = {"Math":"A", "English":"A", "Science":"D", "Agriculture":"B", "Art,Craft & Music":"A"}
        sorted(expected, key=expected.get)
        actual = self.student.getGrades()
        self.assertEqual(expected, actual)
 
    def test_get_student_grade_fails(self):
        expected = {"Math":"B", "English":"A", "Science":"D", "Agriculture":"C", "Art,Craft & Music":"A"}
        sorted(expected, key=expected.get)
        actual = self.student.getGrades()
        self.assertNotEquals(expected, actual)