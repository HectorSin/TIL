from stack import Stack
import sys

instr = input("문자열 입력:")
s = Stack()

instr = instr.lower()
for ch in instr:
    if ord(ch) < ord('a') or ord(ch) > ord('z') : 
        continue         # 스페이스나 구두점 제외
    s.push(ch)           # 입력 문자열의 모든 문자를 스택에 삽입

print("스택: ", s.top)

for ch in instr:  # 문자열의 앞쪽에서 뒤쪽 방향으로 문자 가져옴
    if ord(ch) < ord('a') or ord(ch) > ord('z') :
        continue
    if ch != s.pop() :  # 스택에서는 반대로 문자열의 뒤쪽에서 앞쪽 방향으로 문자 꺼냄
        print("회문이 아님")
        sys.exit()
print("회문이 맞음")