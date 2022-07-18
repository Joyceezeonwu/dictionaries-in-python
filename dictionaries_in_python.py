# creating a dictionary with key:value pairs as num:squares
# create a dictionary called squares considering the range 5,16
# not using dictionary comprehension

squares = {}
for x in range(5,16):
    squares[x] = x*x

print(squares)

#using dictionary comprehension
square ={x: x*x for x in range(5,16)}
print(square)