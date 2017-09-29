Algorithm

We only really care about building up an expression tree. Once this is built the evaluation simply becomes evaluating every node recursively

This is a great site for viewing expression trees:
https://www.mathsisfun.com/algebra/operations-order-calculator.html.

The true test will be evaluating: 7-4*8+3-4/2 = -24
Which once ordered is: 
((7−4×8)+3)−4÷2

See the tree here:
http://www.mathsisfun.com/algebra/operations-order-calculator.html?i=7-4*8%2B3-4%2F2


3+2*4
10 - 10 / 5 + 3

1. Read token. 
2. If number then put in number stack.
3. If operator then 
	If operator stack is empty then add to stack
	Else
		If top operator stack is lower precedence
			then add operator to stack
		If top operator is higher precedence or equal
			while operator stack is not empty: # why operator stack? why not number stack?
				Create Node From Stack
						
4. If empty stream then
	while operator stack is not empty:
		Create Node From Stack and append this result to existing tree. ... where in the existing tree? wtf
		


Create Node From Stack

1. If number stack count greater then operator stack then:
	pop number stack, make this right operand
	pop operator stack, make this the operator
	pop number stack, make this left operand
	make node the root
   Else if number stack and operator stack are size of one AND is currently popping stack then:
	pop number stack, make this the left operand
	pop operator stack, make this the operator
	make right operand the previous root node
	make node the root
   Else if number stack and operator stack are size of one AND is not currently popping stack then:
	pop number stack, make this the right operand,
	pop operator stack, make this the operator,
	make left operand the previous root node
	make node the root
   Else if number stack and operator stack are equal:
	pop number stack, make this the right operand
	pop operator stack, make this the operator
	pop number stack, make this the left operand
	make new node

	make a new empty node the root node
	make left operand the existing root node
	make right operand the new tree
	pop operator from stack and add to operator of new node


	Brackets: naive approach!

	Is we tweak the ExpressionParser so that it's termination condition is the end of stream OR an end bracket ')' then surely we could just recurse into the expression parser again when we encounter an open bracket...
	Ensuring that these brackets are consumed properly. Fingers crossed this is a solution! Super easy if so...

	Test cases:

	(3+2)*4 = 20
	(10-10)+3/(5+3) = 0+(3/15) = 5
	(7-4)*(8+3-4)/7 = 3






	



