# IMPORTING LIBRARIES AND MODULES TO BE USED.
import os, Pmw, csv
from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import askinteger, askstring
import sys
import time
from tkinter import ttk

app = Tk()  # instantiating Tk as app.
app.title('EMPLOYEE BOK')

bar = Frame(app, bg='blue').place(relx=0, rely=0)
root = Frame(app, bg='purple').place(relx=0, rely=0.1)

case1 = Frame(root, bg='red').place(relx=0, rely=0.4)
case2 = Frame(root, bg='red').place(relx=0, rely=0.7)

recruitment_frame = Frame(case1, bg='white')

widget1 = Label()
widget1.place(relx=1, rely=1)

admin_mode = False
admin_password = 'SECUREDadmin'


# IN DEVELOPMENT, SECURED AN ENHANCED LOGIN MANAGEMENT
# def encrypt(password):
#     return
# 
# 
# def decrypt(password):
#     return
# 
# 
# def set_password(flag=1):
#     if flag == 0:  # Proceed to create new password without asking for previous password.
#         return
#     else:  # Change password, this function will need the previous password to validate.
#         return


# def get_password():
#     if not admin_password:
#         showinfo(title='Security Centre', message="No Administrator login has been found\n"
#                                                   "Proceed to create an administrator account...")
#         set_password(0)
#         return admin_password
#     else:
#         password = decrypt(admin_password)
#         return password


def setMode():
    """ Set the application to either admin or employee mode."""
    global admin_mode
    question = askyesno(title="EMPLOYEE BOOTH", message="Employee Login or Administrator Login ?")
    if question:
        while True:
            prompt = askstring(title="Security Centre", prompt="Enter Administrator password "
                                                               "to access admin privileges")
            if prompt == admin_password:
                showinfo(message="Administrator login completed/ Switching to admin mode")
                admin_mode = True
                return
            if prompt == None:
                return
            else:
                showerror("Security Centre", "Incorrect Password ")
    else:
        admin_mode = False
        return


def show(widget2):
    global widget1
    widget1.place_forget()
    widget2.place(relx=0, rely=0)
    widget1 = widget2


setMode()

Pmw.initialise()
Pmw.aboutversion(2.8)
Pmw.aboutversion('1.5')
Pmw.aboutcopyright('Copyright LumenTexch 2021\nAll rights reserved')
Pmw.aboutcontact(
    'For information about this application contact:\n' +
    ' Sales at Lumen Texch\n' +
    ' Phone: 0903-3831-610\n' +
    ' email: shittuoluwaseyi777@gmail.com'
)
about = Pmw.AboutDialog(case1, applicationname='ABOUT APPLICATION')
about.withdraw()


def hide_about(e):
    about.withdraw()


about.bind("<Button-1>", hide_about)


class Work:
    def __init__(self, title, point=0, worker_id='', status=''):
        self.title = title
        self.worker = 'None YET'
        if point != 0:
            self.point = int(point)
            self.worker_id = worker_id
            self.status = status
        else:
            self.point = askinteger(title='Centre of Works', prompt="Enter work point")
            self.worker_id = ''
            self.status = 'pending'


    def __repr__(self):
        return f"Job name: {self.title}, Work point{self.point}. Assigned to {self.worker}, Status: {self.status}\n"

