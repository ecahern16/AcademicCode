from person.person import Person


class Teacher(Person):
    def __init__(self, name, pay=None):
        Person.__init__(self, name)
        self.pay = 0
        
    def __repr__(self):
        return self.name
        
        