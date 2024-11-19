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

__All of the above require you to be able to traverse an array.__

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

    * Initialise the variable (__1 mark__)
 
    * Loop through the elements of the array (__1 mark__)
		
    * Check if the element matches target (__1 mark__)
		
    * Set variable to true (__1 mark__)

    The final mark in the example (__setting the variable to true__) might be replaced with something else, depending on the question. 
    
    For example, you might be asked to find the position of the element.

## Example 1 - Using Found

=== "Python"

	``` python linenums="1"
		# An array of seven names
		names = ["Dopey", "Grumpy", "Doc", "Bashful", "Sneezy", "Sleepy", "Happy"]
		 
		target = input("Enter a name to look for")
		found = False
		
		# Loop through each item
		for counter in range(0,7):
		  # Check each item against the target
		  if names[counter] == target:
		    found = True
		
		# Is the target in the list?
		print("Item was found:", found)

	```

=== "Explanation"

    This program contains a list of names. It asks the user to enter a search target. Then it searches the list of names to see if any of them match the target. 
    
    If they do, it confirms that the target was found.

    At the end of the program, the console should show a message confirming whether the target was in the list.
    
## Example 2 - Using Posistion

=== "Python"

	``` python linenums="1"
		# An array of seven names
		names = ["Dopey", "Grumpy", "Doc", "Bashful", "Sneezy", "Sleepy", "Happy"]
		 
		target = input("Enter a name to look for")
		position = -1
		
		# Loop through each item
		for counter in range(0,7):
		  # Check each item against the target
		  if names[counter] == target:
		    position = counter
		
		# Is the target in the list?
		print("Item was found at position:", position)
	```

=== "Explanation"

    Sometimes, we want to know the position of an element in the array - for instance, the target was found at position 5. This example uses the same basic program as the one above, but instead of reporting whether the name is found, it reports its position.

    We set the starting position to -1. This is because it isn’t possible to be at position -1 in the array. That way, we know that anything other than -1 must mean the item was found, so the position was changed.

    __If, at the end of the program, the value of position was still -1, we would know that the target hadn’t been found.__

## Example 3 - Using Posistion with Parallel Arrays

=== "Python"

	``` python linenums="1"
	# An array of pupil names, and a *parallel* array of marks
	pupils = ["Bob", "Bart", "Krusty", "Mel", "Lisa"]
	marks = [10, 2, 1, 8, 9]
	
	# Ask for a person's name, and print their mark
	target_name = input("Please enter a name:")
	position = -1
	
	# Loop through names
	for counter in range(0, 5):
	  if pupils[counter] == target_name:
	    position = counter
	
	# If we found their name at [position], their mark must also be there
	their_mark = marks[position]

	```

=== "Explanation"

    This program has two arrays: one of pupil names, and one of marks. 
    
    Both arrays have the same number of elements. 
    
    Looking at a name, we can find their mark by going to the corresponding element in the marks array (so the third name corresponds to the third mark). 
    
    The program asks for a target name. 
    
    It loops through the first array, and finds the position where that name is in the list. Later, we can find the corresponding mark, because if the name was found at pupils[position], their mark must be stored at marks[position].

## Count Occurrences

Count occurrences are very similar to linear search:

* The user enters a target/search-term.
  
* The algorithm then searches the array. 

* If the target is found, instead of recording position, it adds +1 to a total/counter. 

By doing this, it counts how often a particular condition is met.

It could also be used to check for an exact match - for example, in a list of names, how many people are called Bob?

However, we could also use it with other conditions:

* In a list of percentages, how many are above 75%?

* In a list of integers, how many are even?

* In a list of letters, how many are upper-case?

!!! warning "Important"

    * Do not confuse __counting occurrences__ with __keeping a running total__: one counts how many of something there are, the other adds them all together.  
    
    * __There might be times when you are asked to do both on the same question.__
    
    * Do not confuse ‘__count__’ or ‘__counter__’ with the loop counter. 
    
    * Your loop counter (e.g. for counter in range...) might use a similar name, e.g. you call one count and the other counter. 
    
    * You could call your loop counter something like “for index in range(0,9)”  to make sure you don’t get confused.

Like a linear search, count occurrences depends on traversing an array. 

There is an if statement inside the array that checks if the element meets the condition and adds +1 to the counter/total if so.

The example below  asks the user to enter a target. It loops through a list of ten names. It checks if each element matches the target. If so, it adds 1 to the count. At the end, it displays how many were found.