class EmployeeList:
    def __init__(self):
        self.employees = []
        self.male_employees = []
        self.female_employees = []
        self.f_ratio = IntVar()
        self.m_ratio = IntVar()
        self.labour_force = 0
        self.id_list = []
        self.id_length = 1
        self.work = []
        self.work_num = 0
        self.work_pending = []
        self.work_in_progress = []
        self.work_fin = []
        self.work_load = 0
        self.workers_load = 0
        self.work = []
        self.salary_budget = 0
        self.graph1 = Scale(root, label='MALE RATIO', var=self.m_ratio, from_=0, to=100, background='white',
                            sliderrelief=FLAT, troughcolor='red', orient=VERTICAL, state=DISABLED).place(relx=0.8,
                                                                                                         rely=0.2)
        self.graph2 = Scale(root, label='FEMALE RATIO', var=self.f_ratio, from_=0, to=100, background='white',
                            sliderrelief=FLAT, troughcolor='blue', orient=VERTICAL, state=DISABLED).place(relx=0.9,
                                                                                                          rely=0.2)

    def add_employee(self, id_num='', First_name='', Last_name='',Gender='', Age=18, Rank="Junior Staff", Salary=0, Join_date='',
                     Bonus=[], flag=True):
        if flag == False:
            Num = id_num
            self.id_length += 1
            Employee(First_name, Last_name, Num, Gender, Age, rank=Rank, salary=Salary, join_date=Join_date, bonus=Bonus, flag=False)
            return
        name = askstring(title='HUMAN RESOURCE', prompt="Kindly enter employee's first name")
        num = ''  # VARIABLE FOR NEW EMPLOYEE IDENTIFICATION NUMBER.
        # THE NEXT 7 LINES GENERATES A SUITABLE IDENTIFICATION NUMBER WITH MINIMUM OF THREE CHARACTERS.
        length = self.id_length
        if length < 9:
            num = f"emp-00{length}"
        elif 9 < length < 99:
            num = f"emp-0{length}"
        else:
            num = f"emp-{length}"
        self.id_length += 1
        Employee(first_name = name, generated_id=num)  # CALLING AN INSTANCE OF EMPLOYEE CLASS WITH TAILORED NAME AND IDENTIFICATION NUMBER.

    def print_employees(self):
        if not self.employees:
            return showwarning(title='HUMAN RESOURCE', message='You currently have no employee')
        workers = 'The following are your staff:\n '
        sn = 0
        for emp in self.employees:
            sn += 1
            workers += f"{sn}. {emp}\n"
        showinfo(title='HUMAN RESOURCE', message=str(workers))

    def print_male_staff(self):
        if not self.male_employees:
            return showwarning(message="you currently do  not have any female employee")
        workers = 'The following are your male staff: \n'
        sn = 0
        for emp in self.male_employees:
            sn += 1
            workers += f"{sn}. {emp} \n "
        showinfo(title='HUMAN RESOURCE', message=workers)

    def print_female_staff(self):
        if not self.female_employees:
            return showwarning(message="you currently do  not have any female employee")
        workers = "The following are your female staff:\n"
        sn = 0
        for emp in self.female_employees:
            sn += 1
            workers += f"{sn}. {emp}\n "
        showinfo(title='HUMAN RESOURCE', message=workers)

    def plabour_force(self):
        showinfo(title='CENTRE OF WORKS', message=f"Total number of employees is {self.labour_force}")

    def add_work(self, title='', point=0, worker_id='', status=''):
        if title:
            work = Work(title, point, worker_id, status)
            self.work_pending.append(work)
            self.work.append(work)
            self.work_load += work.point
            self.work_num += 1
            return
        Title = askstring(title='WORK CHAMBER', prompt="Input the work title")
        work = Work(Title)
        work.status = 'pending'
        self.work_pending.append(work)
        self.work.append(work)
        self.work_load += work.point
        self.work_num += 1
        showinfo(title='WORK CHAMBER', message='Work added')

    def assign_work(self,task='',flag=True):
        if flag == False:
            for emp in self.employees:
                if emp.id_num == task.worker_id:
                    staff = emp
            task.worker = emp
            self.work_in_progress.append(task)
            staff.work_todo.append(task)
            staff.work_load += task.point
            task.worker = staff
            self.workers_load += task.point
            task.status = 'in_progress'
            return
        if not self.work_pending:
            return showerror(message='There is currently no idle task \n consider adding work?')
        if self.labour_force < 1:
            return showerror(message="Employee not Available")
        sn = 0
        txt = ''
        for work in self.work_pending:
            sn += 1
            txt += f"{sn}. {work}\n"
        choice1 = askinteger(title='WORK CHAMBER', prompt=f'Which work is to be assigned?\n {txt}') - 1
        task = self.work_pending.pop(choice1)
        workers = ''
        sn = 0
        for emp in self.employees:
            sn += 1
            workers += f"{sn}. {emp}\n"
        choice2 = askinteger(title='CHAMBER OF EMPLOYEES & WORKS', prompt=f'Which staff is to be assigned the task\n'
                                                                          f'{workers}') - 1
        staff = self.employees[choice2]

        self.work_in_progress.append(task)
        staff.work_todo.append(task)
        staff.work_load += task.point
        task.worker_id = staff.id_num
        task.worker = staff
        self.workers_load += task.point
        task.status = 'in_progress'
        showinfo(title='CHAMBER OF EMPLOYEES & WORKS',
                 message=f"SUCCESS! the task '{task.title}' has been assigned to {staff}")

    def get_workstatus(self):
        var = ('has', '')  # VERB TUPLE.
        completed = len(self.work_fin)
        if completed > 1:
            var = ('have', 's')  # CHANGING THE VERBS TO OBEY CONCORD.
        showinfo(title='CHAMBER OF WORKS', message=f'{completed} task{var[1]} {var[0]} been completed out of '
                                                   f'{self.work_num}')

    def show_completed_work(self):
        """

        :return: all finished tasks.
        """
        if not self.work_fin:
            return showinfo(message='No task has been completed')
        txt = ''
        sn = 0
        for work in self.work_fin:
            sn += 1
            txt += f"{sn}. {work}"
        showinfo(title="CENTRE OF WORKS", message=f'Below is a list of all completed work\n{txt}')

    def show_pending_work(self):
        """
        checks for all tasks that are yet to be assigned to an employee nor have been completed.
        :return: all pending task
        """
        if not self.work_pending:
            return showinfo(message='There is no idle task\n consider adding one?')
        sn = 0
        txt = ''
        for work in self.work_pending:
            sn += 1
            txt += f"{sn}. {work}"
        showinfo(title='CENTER OF WORKS', message=f'Below is a list of all pending work\n{txt}')

        return

    def finished_work(self,task='',flag=True):
        """
        checks for tasks that are yet to completed but have been assigned and updates the task status to completed.
        """
        if flag == False:
            self.work_in_progress.remove(task)
            self.work_fin.append(task)
            task.status = 'completed'
            return
        if not self.work_in_progress:
            return showwarning(title="CENTRE OF WORKS", message='There is currently no work in progress')
            # STOPS EXECUTION IF THERE IS NO WORK IN PROGRESS AS THERE WON'T BE A TASK TO BE UPDATED AS COMPLETED.
        while True:
            sn = 0
            txt = ''
            for work in self.work_in_progress:
                sn += 1  # TO MAKE THE SERIAL NUMBER START FROM 1 INSTEAD OF 0, SEE LINE 242.
                txt += "%d. %s.\n" % (sn, work)
            choice = askinteger(title='Work Chamber',
                                prompt=f"Below is a list of work in progress\n{txt}\nWhich of the following task "
                                       f"have been completed ?")
            choice -= 1  # TO COMPENSATE FOR THE FACT THAT PYTHON INDEX STARTS FROM ZERO AND ALSO LINE 237.
            if choice in range(sn):
                completed = self.work_in_progress.pop(choice)
                self.work_fin.append(completed)
                completed.status = 'completed'
                return showinfo(message=f"The task'{completed}' has been completed by {completed.worker}.")
            else:
                return showerror(message="Invalid Selection")

    def mvp(self):
        """
        calculates for the employee with highest task points and therefore most vital.
        :return:
        """
        if self.labour_force == 0:  # STOP EXECUTION IF THERE IS NO EMPLOYEE.
            return showinfo(message="No Employee")
        if self.workers_load == 0:  # STOP EXECUTION IF NO EMPLOYEE HAS BEEN ASSIGNED A TASK.
            return showwarning(message="None of your employee has performed any task")
        y = 0
        mvp = ''
        for emp in self.employees:
            if emp.work_load > y:
                y = emp.work_load
                mvp = emp
        per = (y / self.work_load) * 100
        showinfo(title='CHAMBER OF WORKS AND EMPLOYEES',
                 message=f"{mvp} is the MVP with a workload of {y} out of{self.work_load} ({per}%)")

    def ratio(self):
        """
        calculating the ratio of make and female employees.
        :return: a graph depicting the ratio.
        """
        total = self.labour_force
        if total < 1:
            self.f_ratio.set(0)
            return self.m_ratio.set(0)
        male_ratio = len(self.male_employees)
        female_ratio = len(self.female_employees)
        if male_ratio == total:
            self.f_ratio.set(0)
            return self.m_ratio.set(100)
        elif female_ratio == total:
            self.m_ratio.set(0)
            return self.f_ratio.set(100)

        else:
            self.m_ratio.set((male_ratio / total) * 100)
            self.f_ratio.set((female_ratio / total) * 100)
            return


