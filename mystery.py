# Pass By-Value
def double(arg):
    print('Before: ',arg)
    arg = arg * 3
    print('After: ',arg)

# Pass By-Reference
def change(arg):
    print('Before: ',arg)
    arg.append('More data')
    print('After: ',arg)
