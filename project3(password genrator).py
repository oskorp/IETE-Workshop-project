import random


alphabets='abcdefghijklmnopqrstuvwxyz'

capital=alphabets.upper()
small=alphabets.lower()
numbers='1234567890'
special_char='!@#$%'

all=capital+small+numbers+special_char

length=8

password="".join(random.sample(all,length))

print("Your genrated password:",password)