EMPL = EmployeeList()


class Employee:
    def __init__(self, first_name, last_name='', generated_id='', gender='', age=18, rank=1, salary=0, join_date='',
                 bonus=[], flag=True):
        if flag == False:
            self.first_name = first_name
            self.last_name = last_name
            self.gender = gender
            self.id_num = generated_id
            self.work_load = 0
            self.work_todo = []
            self.salary = salary
            self.bonus = bonus
            self.date_employed = join_date
            self.age = age
            self.rank = rank

            EMPL.employees.append(self)
            EMPL.labour_force += 1
            if self.gender == 'male':
                EMPL.male_employees.append(self)
            elif self.gender == 'female':
                EMPL.female_employees.append(self)
            EMPL.id_list.append(self.id_num)
            EMPL.ratio()
            return
        recruitment_frame.place(relx=0.3, rely=0.3)
        self.first_name = ''
        self.name = ''
        self.gender = ''
        self.id_num = generated_id
        self.work_load = 0
        self.work_todo = []
        self.f_name = StringVar()
        self.l_name = StringVar()
        self.g = StringVar()
        self.f_name.set(first_name)
        self.salary = 0
        self.bonus = {}
        self.date_employed = 2021
        self.age = 0
        self.rank = 1

        Label(recruitment_frame, text='FIRST NAME :').grid(row=0, column=1)
        Entry(recruitment_frame, textvar=self.f_name, state='disabled').grid(row=0, column=2)
        Label(recruitment_frame, text='LAST NAME :').grid(row=1, column=1)
        Entry(recruitment_frame, textvariable=self.l_name).grid(row=1, column=2)
        Label(recruitment_frame, text='GENDER :').grid(row=2, column=0)
        Radiobutton(recruitment_frame, text='Male', value='male', variable=self.g).grid(row=2, column=1)
        Radiobutton(recruitment_frame, text='Female', value='female', variable=self.g).grid(row=2, column=2)
        self.g.set('male')

        Label(recruitment_frame, text='ID :').grid(row=3, column=1)
        en3 = Entry(recruitment_frame, bg='green', foreground='red', takefocus=0, text=f'{self.id_num}')
        en3.grid(row=3, column=2)
        Button(recruitment_frame, text='Employ!', command=self.employ).grid(row=4, columnspan=2, sticky=NSEW)

    def __repr__(self):
        return f"Name: {self.first_name} {self.last_name} ID:{self.id_num}"

    def employ(self):
        self.first_name = self.f_name.get()
        self.last_name = self.l_name.get()
        self.gender = self.g.get()
        EMPL.employees.append(self)
        EMPL.labour_force += 1
        if self.gender == 'male':
            EMPL.male_employees.append(self)
        elif self.gender == 'female':
            EMPL.female_employees.append(self)
        EMPL.id_list.append(self.id_num)
        showinfo(title='EMPLOYEE CHAMBER', message='Employee added')
        recruitment_frame.place_forget()
        EMPL.ratio()

    def data(self):
        message = f"NAME: {self.first_name} {self.last_name} \nIDENTIFICATION NUMBER: {self.id_num} \n" \
                  f"AGE: {self.age} \nRANK :{self.rank} \nDATE EMPLOYED: " \
                  f"SALARY: {self.salary} \nCOMPANY'S WORKLOAD : {(self.work_load / EMPL.work_load) * 100}%\n" \
                  f"SUGGESTED YEAR OF RETIREMENT :{self.age - 60}years"


