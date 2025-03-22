# A Requirement represents a class including name, grade, and if they have passed.
class Requirement:
    def __init__(self, requirement_name: str):
        self.requirement_name = requirement_name
        self.grade = "U"
        self.has_passed = False
    def get_grade(self):
        return self.grade
    def set_grade(self, new_grade: str):
        self.grade = new_grade
        if self.grade not in ["F", "D" , "U"]:
            self.has_passed = True
        else:
            self.has_passed = False
# Major represents a students major by containing a list of Requirements and allows to add Requirements, get Requirements and set Grade in a Requirement.
class Major:
    def __init__(self, major_name: str):
        self.major_name = major_name
        self.requirements = []
    def add_requirements(self, requirement: list):
        self.requirements.extend(requirement)
    def get_requirements(self):
        return self.requirements
    def set_requirement_grade(self, requirement_name: str, grade: str):
        for requirement in self.requirements:
            if requirement.requirement_name == requirement_name:
                requirement.set_grade(grade)
                break
        else:
            print(f"Requirement {requirement_name} not found")
# Computer Science Class inherits from Major Class, it includes a list of Requirements added to the Major.
class Computer_Science(Major):
    def __init__(self):
        super().__init__("Computer Science")
        # Major Core Courses
        CIS121 = Requirement("Intro To Programming")
        CIS122 = Requirement("Data Structures")
        CIS223 = Requirement("Algorithms")
        CIS224 = Requirement("Computer Architecture")
        CS301 = Requirement("CS Core: Operating Systems")
        CS302 = Requirement("CS Core:Software Engineering & Parallel Computing")
        CS303 = Requirement("CS Core: Programming Languages")
        CS304 = Requirement("CS Core: Databases & Information Security")
        CS391W = Requirement("Computer Science Project 1")
        CS392W = Requirement("Computer Science Project 2")
        CS491W = Requirement("Computer Science Capstone 1")
        CS495 = Requirement("Computer Science Seminar: Take 4 credits")
        MATH122 = Requirement("Calculus II")
        MATH247 = Requirement("Linear Algebra I")
        MATH280 = Requirement("Discrete for Comp Sci I")
        MATH354 = Requirement("Concepts of Probability & Statistics")
        MATH380 = Requirement("Discrete Mathematics for Computer Science II")
        CS492W = Requirement("Computer Science Capstone 2") 
        CS498W = Requirement("Senior Thesis")
        self.add_requirements([CIS121, CIS122, CIS223, CIS224, CS301, CS302, CS303, CS304, CS391W, CS392W, CS491W, CS495, MATH122, MATH247, MATH280, MATH354, MATH380, CS492W, CS498W])
# Student Class stores a name, Tech ID, and Major, and allows to declare a major.
class Student:
    def __init__(self, first_name: str, last_name: str, tech_id: str):
        self.first_name = first_name
        self.last_name = last_name
        self.tech_id = tech_id
        self.major = None
    def declare_major(self, new_major: Major):
        self.major = new_major
    def __str__(self):
        return f"{self.first_name} {self.last_name}\nTech ID : {self.tech_id}\nMajor: {self.major.major_name}"   
# Degree Audit Class evaluates a student by calculating gpa and percent complete through major.
class Degree_Audit:
    def __init__(self, student: Student):
        self.student = student
        self.requirements = student.major.get_requirements()
        self.grades_to_percentage = {'A' : 4.0, 'B' : 3.0, 'C' : 2.0, 'D' : 1.0, 'F' : 0}
    def get_gpa(self):
        counter = 0
        total = 0
        for requirement in self.requirements:
            if requirement.get_grade() in self.grades_to_percentage.keys():
                counter += 1
                total += self.grades_to_percentage[requirement.get_grade()]
        return total/counter
    def percent_complete(self):
        num_of_requirements = len(self.requirements)
        counter = 0
        for requirement in self.requirements:
            if requirement.has_passed == True:
                counter +=1
        return (counter/num_of_requirements)*100
    def __str__(self):
        return f"{self.student}\nGPA: {self.get_gpa()}\nRequirements Complete: {self.percent_complete():.2f}%"   
# Test 
mnsu_Student = Student("John", "Doe", "012345678910")
mnsu_Student.declare_major(Computer_Science())
mnsu_Student.major.set_requirement_grade("Intro To Programming", 'A')
mnsu_Student.major.set_requirement_grade("Data Structures", 'B')
mnsu_Student.major.set_requirement_grade("Calculus II", 'A')
mnsu_Student.major.set_requirement_grade("Discrete for Comp Sci I", 'F')
mnsu_Student.major.set_requirement_grade("Linear Algebra I", 'D')

print(Degree_Audit(mnsu_Student))