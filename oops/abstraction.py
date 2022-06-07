from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name,salary,designation):
        self.name=name
        self.salary=salary
        self.designation=designation

    @abstractmethod
    def performance_management(self):
        pass

    @abstractmethod
    def salary_scale(self):
        pass
    
    def abscence_leave_tracking(self):
        print()
        print("All employees will have 15 causal/sick leaves")
        print("All employees will have 15 earned leaves")

    
#emp1=Employee('Anil',20000,'Technical Specialist')
#emp1.performance_management()
#emp1.salary_scale()
#emp1.abscence_leave_tracking()


class TestEngineer(Employee):
    def performance_management(self):
        print()
        print("Performance evaualtion will be done by the team lead")

    def salary_scale(self):
        print()
        print("1 to 5 years experience people will come under this scale")
        print("salary range is between 3 lacs to 9 lacs ")

    def testcase_writing(self):
        print()
        print("You need to write 5 test cases per day")

print("---------------Test Engineer------------------------")

te1=TestEngineer('Sachin',25000,'Senior Tester')
te1.performance_management()
te1.salary_scale()
te1.abscence_leave_tracking()
te1.testcase_writing()

class TestLead(Employee):
    
    def performance_management(self):
        print()
        print("Performance evaualtion will be done by the team manager")

    def salary_scale(self):
        print()
        print("6 to 8 years experience people will come under this scale")
        print("salary range is between 10 lacs to 15 lacs ")

    def create_test_plan(self):
        print()
        print("Create the test plan based on the requirement")

print("---------------Test Lead------------------------")
tl_1=TestLead('Sunil',70000,'Test Lead')
tl_1.performance_management()
tl_1.salary_scale()
tl_1.abscence_leave_tracking()
tl_1.create_test_plan()