employee_chamber1 = [('ADD EMPLOYEE', EMPL.add_employee), ('SHOW ALL EMPLOYEES', EMPL.print_employees),
                     ('SHOW ALL FEMALE EMPLOYEES', EMPL.print_female_staff),
                     ('SHOW ALL MALE EMPLOYEES', EMPL.print_male_staff),
                     ('GET WORKFORCE SIZE', EMPL.plabour_force), ('SHOW MVP', EMPL.mvp)]

work_chamber1 = [('ADD WORK', EMPL.add_work), ('ASSIGN TASK', EMPL.assign_work),
                 ('UPDATE TASK', EMPL.finished_work), ('SEE UNCOMPLETED TASKS', EMPL.show_pending_work),
                 ('SHOW COMPLETED TASKS', EMPL.show_completed_work)]
# RESTRICTING WIDGETS AVAILABLE WHEN ADMIN MODE IS OFF
employee_chamber2 = [('SHOW ALL EMPLOYEES', EMPL.print_employees),
                     ('GET WORKFORCE SIZE', EMPL.plabour_force), ('SHOW MVP', EMPL.mvp)]
work_chamber2 = [('SEE UNCOMPLETED TASKS', EMPL.show_pending_work),
                 ('SHOW COMPLETED TASKS', EMPL.show_completed_work)]

