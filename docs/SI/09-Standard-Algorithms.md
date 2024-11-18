# Standard Algorithms

!!! info "What you need to know"

	You must be able to describe, exemplify and implement arrays of records 

## Explanation

You learned three standard algorithms for National 5:

* Input validation
* Running total in a loop
* Traversing an array (simply, looping through each item in the array, one at a time)

For Higher, we add three more standard algorithms:

* Linear search
* Count occurrences
* Find minimum/maximum

All of the above require you to be able to traverse an array.

## Traversing an array in Python - Refresh

=== "Pseudocode"

	```pseudocode linenums="1"
			For loop [counter for the number of elements]
				print element(counter)
			End loop
	```

=== "Python"

	```python linenums="1"
		for counter in range(0, 6):
			print(names[counter])]
	```
 
The linear search and count occurrences algorithms use this existing algorithm, and add an if statement inside the loop. We will cover these first.

For each algorithm, you must be able to:

* Write it in pseudocode
* Write a memorised example in program code, then:
* Write it in the context of a question you’re given, in the exam or assignment

__The first step is to learn/memorise the algorithms; then, you can apply them to unfamiliar contexts.__

## Linear Search 

A linear search is used with one or more arrays of items. We traverse (loop through) the array, looking for a particular value. 

If one of the items in the array matches the search value, we do something.
There are two variations of the algorithm: one simply records if something is found; the other records where in the list it is found. 

It should be clear from a question which one you’re expected to use.

The example below asks for a target (search term the user is looking for). 

* It loops through 10 names. 
* If each name matches the target, it switches the ‘found’ variable to true. 
* At the end of the program, we could know if the name was in the list by checking the value of the found variable.

=== "__Algorithm Example__"

	```pseudocode linenums="1"
		Set found to false
		Input target
  
		For counter from 0 to 9
			If names(counter) == target then
				Set found to true
			End if
		End for loop

	```

=== "__SQA-style Marking Scheme for a Linear Search (4 marks)__"

	``` text
 		* Initialise the variable (1 mark)
 
		* Loop through the elements of the array (1 mark)
		
		* Check if the element matches target (1 mark)
		
		* Set variable to true (1 mark)
	```

### Part Three

=== "Python"

	``` python linenums="1"
		from dataclasses import dataclass
		
		@dataclass
		
		class SchoolReg:
		    Name : str = ""
		    Age : int = 0
		    Reg : str = ""
		
		pupilRecord = [SchoolReg() for x in range (0,3)]
		
		pupilRecord[0].Name = "Peter"
		pupilRecord[0].Age = 17
		pupilRecord[0].Reg = "r1"
		
		print (pupilRecord[0].Name) 
		print (pupilRecord[0].Age) 
		print (pupilRecord[0].Reg) 
	```

=== "Explanation"

	__Line 16 - print(pupilRecord[0].Name)__
	This line tells the computer to print the name of the first student in the list, which is Peter.
 
	__Line 17 - print(pupilRecord[0].Age)__
	This prints the age of the first student in the list, which is 17. 
 
	__Line 18 - print(pupilRecord[0].Reg)__
	Finally, this prints the registration number of the first student, which is "r1".


## Array of Records (efficient method)

### Part One

=== "Python"

	```python linenums="1"
	
		from dataclasses import dataclass
		
		@dataclass
		
		class SchoolReg:
		    Name : str = ""
		    Age : int = 0
		    Reg : str = ""
		
		pupilRecord = [SchoolReg() for x in range (0,3)]
		
		for x in range(len(pupilRecord)):
		   pupilRecord[x].Name = str(input("Enter Name: "))
		   pupilRecord[x].Age = int(input("Enter Age: "))
		   pupilRecord[x].Reg = str(input("Enter Reg: "))
		
		for x in range(len(pupilRecord)):
		    print ("Name: " , pupilRecord[x].Name , "Age: " , pupilRecord[x].Age , "Reg: " , pupilRecord[x].Reg )
	```

=== "Explanation"

	!!! info
 
		Lines 1 - 8 are covered in __Working with Records__.
  
	__Line 12 - for x in range(len(pupilRecord)):__
	The range(len(pupilRecord)) makes the loop go through each student one at a time (three students in this case).
	
	__Line 13 - pupilRecord[x].Name = str(input("Enter Name: "))__
	This line asks the user to type a name for each student using the input() function. Whatever the user types in is stored in the Name variable for each student in the list. For example, the first time the loop runs, it asks for the name of pupilRecord[0].
	
	__Line 14 - pupilRecord[x].Age = int(input("Enter Age: "))__
	This line asks the user to type the student's age. The input() function is used again, and the number typed is stored as the student's age. It’s converted into an integer (whole number). For example, the first time, it will store the age for pupilRecord[0].
	
	__Line 15 - pupilRecord[x].Reg = str(input("Enter Reg: "))__
	This line asks the user to type the student's registration number. The registration number is stored as a string (letters and numbers) for each student. For example, the first time, it stores the registration number for pupilRecord[0].


