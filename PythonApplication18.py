#palimdrome using stack

_input=input("Enter the input?")
data=[]
stack=[]

for i in _input:
    data.append(i)
while(data):
    stack.append(data.pop())

stack=("".join(stack))#convert list to string

if(_input==stack):
    print("It's a palindrome..!")
else:
    print("It's not a palindrome..!")