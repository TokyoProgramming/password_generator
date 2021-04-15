# PASSWORD GENERATOR

## Table of contents

- [General info](#general-info)
- [Technologies](#technologies)
- [Code Examples](#CodeExamples)
- [License](#License)

## General info

This is the project which will create random password.<br/>
output will be such as <br />

**['5KO68x7W5', 'D2JdGkFRw', 'R8xaTUtz8', '2VOwUoNsa', 'Wr358HC7r']**

## Technologies

Project is created with:

- python: 3.8.4

## CodeExamples

### 1 prepare lowercase, uppercase and numbers

```python

# prepare lowercase letters
lowercase = ['a','b', ... ,'z']

# generate uppercase letters
uppercase = []
for item in lowercase:
	upItem = item.upper()
	uppercase += [upItem]

# output will be like this <br />
print(output)
output = ['A','B','C',...,'Z']
# prepare number
number = ['1','2',...,'9']
```

### 2 generate password function

```python
import random
from random import randrange

# num: how many passwords would you like to generate
# size: password length
def pass_generate(num,size):
    j = 1
    password_arr = []

    while j <= num:
        password = []



        for i in range(1,size):
			# randrange randomly returns 0 to 2
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


```

## License

[MIT](https://choosealicense.com/licenses/mit/)
