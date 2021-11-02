# Classifying employes,Keeping track of names and work they have done. 
Employees = {"Boss": 0 }
work_todo = {"Manage": "Boss"}
work_fin = [""]
check_emp = []
work=[]
	# This function is to check if employyes name is already in the dictionary. If it isnt it makes a new key, and adds a value.
def add_employ():
	print("Please input the name of an Employee.")
	new_emp = input(">")
	for i in Employees:	
		check_emp = i
		
	if new_emp in check_emp :
		print("This employee is already in the system.")
	else:
		employ_num = (input("whats the Employees number. \n >"))
		Employees[new_emp] = employ_num
	employees = Employees.items()
	for existing_emp in employees:
		print (existing_emp)
	return
# This function is to add work to the todo dictinary. and check to see of the work is in there. 
def add_work():
	print("Please print what work you want to add to the list. ")
	work_load= input(">")
	for cwork in work_todo :
		work = cwork
	if work_load in work:
		print ("This work already has been assigned to someone.")
		print (work_todo[work])
	elif work_load != work:
		print("Work load has been added. \n What employee do you want to do the work?")
		emp_dowork= input(">")
		work_todo[work_load] = emp_dowork
		print(f"Employee {emp_dowork} has been assigned {work_load}.")
	Work_todo = work_todo.items()
	for exist_work in Work_todo:
		exist_work = exist_work
	return
	
#This function is to delete the work from todo so we can switch it over to work done
def delete_work():
	listwork = work_todo.items()
	for existwork in listwork:
		existwork = existwork
	print("Please input what work has been completed. Here is a list of current ongoing work.")
	print(existwork) 
	workto_del = input ("What task has been done? \n >")
	if workto_del in work_todo:
		work_fin.append(workto_del)
		try:
			del work_todo [workto_del]
			print(f"{workto_del} has been deleted.")
		except keyerror :
				print ("Workload is not in list.")
				
# when typed will give lists of dic and loop.
	return
def pwork_done():
	print("Here is a list of work done ")
	print(work_fin)
	return
def pemployees():
	print("Here is a list of employyes.")
	print(Employees)
	return
def pwork_todo():
	print("Here is a list of work to be done")
	print (work_todo)
	return
#function if a letter was pressed pick one of the print options 
def pick_pfunc():
	puser_input = input("Please type ' what work is done.' to see work done.\n Type 'Employees' to see a list of Employees\n Type 'work todo' to show What work is left.\n >").lower()
	if puser_input == "what work is done".lower():
		pwork_done()
	elif puser_input == "Employees".lower():
		pemployees()
	elif puser_input == "work todo".lower() or "work to do".lower():
		pwork_todo()
	return
# loop function. To loop it all together.
def loop_all() :
	loop = True
	while loop == True:
		user_inpput = input ("if you would like to add or edit lists for workers and work to do. Please type 'Edit'.\n If you want to just veiw the listing. please type 'View'. \n If you want to exit this application click ' x ' \n >").lower()
		if user_inpput == "edit".lower():
			pick_task()
		elif user_inpput == "view".lower():
			pick_pfunc()
		elif user_inpput == "x".lower():
			loop = False
			break
		else:
			print("Not a valid input.")
	return
		



# lets user pick tasks to be done.
def pick_task():
	print ("Please type 'add employee, if you want to add a new worker. \n Please type 'add work to do' if you want to give work to an employee. \n Please type 'delete work' If you want to delete work.")
	print_task = input(">").lower()
	if print_task == "add work to do".lower():
		add_work()
	elif print_task == "add employee".lower():
		add_employ()
	elif print_task == "delete work".lower():
		delete_work()
	else: 
		print("Input not accepted. Please input the proper terms.")
	return





loop_all()

