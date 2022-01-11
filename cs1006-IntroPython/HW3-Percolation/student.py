from person.person import Person
from utilities.utilities import skillToGrade


class Student(Person):
    def __init__(self, name, skill):
        super(Student, self).__init__(name)
        self.grades = []
        self.skill = skill
        self.name = name
    
    def completeAssignment(self, assignment):
        assignmentGrade = skillToGrade(self.skill, assignment.difficulty)
        self.grades.append(assignmentGrade)
        assignment.grades.append(assignmentGrade)
        return assignmentGrade
