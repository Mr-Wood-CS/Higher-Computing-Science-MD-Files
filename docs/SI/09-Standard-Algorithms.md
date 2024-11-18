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



