e="👎👍👍👎👍👎👎👍👎👍👍👎👎👎👍👍👎👍👍👍👎👍👎👎👎👍👍👎👎👍👍👎👎👍👍👍👍👎👍👍👎👍👍👎👎👍👎👍👎👍👍👎👍👍👍👎👎👍👍👎👎👎👍👍👎👎👍👍👎👎👎👎👎👍👍👎👎👍👎👎👎👍👍👎👍👎👎👍👎👍👍👎👍👍👍👎👎👍👍👎👎👍👍👍👎👍👎👍👍👍👍👍👎👍👍👎👍👎👎👍👎👍👍👍👎👎👍👍👎👍👎👍👍👍👍👍👎👍👍👎👍👍👍👎👎👎👍👍👎👎👎👎👎👍👍👍👎👍👎👎👎👍👎👍👍👍👍👍👎👍👍👎👎👍👎👍👎👍👍👎👍👍👍👎👎👍👍👎👎👎👍👍👎👍👍👍👎👎👍👎👎👍👍👍👍👎👎👍👎👍👍👍👎👎👎👎👎👍👍👍👎👍👎👎👎👍👍👎👍👎👎👍👎👎👍👍👎👎👎👎👎👍👍👎👍👍👍👎👎👍👎👍👍👍👍👍👎👎👍👍👎👎👎👍👎👍👍👎👎👎👍👎👎👎👍👍👎👎👍👎👎👍👍👎👎👍👎👍👎👎👍👍👎👎👎👎👎👍👍👎👎👍👎👎👎👎👍👍👎👍👎👎👎👎👍👍👎👎👍👍👎👍👍👍👍👍👎"
dic={"👎":"0","👍":"1"}  # making dictionary
cipher=""
for h in range(0,len(e)):  # making loop 0 to length of e
	for keys,values in dic.items():  # getting keys and values of dictionary
		if keys==e[h]:     # comparing
			cipher+=values   # adding the values for each emojis
	else:
		continue
i=0
flag=""
while i<=len(cipher)-1:
	c=cipher[i:i+8]    # slicing binaries in each 8bits
	flag+=chr(int(c,2))    # converting integer into character
	i+=8
print(flag)
