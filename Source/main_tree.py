from tree import Tree,Employees,Plant  # Imported class Tree,class Employee and class Plant  from module tree1.

employees = {}

employee_id = 0

count = 0

print("Welcome To Tree Census Committee")

# Application Loop

while True:
	print("Hey!What Would You Like To Do?\n\n\
		1.Create Employee Account\n\
		2.Login\n\
		3.Exit\n")
	choice=int(input("Enter Your Choice:"))

	if choice == 1:
		
		employee_id = employee_id+1 
		employee_name = input("Enter the name of the employee:")
		employee_gender = input("Enter the gender of the employee:")
		employee_password = input("Enter the password:")

		# Employee id is used as key in the dictionary and name,gender and password as values.
		
		employees[employee_id] = [employee_name,employee_gender,employee_password]  
		
		print("User Details\
			employee_name={}\
			employee_password={}\
			employee_id={}".format(employee_name,employee_password,employee_id))
		continue

	elif choice == 2:
		
		employee_name = input("Enter Your Name:")
		employee_id = int(input("Enter Your Id:"))
		employee_password = input("Enter Your Password:")
		
		if (employees[employee_id][0] == employee_name) and (employees[employee_id][2] == employee_password):
			emp = Employees(employee_name,employee_gender) # Each employee account created is an object.

			# Display the options available.

			while True:
				print("""Welcome!What Would You Like To do?:
					1.Add Tree
					2.Add Plant
					3.Update Census
					4.Exit""")
				choice=int(input("Enter Your Choice:"))

				if choice == 1:
					emp.add_tree()


				if choice == 2:
					emp.add_plant()

				if choice == 3:
					
					# Here ,when a tree or plant is cut down an object is remove so the total count decrement by 1.

					for object in emp.treesandplants:  
						age = input("Enter The Age Of The Tree or Plant:")
						height = input("Enter The Height Of The Tree Or Plant:")
						reason = input("Enter The Reason:")

						
						object.update_census(age,reason,height)
					

				if choice == 4:
				
					break
		else:
			print("Invalid Name or Password!.Try Again")
			
	else:
		break