=== "__Algorithm Example__"

	```pseudocode linenums="1"
		Set count to 0
  
		Input target
  
		For index from 0 to 9
  
			If names(index) == target then
				
    				Set count to count + 1
    
			End if
   
		End for loop
  
                Display count

	```

=== "__SQA-style Marking Scheme for a Linear Search (4 marks)__"

    * Initialise the count variable  (__1 mark__)
 
    * Loop through the elements of the array (__1 mark__)
		
    * Check if the element matches target (__1 mark__)
		
    * Add 1 to the count variable (__1 mark__)

    The final mark in the example (__setting the variable to true__) might be replaced with something else, depending on the question. 
    
    For example, you might be asked to find the position of the element.


## Example 1 - Using == Sign

=== "Python"

	``` python linenums="1"
		# A list of cars spotted on a road, recorded by make
		cars = ["Ford", "Ford", "Toyota", "Volkswagen", "Kia", "Nissan", "Honda"]
		
		# Ask the user to enter a target
		make = input("Please enter a make:")
		count = 0
		
		for index in range(0, 7):
		  if cars[index] == make:
		    count = count + 1
		
		# Display how many
		print("There were", count, "matching cars")
	```

=== "Explanation"

    This program contains data for cars spotted going down a road at a particular time. 
    
    The programmer wants to be able to find how many Fords, Nissans or Hondas were recorded.

    The user enters a make.

    The program then searches through the list of cars, and if the make matches, it adds 1 to the counter.

    At the end of the program, it shows how many of that make were found.


## Example 2 - Using >= Sign

=== "Python"

	``` python linenums="1"
		# A list of percentages
		percentages = [99.7, 100.0, 52.6, 13.9, 15.2, 88.1, 64.7, 22.5, 71.8]
		
		# How many are at least 50%?
		target = 50.0
		count = 0
		
		for index in range(0, 9):
		  if percentages[index] >= target:
		    count = count + 1
		
		# Show results
		print("There were", count, "values of 50% or more")

	```

=== "Explanation"

    This program contains data for cars spotted going down a road at a particular time. 
    
    The program sets a target of 50.0, and counts how many of the percentages are greater than or equal to the target.

## Example 3 - Odd or Even

=== "Python"

	``` python linenums="1"
		# A list of integers
		numbers = [99, 44, 55, 12, 19, 72, 60, 54, 13, 18, 2, 75]
		
		# Are these odd or even?
		odd_count = 0
		even_count = 0
		
		for index in range(0, 12):
		  if (numbers[index] % 2) == 0:
		    even_count = even_count + 1
		  else:
		    odd_count = odd_count + 1
		
		print("There were", even_count, "even numbers")
		print("and", odd_count, "odd numbers in the list")
	```

=== "Explanation"

    This program has a list of numbers, and counts how many are odd and how many are even, using two counters:

## Finding Minimum & Maximum

The find minimum (find-min) and find maximum (find-max) algorithms are very similar, only differing in whether they use the < or > sign. 

These algorithms would only work on arrays of integers or real numbers (you can’t find the “maximum name” from an array of strings).

For example, below is an array of 10 integers:

<figure markdown="span">
  ![img 1](../Images/Min-and-Max-1.png){ width="800" }
</figure>

To find the maximum (highest) value, we would look through the list one-by-one:

* The first value is 33. We don’t yet know any other values, so 33 must be the highest we’ve found.
  
* The next value is 12. That is less than 33, so we ignore it (it isn’t higher).
  
* The next value is 46. This is higher than 33 (the highest we’ve found so far), so becomes the new highest.
  
* The next value is 18. This is lower than 46 (the current highest found), so we ignore it…

__On that basis, we would find that 49 (element 6) is the highest value in the array.__

=== "__Find Maximum Algorithm__"

		```pseudocode linenums="1"
			Declare a maximum variable, and set it to the first item in the array (e.g. 33)
		
			Loop for each element in the array
		
				If number(counter) > maximum
		  
					Set maximum to number(counter)
				
				End if
				
			End for loop
		```

=== "__Find Minimum Algorithm__"

		```pseudocode linenums="1"
		
			Declare a minimum variable, and set it to the first item in the array (e.g. 33)
			
			Loop for each element in the array
			
				If number(counter) < minimum
			
					Set minimum to number(counter)
				
				End if
		
			End for loop
		```
