lst = [23,8,1,20,1,23,5,9,18,4,19,20,1,20,9,19,20,1,20,9,15,14]
f = ""
for num in lst:
    o = num + 96
    f += chr(o)
print("DOCTF{"+f+"}")   # use '_' inside the flag for segregation