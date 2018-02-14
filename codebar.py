class Member():
    def __init__(self,full_name):
        self.full_name = full_name
    def introduce(self):
        print('Hi!  My name is ' + self.full_name)

class Student(Member):
    def __init__(self,full_name,reason):
        Member.__init__(self,full_name)
        self.reason = reason

class Instructor(Member):
    def __init__(self,full_name,bio,skills):
        Member.__init__(self,full_name)
        self.skills = skills
        self.bio = bio
    def add_skill(self, skill):
        self.skills.append(skill)
    def print_skills(self):
        if len(self.skills) > 1:
            for i in range((len(self.skills) - 1)):
                print(self.skills[i] + ', ', end='')
            print(self.skills[(len(self.skills) - 1)])
        elif len(self.skills) == 1:
            print(self.skills[0])

class Workshop(Instructor, Student):
    def __init__(self,date,subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []
    def add_participant(self,participant):
        if participant.__class__.__name__ == 'Student':
            self.students.append(participant)
        elif participant.__class__.__name__ == 'Instructor':
            self.instructors.append(participant)
    def print_heading(self):
        print('Workshop - ' + str(self.date) + ' - ' + self.subject)
    def print_students(self):
        print('Students')
        for i in range(len(self.students)):
            print(str(i + 1) + '. ' + self.students[i].full_name + ' - ' + self.students[i].reason)
    def print_instructors(self):
        print('Instructors')
        for i in range(len(self.instructors)):
            print(str(i + 1) + '. ' + self.instructors[i].full_name + ' - ', end='')
            self.instructors[i].print_skills()
            print(self.instructors[i].bio)
    def print_details(self):
        self.print_heading()
        self.print_students()
        self.print_instructors()



workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.",["HTML","JavaScript"])
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love",["Python"])

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()
