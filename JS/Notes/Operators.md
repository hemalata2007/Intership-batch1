## operators


////////    Types of operator //////////

- Arithmetic Operators
## Operator	Description
+	        Addition
-	        Subtraction
*	        Multiplication
**          Exponentiation 
/	        Division
%	        Modulus (Division Remainder)
++	        Increment
--	        Decrement
## Ex.let a = 3; 
## let x = (100 + 50) * a;

- Assignment Operators
## Operator	Example	    Same As
=	         x = y	     x = y
+=	         x += y	    x = x + y
-=	         x -= y	    x = x - y
*=	         x *= y	    x = x * y
/=	         x /= y	    x = x / y
%=	         x %= y	    x = x % y
**=	         x **= y	x = x ** y
EX.let x = 10;
x += 5;

- Comparison Operators
Operator	Description
==	         equal to
===	         equal value and equal type
!=	         not equal
!==	         not equal value or not equal type
>	         greater than
<	         less than
>=	         greater than or equal to
<=	         less than or equal to
?	         ternary operator

- String Operators
All the comparison operators above can also be used on strings:
Ex.let text1 = "A";
let text2 = "B";
let result = text1 < text2;

Ex.let text1 = "20";
let text2 = "5";
let result = text1 < text2;

Ex.let text1 = "John";
let text2 = "Doe";
let text3 = text1 + " " + text2;

Ex.let text1 = "What a very ";
text1 += "nice day";

Ex.let x = 5 + 5;
let y = "5" + 5;
let z = "Hello" + 5;

- Logical Operators
Operator	Description
&&	        logical and
||	        logical or
!	        logical not

- Bitwise Operators
Operator	Description	          Example	        Same as	           Result	Decimal
&	         AND	               5 & 1	      0101 & 0001	        0001	   1
|	         OR	                   5 | 1	      0101 | 0001	        0101	   5
~	         NOT	                ~ 5	             ~0101	            1010	  10
^	         XOR	               5 ^ 1	      0101 ^ 0001	        0100	   4
<<	         left shift	           5 << 1	       0101 << 1	        1010	  10
>>	         right shift	       5 >> 1	       0101 >> 1	        0010	   2
>>>	         unsigned right shift  5 >>> 1	      0101 >>> 1	        0010	   2

- Type Operators
Operator	    Description
typeof	        Returns the type of a variable
instanceof	    Returns true if an object is an instance of an object type

- Ternary Operators