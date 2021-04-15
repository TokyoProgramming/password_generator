import random
from random import randrange

# define lowercase
lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# define uppercase
uppercase = []
for item in lowercase:
    upItem = item.upper()
    uppercase += [upItem] 
    
# define number
number = ['1','2','3','4','5','6','7','8','9']


# password_arr = []

def pass_generate(num,size):
    j = 1
    password_arr = []

    while j <= num: 
        password = []
        for i in range(1,size):
            selectArr = randrange(3)
            
            # choose from lowercase
            if(selectArr == 0):
                pass1 = random.choice(lowercase)
                password.append(pass1)

            
            # choose from uppercase
            elif(selectArr == 1):
                pass2 = random.choice(uppercase)
                password.append(pass2)

            
            # choose from number
            elif(selectArr == 2):
                pass3 = random.choice(number)
                password.append(pass3)

        
        result = ''.join(password)    
        password_arr.append(result)

        
        j +=1
        
    return password_arr
        
    
    
res = pass_generate(5,10)

print(res)

    

