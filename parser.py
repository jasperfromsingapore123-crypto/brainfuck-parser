#brainfuck parser for brain rotted people
with open ("brainfix.py","r") as file:
	brainfix = file.read()

print("Starting to parse. Saving results in parsed.txt")

parsed = open("parsed.txt", "w")

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
		indent_amount = 0


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
parsed.write("i = 0 \n")

indent_amount = 0
parsed.write("memory = [0] * 30000\n")
while i < length:
	if brainfix[i] == "[":
		parsed.write(f"while memory[{j}] != 0:\n")
		indent_amount += 4
	elif brainfix[i] == "]":
		indent_amount -= 4
	elif brainfix[i] == ">":
		j += 1
	elif brainfix[i] == "<":
		j -= 1
	elif brainfix[i] == ",":
		parsed.write(" "*indent_amount)
		parsed.write("x = int(input())\n")
		parsed.write(f"memory[{j}] = x\n")
	elif brainfix[i] == ".":
		parsed.write(" "*indent_amount)
		parsed.write(f"print(memory[{j}])")
	elif brainfix[i] == "+":
		parsed.write(" "*indent_amount)
		parsed.write(f"memory[{j}] += 1\n")
	elif brainfix[i] == "-":
		parsed.write(" "*indent_amount)
		parsed.write(f"memory[{j}] -= 1\n")
	i += 1


parsed.close()
print("Finish parsing.")











































