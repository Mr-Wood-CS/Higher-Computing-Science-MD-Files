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

Once we have read each line from the file, we split the line into its constituent parts.

We use the split() function to separate each line, passing as a parameter the character we want to split with (usually a comma). 

Based on the first row of the table above, the following code would print “1027”.
</br>
</br>

!!! example

	```Python
		# Split the line based on commas, and store in an array
		values = firstline.split(",")
		print(values[2]) 
	```
 
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


