print("------methods of strings------")
print("---1.capitalize---\n")
    
s1 = 'dhee coding lab'
print(s1.capitalize())
print("---2.title---\n")

print(s1.title())
print("---3.upper---\n")

print(s1.upper())
print(s1)
print("---4.lower---\n")

s2 = "MYSTERY"
print(s2.lower())
print("---5.isupper---\n")

print(s2.isupper())
print("---6.islower---\n")

s3 = "today is thursday"
print(s3.islower())

print("---7.swapcase---\n")
s4 = "How Are You"
print(s4.swapcase())
print("---8.Count---\n")
s5 = "Good Afternoon"
print(s5.count(""))
print("---9.index---\n")
print(s5.index("o"))
print(s2.index("E"))
s6 = "we and you cant see yourself"
print(s6.index("you"))
print("---10.startswith---\n")
s7 = "where there is a will"
print(s7.startswith("Where"))
print("---11.endswith---\n")
print(s7.endswith("l"))
print("---12.isalpha---\n")
s8 = "Ramayana"
print(s8.isalpha())
print("---13.isdigit---\n")
pno="8431782461"
print(pno.isdigit())
print("---14.isalnum---\n")
pan = "A74EJK8"
print(pan.isalnum())
print("---15.lstrip---\n")
s9 = "   OMG YEH MERA INDIA   "
print(s9.lstrip())
print("---16.rstrip---\n")
print(s9.rstrip())
print("---17.strip---\n")
print(s9.strip())
print("---18.replace---\n")
s10 = "Ha Ha Ha HA"
print(s10.replace(" ",""))
print("---19.split---\n")
s11="Jack of All Trades Master of None but still gets the work done"
print(s11.split())
aadhar = "1234-6782-4134-8972"
print(aadhar.split("-"))

mail_id = "jarvis@gmail.com"
name = mail_id.split("@gmail.com")
print(len(name[0]))
print("---20.join---\n")
words = ['tom','jerry','ben10']
v = " and ".join(words)
print(v)
dates = ['15','08','1947']
c = "/".join(dates)
print(c)
