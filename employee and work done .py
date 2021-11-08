class EmployeeList(object):
    def __init__(self):
        self.employees = []
        self.work_todo = []
        self.assigned_task = []
        self.work_fin = []
        self.work = self.work_todo + self.assigned_task + self.work_fin
        self.work_load = 0
        self.male_employees = []
        self.female_employees = []
        self.work_force = 0
    def __str__(self):
        while True:
            print('Select a number')
            methods = self.employees,self.work_force,self.work_todo,self.assigned_task,self.work_fin,self.work,
            print("1. Show all employees \n2. Display number of employees.\n3. Show all un assigned work."
                  "\n5. Show all completed work. \n6. Get a list of all work")
            choice = int(input('Pick a number ;'))
            if type(choice) is not int or choice not in range(1,7):
                print('Invalid Selection')
                continue
            pick = methods[choice]
            return str(pick)

    def add_male_employees(self,emp):
        self.male_employees.append(emp)

    def add_female_employees(self, emp):
        self.female_employees.append(emp)

    def add_work(self):
        work_title = input("Input the work title :")
        self.work_todo.append(work_title)
        self.work.append(work_title)
        self.work_load +=1

    def pwork_done(self):
        print('Below is a list of all completed work')
        i = 1
        for work in self.work_fin:
            print(f"{i}. {work}")
            i += 1

    def pemployees(self):
        print('The following are your staff')
        sn = 0
        for emp in self.employees:
            sn += 1
            print(f'{sn}. {emp}')

    def p_m_employees(self):
        print('The following are your male staff')
        sn = 0
        for emp in self.male_employees:
            sn += 1
            print(f'{sn}. {emp}')

    def p_f_employees(self):
        print('The following are your female staff')
        sn = 0
        for emp in self.female_employees:
            sn += 1
            print(f'{sn}. {emp}')

    def pwork_force(self):
        print(f"Total number of employees is {self.work_force}")

    def pwork_todo(self):
        print('Below is a list of all pending work:')
        for work in self.work_todo:
            print(work)

    def finished_work(self):
        while True:
            num = 0
            for work in self.work:
                num +=1
                print("%d. %s"%(num,work))
            choice = int(input("Which of the following task have been completed\nSelect by number :"))
            pick = num+1
            if choice  in range(pick):
                deleted = self.work.pop(pick)
                self.work_fin.append(deleted)
                return f"The task'{deleted}' has been completed."
            else:
                print("Invalid Selection")
                return

    def add_employee(self):
        name = input("Please input the name of this employee :")
        name = Employee(name)
        self.employees.append(name)
        self.work_force +=1

    def pick_pfunc(self):
        while True:
            print("Enter a number to perform one of the following task\n1. To get details on employees or add employees.\n"
                  "2. For work related issues.\n0. To exit")
            side = int(input('Enter your Choice :'))
            if side == 1:
                print("(EMPLOYEES CHAMBER)")
                while True:
                    print('Enter a number to perform one of the following task: \n1. Get a list of all employees \n'
                          '2. Add a new employee.\n3. Show all male employees. \n'
                          '4. Show all female employees.\n5. Get total number of employees.'
                          '\n9. To go back to previous selection')
                    enter = int(input('Enter a number:'))
                    if enter not in range(1,6) and enter != 9:
                        print('Invalid input')
                        continue
                    elif enter == 9:
                        break

                    elif enter == 1:
                        self.pemployees()
                        continue
                    elif enter == 2:
                        self.add_employee()
                        continue
                    elif enter == 3:
                        self.p_m_employees()
                        continue
                    elif enter == 4:
                        self.p_f_employees()
                        continue
                    elif enter == 5:
                        self.pwork_force()
                        continue
                    else:
                        print('Input not recognized')
                        continue

            elif side == 2:
                print("(WORK CHAMBER)")
                while True:
                    print("Enter a number to perform one of the following task: \n1. Update a work as completed.\n"
                          "2. Add a new work.\n3. Show all uncompleted work \n9. To go back to previous selection")
                    enter2 = int(input('Enter a number :'))
                    if enter2 not in range(1,4) and enter2 != 9:
                        print("Invalid input\nEnter a valid option(from 1 to 4)")
                        continue
                    elif enter2 == 9:
                        break
                    elif enter2 == 1:
                        self.finished_work()
                        print('Work progress updated')
                        continue
                    elif enter2 == 2:
                        self.add_work()
                        print("Work added")
                        continue
                    elif enter2 == 3:
                        self.pwork_todo()
                        continue
                    else:
                        print("Invalid input\nEnter a valid option(from 1 to 4)")
                        continue

            elif side == 0:
                break
            else:
                print("INVALID INPUT, Try again")
                continue








EMPL = EmployeeList()

class Employee():
    def __init__(self, name):
        self.name = name
        while True:
            path = input("What is %s's gender?\n reply M for male and F for female:-" % self.name).lower()
            if path == 'm' :
                self.gender = 'Male'
                self.pronoun = 'his'
                EmployeeList.add_male_employees(self=EMPL,emp=name)
                break
            elif path == 'f':
                self.gender = 'Female'
                self.pronoun = 'her'
                EmployeeList.add_female_employees(self=EMPL,emp=name)
                break
            elif self.gender != 'm' and self.gender != 'f':
                print("Invalid input")
                continue
        id_length: int = EMPL.work_force + 1
        if id_length < 9:
            self.id_num = "00%d" % id_length
        elif 9 < id_len < 99:
            self.id_num = "0%d"% id_length
        print("%s's ID number is %s"%(self.name,self.id_num))
        print(f"Would you like to immediately assign a work to {self.name}")
        choice = input("Enter Yes or No :").lower()
        if choice == 'yes':
            self.work_todo = input(f"Assign a work to %s :"%self.name)
    def __str__(self):
    	return "%s with ID number %s"%(self.name, self.id_num)

EMPL.pick_pfunc()
