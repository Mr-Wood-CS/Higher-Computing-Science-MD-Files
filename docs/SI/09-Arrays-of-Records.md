# Working with Records

!!! info "What you need to know"

	You must be able to describe, exemplify and implement arrays of records 

## Explanation

In Python, an array of records is like a list of boxes, where each box holds important information about a person, place, or thing. 

Each "box" (record) has labelled parts for details, like a name, age, or ID number. 

For example, if we have three students, we can store their name, age, and registration number in three separate __boxes__.

These boxes are part of a record, and we can easily look inside each one to see or change the details. 

## Working with Arrays of Records in Python

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
    ```

=== "Explanation"

	!!! info
 
		Lines 1 - 8 are covered in __Working with Records__.
 
	__Line 10 - pupilRecord = [SchoolReg() for x in range(0,3)]__
	This line creates a list called pupilRecord. A list is like a box where we can store many things. In this case, we are creating two empty student records because the range (0,3) means it will create three spots, one for pupilRecord[0], one for pupilRecord[1] and one for pupilRecord[2].
	
 	__In short, this line says:__
  
	"Make 3 empty student records using the SchoolReg class."

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
		
		pupilRecord[0].Name = "Peter"
		pupilRecord[0].Age = 17
		pupilRecord[0].Reg = "r1"
    ```

=== "Explanation"

	__Line 12 - pupilRecord[0].Name = "Peter"__
	Here, we set the Name of the first student (pupilRecord[0]) to "Peter". Before, it was empty, but now it holds the name "Peter."
 
	__Line 13 - pupilRecord[0].Age = 17__
	Next, we set the Age of the first student (pupilRecord[0]) to 17. Before it was 0, and now it’s set to 17 years old.
 
	__Line 14 - pupilRecord[0].Reg = "r1"__
	Here, we set the registration number (Reg) for the first student to "r1". Now Peter has the registration number "r1".

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


## Array of Records in Python (Efficient  Method)

### Part One

=== "Python"

    ``` python linenums="1"
		from dataclasses import dataclass
	
		@dataclass
		
		class SchoolReg:
		    Name : str = ""
		    Age : int = 0
		    Reg : str = ""
		
		pupilRecord = SchoolReg()
		pupilRecord.Name = "Peter"
		pupilRecord.Age = 17
		pupilRecord.Reg = "r1"
		
		print (pupilRecord.Name) 
		print (pupilRecord.Age) 
		print (pupilRecord.Reg) 
    ```

=== "Explanation"

	__Line 15 - print(pupilRecord.Name)__
	This line tells the computer to print (show) the name of the student, which is "Peter". The computer will display "Peter" on the screen.
	
 	__Line 16 - print(pupilRecord.Age)__
	This prints the student's age, which is 17. The computer will show 17 on the screen.
 
	__Line 17 - print(pupilRecord.Reg)__
	Finally, this prints the student's registration number, which is "r1". The computer will show "r1".







