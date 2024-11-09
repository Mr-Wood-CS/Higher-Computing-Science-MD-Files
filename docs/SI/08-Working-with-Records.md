# Working with Records

!!! info "What you need to know"

	You must be able to describe, exemplify and implement records 

## Explanation

So far, we’ve used only one type of data structure to store multiple values: the array. 

Remember, an array is like a list of related variables that all share the same data type. For example, an array could store a list of numbers or a list of names, but not both.

While arrays can only hold one type of data, records allow us to store different types of data together in a single structure. For example, one record can store a name (string), an age (integer), and a status (Boolean) all in one place.

Just like in a database, records help us organize related information more efficiently.

By using records, we can keep all related data about a single person or object together in one structure, and we can use real-world names for each category (called fields) to make the data easier to understand and manage. 

__This is especially useful because most systems we work with, like databases, organize data in this way.__

## Record Structure

A record structure is like creating your own custom data type. 

As a programmer, you define a record with a name that represents something real, like "Student" or "Product" and specify different categories (fields) for storing information. 

Each field has a name and a specific data type (e.g., string, integer, Boolean), so the program knows how to store and handle each piece of data. This way, when the program creates actual records, it knows exactly what 

kind of information to expect in each field.

## Creating a Single Record Structure

=== "Python"

    ``` python
	from dataclasses import dataclass
	
	@dataclass
    }
    ```

=== "Explanation"

	__Line 1 - from dataclasses import Dataclass__
	This line is like getting a special helper from a toolbox. It brings in something called dataclass, which makes it easier to create a class that stores information.
	
	__Line 3 - @dataclass__
	This is a special tag that tells Python, "I want to make the next class a dataclass." This means Python will automatically help us with things like creating the class and keeping track of data inside it.

