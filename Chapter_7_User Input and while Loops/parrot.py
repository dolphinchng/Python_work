#  coding:utf-8

# 函数input()的工作原理

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#让用户选择何时退出

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
       message = input(prompt)
       if message != 'quit':
              print(message)


# 7.2.3 使用标志
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
       message = input(prompt)
       
       if message != 'quit':
              print(message)
       else:
              active = False

