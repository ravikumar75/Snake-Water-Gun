import random
def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='s':   
        if you=='g':
            return True
        if you=='w':
            return False
    elif comp=='g':    
        if you=='w':
            return True
        if you=='s': 
            return False
    elif comp=='w':    
        if you=='s':
            return True
        if you=='g': 
            return False        
print("comp turns:snake(s),water(w),gun(g)? ")
random=random.randint(1,3)
if random==1:
    comp='s'
if random==2:
    comp='w'
if random==3:
    comp='g'
you=input("Your turns:snake(s),water(w),gun(g)? ")
a=gameWin(comp,you)
print("comp choose "+ str(comp))
print("you choose "+ str(you))
if a==None:
    print("Tie!")
elif a:
    print("Win!")
else:
    print("Lose!")        