### Test8_infs3203

This is a simple command-line calculator program written in Python. It allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, division, modulo, power, and square root.


## Description

### Bug Identification:
#### Bug1: The square_root Operation in the Calculator Class Lacks a Condition for Handling Negative Numbers. 
**Resolution**: Changing the negative operational sign to plus operation sign 

#### Bug2: Enhancement to code for "square_root" operation
**Resolution**: Adding in if loop to identify related opreation function 

#### Bug3: The modulus operation in the Calculator class cannot have the divisor set to zero
**Resolution**: Adding in if loop to make sure it is not zero

#### Bug4: The power function in the calculator is producing an error
**Resolution**: Changing the operation sign to two asterisk to calculate as power

#### Bug5: The subtraction operation in the Calculator class is performing addition
**Resolution**: Changing the operation sign to subtraction

#### Bug6: The addition operation in the Calculator class is performing subtraction
**Resolution**: Changing the operation sign to subtraction

Tested each operation individually:
Ensured correct behavior for both positive and negative numbers. Checked edge cases such as division by zero. Validated the changes against expected results for each bug.
Ran the entire program to ensure overall functionality.

## Authors

Hamdan Mahroof - Hamdan-Maharoof
<br>Mazin Thajudeen - mazinthaj
<br>Ekram Karim - Git-Kar33


### Acknowledgments

https://github.com/vanilson/infs3203
