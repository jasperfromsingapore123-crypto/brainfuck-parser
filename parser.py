#brainfuck parser for brain rotted people like me
counter = 0 
jcounter = 0

currently_doing_operators = False
add = False
minus = False

currently_doing_j = False
j_add = False
j_minus = False

def print_operators(counter):
    global currently_doing_operators, add, minus
    if currently_doing_operators:
        if add:
            converted.write(" " * indent_amount)
            converted.write(f"memory[j] = (memory[j]+{counter})%256\n")

        elif minus:
            converted.write(" " * indent_amount)
            converted.write(f"memory[j] = (memory[j]-{counter})%256\n")

        currently_doing_operators = False
        add = False
        minus = False

def jprinter(jcounter):
	global currently_doing_j, j_add, j_minus
	if currently_doing_j:
		if j_add:
			converted.write(" "*indent_amount)
			converted.write(f"j += {jcounter}\n")
		elif j_minus:
			converted.write(" "*indent_amount)
			converted.write(f"j -= {jcounter}\n")

	currently_doing_j = False
	j_add = False
	j_minus = False


with open ("brainfix.py","r") as file:
	brainfix = file.read()

print("Starting to parse. Saving results in parsed.txt")

brainfix = "".join(c for c in brainfix if c in "+-<>[],.")
length = len(brainfix)

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
		parsed.write(" " * indent_amount + "Begin loop\n")
		counter = 0
		indent_amount += 4

	elif curr_symbol == "]":
		indent_amount -= 4
		parsed.write(" " * indent_amount + "Ended loop\n\n")
		counter = 0


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

counter = 0
jcounter = 0


parsed.write("Python interpretation. All rights not reserved \n")

converted.write("import sys\n")

memory = [0] * 30000

i = 0
j = 0
converted.write("j = 0 \n")

indent_amount = 0
converted.write("memory = [0] * 30000\n")

while i < length:
	if brainfix[i:i+2] == "[]":
		converted.write(" " * indent_amount)
		converted.write("while memory[j] != 0:\n")
		converted.write(" " * (indent_amount + 4))
		converted.write("pass\n")
		i += 2
		continue

	if brainfix[i:i+3] in ("[-]", "[+]"):
		converted.write(" " * indent_amount)
		converted.write("memory[j] = 0  # Reset variable\n")
		i += 3
		continue


	if brainfix[i] == "[":
		converted.write(" "*indent_amount)
		converted.write(f"while memory[j] != 0:\n")
		indent_amount += 4
	elif brainfix[i] == "]":
		indent_amount -= 4
	
	elif brainfix[i] == ">":
		currently_doing_j = True
		jcounter += 1
		j_add = True
		j_minus = False
		# converted.write(" " * indent_amount + "j += 1\n")
	elif brainfix[i] == "<":
		currently_doing_j = True
		jcounter += 1
		j_add = False
		j_minus = True
		# converted.write(" " * indent_amount + "j -= 1\n")
	
	elif brainfix[i] == ",":
		converted.write(" " * indent_amount)
		converted.write("memory[j] = ord(sys.stdin.buffer.read(1))\n")
	elif brainfix[i] == ".":
		converted.write(" "*indent_amount)
		converted.write('print(chr(memory[j]), end="")\n')
	
	elif brainfix[i] == "+":
		currently_doing_operators = True
		add = True
		minus = False
		counter += 1
		# converted.write(f"memory[j] = (memory[j]+1)%256\n")
	elif brainfix[i] == "-":
		currently_doing_operators = True
		minus = True
		add = False
		counter += 1
		# converted.write(f"memory[j] = (memory[j]-1)%256\n")

	if brainfix[i] in "+-":
		if i + 1 == length or brainfix[i] != brainfix[i + 1]:
			print_operators(counter)
			counter = 0
	if brainfix[i] in "><":
		if i + 1 == length or brainfix[i] != brainfix[i + 1]:
			jprinter(jcounter)
			jcounter = 0
	i += 1


parsed.close()
converted.close()
print("Finish parsing.")











































