filename = 'todos.txt'
tasks=open(filename,'x')

print('new file',file=tasks)
print('python',file=tasks)
print('create',file=tasks)

tasks.close();


read=open(filename)
for i in read:
    print(i,end='')

read.close()