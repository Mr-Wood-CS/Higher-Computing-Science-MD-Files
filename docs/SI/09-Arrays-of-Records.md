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
    ```

=== "Explanation"

	!!! info
 
		Lines 1 - 8 are covered in records.
 
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
    ```

=== "Explanation"

	__Line 5 - class SchoolReg__
	Here, we are creating a class called SchoolReg. A class is like a blueprint or recipe. In this case, it helps us create something to store information about a school registration, like a student's name, age, and registration number.
 
	__Line 6 - Name: str = ""__
	Inside the class, we create a variable called Name. This will hold the student's name, and it's a string, which means it's a word or group of letters (like "Peter"). The empty quotes " " mean that we are starting with no name yet.
 
	__Line 7 - Age: int = 0__
	This is another variable called Age. It will hold the student's age, and it's an integer (which means a whole number like 17). Right now, we start it at 0.
 
	__Line 8 - Reg: str = ""__
	This variable is called Reg, which stands for "registration number." It’s also a string (a group of letters or numbers). At first, it's an empty string "", but we will fill it in later.

### Part Three

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
    ```

=== "Explanation"

	__Line 10 -  pupilRecord = SchoolReg()__
	Now we create an object called pupilRecord from the SchoolReg class. Think of the class as a cookie cutter, and this object is a cookie made from it. This object will store a student's name, age, and registration number.
 
	__Line 11 - pupilRecord.Name = "Peter"__
	Here, we set the Name of the pupilRecord object to "Peter". Before it was empty (""), but now it's filled with the name "Peter".
	
 	__Line 12 - pupilRecord.Age = 17__
	Next, we set the Age for pupilRecord to 17. Before, it was 0, but now we know Peter is 17 years old.
	
 	__Line 13 - pupilRecord.Reg = "r1"_
	Here, we set the registration number (Reg) to "r1". Now, the student Peter has a registration number "r1".

### Part Four

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







