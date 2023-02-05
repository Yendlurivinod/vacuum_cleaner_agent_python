def isdirty(i,j):
    if l[i][j]==1:
        return 1
    return 0
def suck(i,j):
    l[i][j]=0
def up():
    vc[0]=vc[0]-1
def down():
    vc[0]=vc[0]+1  
def right():
    vc[1]=vc[1]+1
def left():
    vc[1]=vc[1]-1
def BlueBG(s): print("\033[46m{}\033[00m".format(s),end=' ')   # Blue background to indicate agent position
def pr():
    for i in range(n):
        for j in range(n):
            if vc[0]==i and vc[1]==j:
                BlueBG(l[i][j])
            else:
                print(l[i][j],end=' ')
        print('')
    
#----------------------------------------------
print('enter size')
n=int(input()) #nxn matrix
print('enter vacuum cleaner position')
vc=[0]*2
vc[0]=int(input())  # x-corordinate
vc[1]=int(input())  # y-corordinate

print('vacuum cleaner position is: ',vc)
print('enter room status 1-dirty 0-clean for all rooms')
l=[[int(input()) for j in range (n)] for i in range(n)]   #room status 1-dirty, 0-clean
print('dirt is in following rooms: ')
pr()
c=0
if(vc[0]!=0 and vc[1]!=0): # case-2 agent not at (0,0)
    x=vc[0]
    y=vc[1]
    for i in range(y+1):
        if isdirty(vc[0],vc[1])==1:
            suck(vc[0],vc[1])
            print('room', vc[0],',',vc[1] ,'is cleaned')
        print('vacuum cleaner at')
        pr()
        left()
    right()
    up()
    for i in range(x-1):
        if isdirty(vc[0],vc[1])==1:
            suck(vc[0],vc[1])
            print('room', vc[0],',',vc[1] ,'is cleaned')
        print('vacuum cleaner at')
        pr()
        up()
        
while c<=(n*n-1): # agent position at (0,0)
    for k in  range(n):
        if isdirty(vc[0],vc[1])==1:
            suck(vc[0],vc[1])
            print('room', vc[0],',',vc[1] ,'is cleaned')
        print('vacuum cleaner at')
        pr()
        right()
        c+=1
    left() 
    down()
    if c>=(n*n-1):
        break
    for k in  range(n):
        if isdirty(vc[0],vc[1])==1:
            suck(vc[0],vc[1])
            print('room', vc[0],',',vc[1] ,'is cleaned')
        print('vacuum cleaner at')
        pr()
        left()
        c+=1
    right()
    down()
print('All rooms cleaned bro')  