### Part Two

=== "Python"

	``` python linenums="1"
		from dataclasses import dataclass
		
		@dataclass
		
		class SchoolReg:
		    Name : str = ""
		    Age : int = 0
		    Reg : str = ""
		
		pupilRecord = [SchoolReg() for x in range (0,3)]
		
		for x in range(len(pupilRecord)):
		   pupilRecord[x].Name = str(input("Enter Name: "))
		   pupilRecord[x].Age = int(input("Enter Age: "))
		   pupilRecord[x].Reg = str(input("Enter Reg: "))
		
		for x in range(len(pupilRecord)):
		    print ("Name: " , pupilRecord[x].Name , "Age: " , pupilRecord[x].Age , "Reg: " , pupilRecord[x].Reg )
	```

=== "Explanation"

	__Line 17 - pupilRecord = [SchoolReg() for x in range(0,3)]__
	This is another loop that goes through each student record in the pupilRecord list only this time it’s going to print the details of every student one at a time.
	
	__Line 18 - print("Name: ", pupilRecord[x].Name, "Age: ", pupilRecord[x].Age, "Reg: ", pupilRecord[x].Reg)__
	This line prints out the name, age, and registration number for each student in the list.
	
	!!! example
	
		``` text
			Name: Peter Age: 17 Reg: r1
	  	```
### Array of Records (with Files)

### Part One

=== "Python"

	``` python linenums="1"
		from dataclasses import dataclass
		
		@dataclass
		
		class SchoolReg:
			Name : str = ""
			Age : int = 0
			Reg : str = ""
		
		pupilRecord = [SchoolReg() for x in range (0,3)]
		
		file = open("School-Reg.csv", "r")
	```

=== "Explanation"

	!!! info
 
		Lines 1 - 10 are covered in __Working with Records__.
  
	__Line 12 - file = open("School-Reg.csv", "r")__
	This line opens a file called "School-Reg.csv" in read mode so that we can read from it.

### Part Two

=== "Python"

	``` python linenums="1"	
		from dataclasses import dataclass
		
		@dataclass
		
		class SchoolReg:
		    Name : str = ""
		    Age : int = 0
		    Reg : str = ""
		
		pupilRecord = [SchoolReg() for x in range (0,3)]
		
		file = open("School-Reg.csv", "r")
		
		for i in range(len(pupilRecord)):
		    data = file.readline()
		    data = data.strip("\n")
		    data = data.split(",")
		    pupilRecord[i] = SchoolReg(data[0], int(data[1]), data[2])
	```

=== "Explanation"

	__Line 14__
	A loop that will go through each of the three student records in the pupilRecord list one by one.
	
	__Line 15 - data = file.readline()__
	This line reads one line of data from the file. Each time the loop runs, it reads the next line from the file.
	
	__Line 16 - data = data.strip("\n")__
	This removes the newline character (\n), which is an invisible character at the end of each line in a file. It's like cleaning up the data so there are no extra spaces or jumps to the next line.
	
	__Line 17 - data = data.split(",")__
	This splits the line of data at each comma. Since it's a CSV file, the data for each student is separated by commas. After splitting, we get a list of pieces of information, like the student's name, age, and registration number.
	
	For example, if the line was "Peter,17,r1", after splitting it, we would get:
	
		``` text
			data[0] = "Peter"
			data[1] = "17"
			data[2] = "r1"
		```
	__Line 19 - pupilRecord[i] = SchoolReg(data[0], int(data[1]), data[2])__
	This line takes the pieces of data from the file and creates a SchoolReg object for each student. It fills in the student's name (data[0]), age (data[1]), and registration number (data[2]). The int() function converts the age from a string to a number.

### Part Three

=== "Python"

	``` python linenums="1"	
		from dataclasses import dataclass
		import CSV
		
		@dataclass
		
		class SchoolReg:
		    Name : str = ""
		    Age : int = 0
		    Reg : str = ""
		
		pupilRecord = [SchoolReg() for x in range (0,3)]
		
		file = open("School-Reg.csv", "r")
		
		for i in range(len(pupilRecord)):
		    data = file.readline()
		    data = data.strip("\n")
		    data = data.split(",")
		    pupilRecord[i] = SchoolReg(data[0], int(data[1]), data[2])
		
		for x in range(len(pupilRecord)):
		    print ("Name: " , pupilRecord[x].Name , "Age: " , pupilRecord[x].Age , "Reg: " , pupilRecord[x].Reg )
		    
		file.close()
	```

=== "Explanation"

	__Line 21 - for x in range(len(pupilRecord)):__
	This is another loop. This time, it goes through each student's record in the list and prints out their information.
 
	__Line 22 - print("Name: ", pupilRecord[x].Name, "Age: ", pupilRecord[x].Age, "Reg: ", pupilRecord[x].Reg)__
	This line prints out the student's name, age, and registration number. 
	
	__Line 23 - file.close()__
	This line closes the file after we are finished reading from it.

