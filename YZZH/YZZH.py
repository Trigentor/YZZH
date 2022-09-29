#1
#for i in range (5):
#    print(i+1,"0")
#a=0
#2
#for i in range(101):
#    a+=i
#print(a)
#3
#m=int(input(""))
#n=int(input(""))
#if(m<n):
#    for i in range(m,n+1):
#        print(i)
#elif(m>n):
#    for i in range(n,m+1):
#        print(i)
#4
#m=int(input(""))
#n=int(input(""))
#if(m>n):
#    for i in range(n,m+1,2):
#        print(i)
#else:
#    print("ERROR")
#5
#m=2
#n=4
#p=3
#g=1
#for i in range(15):
#    for i in range(m,n+1):
#        g*=i
#    m+=2
#    n+=2
#    p+=4/g
#print(p)
#6
#m=int(input(""))
#n=int(input(""))
#if(m<=n):
#    for i in range(m,n+1):
#        if(i%17==0):
#            print(i)
#        elif(i%10==9):
#            print(i)
#        elif(i%3==0 and i%5==0):
#            print(i)
#else:
#    print("ERROR")
#7
#a=1
#for i in range(1,1435+1,2):
#    a*=i
#print(a)
#8
#m=int(input(""))
#n=int(input(""))
#t=int(input(""))
#a=0
#if(m>0):
#    a+=1
#if(n>0):
#    a+=1
#if(t>0):
#    a+=1
#print(a)