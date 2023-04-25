from stack import Stack 

instr = input("문자열 입력:")
s = Stack()

for ch in instr:
    s.push(ch)

print("역순 문자열:")
while not s.isEmpty():
    print(s.pop(), "")

