qqfrom statistics import mean
import matplotlib.pyplot as plt

from student.student import Student
from assignment.assignment import Assignment


class Course(object):
    def __init__(self, teacher):
        self.teacher = teacher
        self.students = []
        self.assignments = []
        self.grades = []
        self.names = [] # this variable was never used

    def __repr__(self):
        ret = '\n'
        ret += '\tProfessor: {}\n'.format(self.teacher)
        ret += '\tNumber of Students: {}\n'.format(len(self.students))

        if len(self.students):
            ret += '\t\t' + ','.join(str(s) for s in self.students) + '\n'

        ret += '\tNumber of Assignments: {}\n'.format(len(self.assignments))

        if len(self.assignments):
            ret += '\t\t' + ','.join(str(a.difficulty) for a in self.assignments) + '\n'

        if len(self.assignments) > 0 and len(self.grades) > 0:
            ret += 'Average grade: {}'.format(sum(self.grades) / len(self.grades))
        return ret
    
    def __add__(self, other):
        if isinstance(other, Student):
            self.addStudent(other)
        elif isinstance(other, Assignment):
            self.assign(other)
        return self
    
    def assign(self, assignment):
        self.assignments.append(assignment)
        for student in self.students:
            self.grades.append(student.completeAssignment(assignment))
        return assignment
    
    def register(self, student):
        self.addStudent(student)
    
    def addStudent(self, student):
        self.students.append(student)

    def finish(self):
        # print average of all grades
        print(f'Class Average: {mean(self.grades)}')
        # print teacher pay
        tPay = 0
        for assignment in self.assignments:
            tPay += assignment.difficulty * len(assignment.grades)
        self.teacher.pay = tPay
        print(f'Teacher pay: {self.teacher.pay}')

    def plot(self):
        fig, axes = plt.subplots(3, 1)
        axes[0].set_title('Grades by assignment')
        axes[0].set_ylabel('Grade')

        handles = []
        for s in self.students:
            # array initially empty
            handles.append(axes[0].scatter(list(range(len(self.assignments))), s.grades))

        # set legend
        axes[0].legend(handles, [s.name for s in self.students], loc='upper right', bbox_to_anchor=(1.35, 1), fancybox=True)

        # set x axis labels and ticks
        axes[0].set_xticks([i for i in range(len(self.assignments))])

        # next subplot
        axes[1].set_title('Grades by Student')
        axes[1].set_ylabel('Grade')

        handles = []
        for a in self.assignments:
            # array initially empty
            handles.append(axes[1].scatter(list(range(len(self.students))), a.grades))
            
        # set legend
        axes[1].legend(handles, [i for i in range(len(self.assignments))], loc='upper right', bbox_to_anchor=(1.3, 1), fancybox=True)

        # set x axis labels and ticks
        axes[1].set_xticks([i for i in range(len(self.students))])
        axes[1].set_xticklabels([s.name for s in self.students])

        # next subplot

        axes[2].set_title('Assignment Difficulty')
        axes[2].set_ylabel('Difficulty')

        difficulties = [a.difficulty for a in self.assignments]
        axes[2].plot(list(range(len(self.assignments))), difficulties)

        # set x axis labels and ticks
        axes[2].set_xticks([i for i in range(len(self.assignments))])

        # plot
        plt.subplots_adjust(right=.7, hspace=1)
        plt.show()
