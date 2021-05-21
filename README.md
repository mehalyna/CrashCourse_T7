## Task 8. OOP

#### Task 1. Make a Circle with OOP

Your task is to create a _Circle_ constructor that creates a circle with a radius provided by an argument.   
The circles constructed must have two getters _getArea() (PIr^2)_ and _getPerimeter() (2PI*r)_ which give both respective areas and perimeter (circumference).

For help with this class, I have provided you with a Rectangle constructor which you can use as a base example.
  
_Notes_
Round results up to the nearest integer.  

_Examples_  
```plaintext
circy = Circle(11)
circy.getArea()

# Should return 380.132711084365

circy = Circle(4.44)
circy.getPerimeter()

# Should return 27.897342763877365
```
  
 

#### Task 2. Simple OOP Calculator 

Create methods for the **Calculator** class that can do the following:

- Add two numbers.
- Subtract two numbers.
- Multiply two numbers.
- Divide two numbers.  

_Notes_  

The methods should return the result of the calculation.  

Don't worry about needing to handle division by zero errors.

_Examples_  
```plaintext
calculator = Calculator()
calculator.add(10, 5) ➞ 15
calculator.subtract(10, 5) ➞ 5
calculator.multiply(10, 5) ➞ 50
calculator.divide(10, 5) ➞ 2
```

