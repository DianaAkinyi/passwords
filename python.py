

#how to generate password 
import random           #
lowercase="a-z"
uppercase="A-Z"
number="0-9"
symbol="@!#$%*/\?&"
case=lowercase+uppercase+number+symbol
length=8
password="".join(random.sample(case,length)) #
print("your generated password is:" + password)