buttonBoxE = Pmw.ButtonBox(case2, labelpos='nw', label_text='HUMAN RESOURCE:')
buttonBoxW = Pmw.ButtonBox(case2, labelpos='nw', label_text='CENTRE OF WORKS:')

if admin_mode:
    for txt, cmd in employee_chamber1:
        buttonBoxE.add(componentName=txt, command=cmd)
        
    for txt, cmd in work_chamber1:
        buttonBoxW.add(componentName=txt, command=cmd)
else:
    for txt, cmd in employee_chamber2:
        buttonBoxE.add(componentName=txt, command=cmd)

    for txt, cmd in work_chamber2:
        buttonBoxW.add(componentName=txt, command=cmd)


buttonBoxE.place(relx=0.01, rely=0.2)
buttonBoxW.place(relx=0.01, rely=0.5)

def store():
    # STORING EMPLOYEES DATA
    with open('storage_file1.csv', mode='w') as file1:
        employee_fields = ('id', 'first name', 'last name', 'gender', 'age', 'rank', 'salary',
                           'join date','bonus')
        writer = csv.DictWriter(file1, fieldnames=employee_fields)
        # First line of the csv file as csv_fields.
        writer.writeheader()
        for emp in EMPL.employees:
            dic = {'id': emp.id_num, 'first name': emp.first_name, 'last name':emp.last_name, 'gender': emp.gender, 'age': emp.age,
                   'rank': emp.rank,
                   'salary': emp.salary, 'join date': emp.date_employed,'bonus': emp.bonus}
            writer.writerow(dic)
    # STORING WORK DATA.
    with open('storage_file2.csv', mode='w') as file2:
        work_fields = ('Title', 'Point', 'Worker_id', 'Status')
        writer = csv.DictWriter(file2, fieldnames=work_fields)
        writer.writeheader()
        for work in EMPL.work:
            dic = {'Title': work.title, 'Point': work.point, 'Worker_id': work.worker_id, 'Status': work.status}
            writer.writerow(dic)


def recover():
    if not os.path.isfile('storage_file1.csv') and not os.path.isfile('storage_file2.csv'):
        open('storage_file1.csv', 'w')
        open('storage_file2.csv', 'w')
        return
    with open('storage_file1.csv', mode='r') as file1:
        csv_reader = csv.DictReader(file1)
        for row in csv_reader:
            EMPL.add_employee(id_num=row['id'], First_name=row['first name'], Last_name=row['last name'], Gender=row['gender'],
                              Age=row['age'],Rank=row['rank'],Salary=row['salary'], Join_date=row['join date'],
                              Bonus=row['bonus'], flag=False)

    with open('storage_file2.csv', mode='r') as file2:
        csv_reader = csv.DictReader(file2)
        line_count = 0
        for row in csv_reader:
            EMPL.add_work(title=row['Title'], point=row['Point'], worker_id=row['Worker_id'], status=row['Status'])
        for work in EMPL.work_in_progress:
            if work.status == "completed":
                EMPL.assign_work(task=work,flag=False)
                EMPL.finished_work(task=work,flag=False)
            elif work.status == "in progress":
                EMPL.assign_work(task=work,flag=False)
    return


def Exit(event=None):
    store()
    # app.destroy()
    sys.exit()


help_verb = 'on'


def help_mode():
    return


def show_about():
    return about.show()


menubar = Menubutton(bar, text='help', underline=0)
menubar.adder = Menu(menubar)
menubar.adder.add_command(label=f"toogle {help_verb} help mode", command=help_mode)
menubar.adder.add_command(label="contact", command=show_about)
menubar['menu'] = menubar.adder

# CREATING MENU ITEMS.
Label(bar, text="CURRENT STATE: (CHAMBER)", bg='purple').grid(row=0, column=0)
Label(bar, text='GO TO: CHAMBER', bg='purple').grid(row=0, column=1)
Label(bar, text='CHANGE MODE', bg='purple').grid(row=0, column=2)
Label(bar, text='', bg='purple').grid(row=0, column=3)
menubar.grid(row=0, column=4)
Button(bar, text='Save', command=store).grid(row=0, column=5)
Button(bar, text='Exit', command=Exit, bg='red').grid(row=0, column=6)

recover()
EMPL.ratio()
app.mainloop()

"""MERRY CHRISTMAS"""
