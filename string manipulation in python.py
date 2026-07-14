#string manipulation in python

s1='hello'
s2='world'
s3='''multi line string'''
s4=r"raw \n string"

print(s1)
print(s2)
print(s3)
print(s4)
'''
#common string methods

s="    hello , world!    "

result=s.upper()
print(s)
result=s.lower()
print(result)
result=s.strip()
print(result)
result=s.lstrip()
print(result)
result=s.rstip()
print(result)
result=s.replace("world","python")
print(result)
result=s.split("+")
print(result)
result=s.find("world")
print(result)
result=s.count('l')
print(result)
result=s.startswith("    he")
print(result)
result=s.endswith("ld    ")
print(result)
'''
#string formatting

name = "alice"
age = 23

#f-string

print(f"name :%s,age:%d"%(name , age))

#padding & aligment

print(f"{name:<10}")
print(f"{name:>10}")
print(f"{name:^10}")
print(f"{2.30245435:.30f}")

#slicing

s="hello,world!"

prnit(s)

print(s(1))
print(s[0:5])
print(s[7:])
print(s[:5])
print(s[::2])
print(s[::-1])

#joining & spliting

words=["python","is","programming","language"]

print(" ".join(words))
print("_".join(words))

s="a,b,c,d"
result=s.split(",",4)

print(result)
