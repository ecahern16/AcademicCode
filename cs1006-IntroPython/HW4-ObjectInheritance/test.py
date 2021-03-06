#from engi1006_simulator.teacher import Teacher
#from engi1006_simulator.course import Course
#from engi1006_simulator.student import Student
#from engi1006_simulator.assignment import Assignment

from teacher.teacher import Teacher
from course.course import Course
from student.student import Student
from assignment.assignment import Assignment

def main():
    # instantiate a teacher
    t = Teacher('Joe')

    # instantiate a class
    c = Course(t)

    # register three student objects
    c.register(Student('Jack', 50))
    c.register(Student('Jill', 60))
    c.register(Student('Jane', 75))

    # assign 4 assignment objects
    c.assign(Assignment(50))
    c.assign(Assignment(75))
    c.assign(Assignment(80))
    c.assign(Assignment(90))

    # summarize the class
    c.finish()
    # expected output (average may vary)
    # Class Average : 74.083894
    # Teacher pay: 885.000000

    # plot the three charts
    c.plot()

if __name__ == '__main__':
    main()
