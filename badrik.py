user_ip = raw_input("Enter the ip address")
print(user_ip)
print('\n')
print(type(user_ip))

x = user_ip.split(".")
print(x)

count = 0
for i in x:
    print(type(i),'i')
    i1 = int(i)
    print(type(i1),'i1')
    if i1 >= 0 and i1 <=255:
        print(i1,'yes')
    else:
        print(i1,'no')
