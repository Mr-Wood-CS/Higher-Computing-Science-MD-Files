# Working with Files

<div class="grid cards" markdown>
- :fontawesome-brands-python: [Glazing-Company](../Static/5.2-Glazing-Company.py){:download="Glazing-Company.py"}
- :fontawesome-brands-python: [Glazing-Company](../Static/Golf-Championship.py){:download="Golf-Championship.py"}
</div>

Golf-Championship

## Explanation

CSV stands for Comma Separated Values and is a format usually associated with importing and exporting from spreadsheets and databases.

It allows greater control over the data than a simple text file, as each row is split up into identifiable columns. 

Below is an example of how the data is stored:

| Name  | Age | Reg Number |
| :---: | :--:| :----------:
| Peter | 17  | r1         |
| Laura | 16  | r1         |
| Marie | 16  | r1         |
	
A .csv file would store the above data as:

```txt
	Peter, 17, r1
	Laura, 17, r1
	Marie, 16, r1
```
It may be easier to think of the data as being separated into columns and rows that use an index to identify them:

| Name  | Age | Reg Number |
| :---: | :--:| :----------:
| Peter | 17  | r1         |
| Laura | 16  | r1         |
| Marie | 16  | r1         |


When opening a .csv file to use, you must first specify how that file will be used.

The options are:

`Write`

:   "w" (write Mode) creates a new file and writes to that file. If the file already exists, a new file will be created, overwriting the existing file.

: !!! example
	```Python
		# This must be at the top of your program to allow Python to use the csv libary of commands.
		import csv
		
		# Create a new file called "School-Reg.csv", overwriting any previous files of the same name.
		file = open("School-Reg.csv", "w")
		
		# Add 3 new records to the file
		newRecord1 = ("Peter,17,r1 \n")
		newRecord2 = ("Laura,17,r1 \n")
		newRecord3 = ("Marie,16,r1 \n")
	```

`Cras arcu libero`

:   Aliquam metus eros, pretium sed nulla venenatis, faucibus auctor ex. Proin
    ut eros sed sapien ullamcorper consequat. Nunc ligula ante.

    Duis mollis est eget nibh volutpat, fermentum aliquet dui mollis.
    Nam vulputate tincidunt fringilla.
    Nullam dignissim ultrices urna non auctor.
## Complete example
This example uses the table above. It reads in the data, and finds the names and towns of the schools. If you wanted to print this data (or otherwise use it), you could do so using the parts[] array or name/town variables.

!!! example

	```Python
		# Open the file for reading
		schoolfile = open("Schools.txt", "r")
		
		# Read in the data one line at a time
		lines = schoolfile.readlines()
		
		# Loop through the schools, one at a time
		for counter in range(0, 3):
		   school = lines[counter]
		   parts = school.split(",")
		   name = parts[0]
		   town = parts[1]
		
		# Close the file
		schoolfile.close()
	```


## Types of Variables

In programming variables have a particular type and for National 5 there are five data types that you need to know:



!!! warning

    Once a variable has been set up with a particular type, you can only assign it data of that type.


!!! example
	```Python
	# This is an integer
	myage = int(15)

	# This is a real number
	price = float(0.99)

	# This is a string
	faveSubject = str("Computing")

	# This is a character
	firstInitial = char("F")

	# This is a Boolean
	isStudent = bool(1)
	```

## Calculations

Python programs will often carry out calculations with operators. The result is usually stored in a variable:

!!! example
```Python
num1 = 5
num2 = 7
sum = num1 + num2
```

You can use the following operators:

!!! example
	```Python
	# Three variables
	num1 = 5
	num2 = 7
	sum = 0.0

	# Addition
	sum = num1 + num2

	# Subtraction
	sum = num1 - num2

	# Division
	sum = num1 / num2

	# Multiplication
	sum = num1 * num2

	# Raise to a power
	sum = num1 ** num2

	#Note that “raising to the power” means, for example, num1**num2. 

	#To square or cube a number, you would say:
	square = num1 ** 2
	cube = num1 ** 3
	```

## String Concatenation

String concatenation is the term used when **joining** two strings.

!!! example
	```Python
	word1 = “Hello”
	word2 = “World”

	sentence = word1 + word2
	```

!!! tip

    The example above doesn’t include a space, you would have to add a space to the end of **“Hello”** or the beginning of **“World”**. 


