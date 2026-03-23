import os
print ("= = nmap scanner tool = = =")
target = input(" Enter target (ip or website")
print ("""
slect scen type
1. fast scan
2. Full port scan
3. os detection
""")
choice = input(" Enter choice (1/2/3):")
print("\n Scanning Started.....\n")
if choice == "1":
   os.system(f"nmap -F {target}")
elif choice == "2":
   os.system(f"nmap -P {target}")
elif choice == "3":
   os.system(f"nmap -A {target}")
else:
   print("invalid choice")
