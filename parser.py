#brainfuck parser for brain rotted people like me
with open ("brainfix.py","r") as file:
	brainfix = file.read()

print("Starting to parse. Saving results in parsed.txt")

parsed = open("parsed.txt", "w")
converted = open("converted.py", "w")
length = len(brainfix)

counter = 0
i = 0
indent_amount = 0
while i<length:
	curr_symbol = brainfix[i]
	counter += 1

	if curr_symbol == "[":
		parsed.write("\n")
		parsed.write("Begin loop \n")
		counter = 0
		indent_amount += 4

	elif curr_symbol == "]":
		parsed.write("Ended loop \n")
		parsed.write("\n")
		counter = 0
		indent_amount -= 4


	if i+1 == length or curr_symbol != brainfix[i+1]:
		if curr_symbol == "<":
			parsed.write(" "*indent_amount)
			parsed.write(f"mov {counter} left\n")
		
		elif curr_symbol == ">":
			parsed.write(" "*indent_amount)
			parsed.write(f"mov {counter} right\n")
		
		elif curr_symbol == "+":
			parsed.write(" "*indent_amount)
			parsed.write(f"inc by {counter}\n")
		
		elif curr_symbol == "-":
			parsed.write(" "*indent_amount)
			parsed.write(f"minus by {counter}\n")
		
		elif curr_symbol == ",":
			parsed.write(" "*indent_amount)
			parsed.write(f"input {counter} chars\n")
		
		elif curr_symbol == ".":
			parsed.write(" "*indent_amount)
			parsed.write("Output the char\n")

		counter = 0
	i += 1

print("Starting transpiler")


parsed.write("Python interpretation. All rights not reserved \n")

memory = [0] * 30000

i = 0
j = 0
converted.write("j = 0 \n")

indent_amount = 0
converted.write("memory = [0] * 30000\n")
while i < length:
	if brainfix[i] == "[":
		converted.write(" "*indent_amount)
		converted.write(f"while memory[j] != 0:\n")
		indent_amount += 4
	elif brainfix[i] == "]":
		indent_amount -= 4
	elif brainfix[i] == ">":
		converted.write(" " * indent_amount + "j += 1\n")
	elif brainfix[i] == "<":
		converted.write(" " * indent_amount + "j -= 1\n")
	elif brainfix[i] == ",":
		converted.write(" "*indent_amount)
		converted.write(f"memory[j] = ord(input()[0])\n")
	elif brainfix[i] == ".":
		converted.write(" "*indent_amount)
		converted.write('print(chr(memory[j]), end="")\n')
	elif brainfix[i] == "+":
		converted.write(" "*indent_amount)
		converted.write(f"memory[j] = (memory[j]+1)%256\n")
	elif brainfix[i] == "-":
		converted.write(" "*indent_amount)
		converted.write(f"memory[j] = (memory[j]-1)%256\n")
	i += 1


parsed.close()
converted.close()
print("Finish parsing.")











































