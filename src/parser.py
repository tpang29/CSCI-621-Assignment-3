from errors import *
# define terminals
ZERO = "0"
ONE = "1"
TWO = "2"
THREE = "3"
FOUR = "4"
FIVE = "5"
SIX = "6"
SEVEN = "7"
EIGHT = "8"
NINE = "9"
EXP = "^"
COMMA = ","
EOF = "$"

# split terminals into groups for rule generation
terminal_digits = {ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE}
terminals_characters = {EXP, COMMA, EOF}

# union of all terminals into complete terminal set
terminals = terminal_digits | terminals_characters

# define nonterminals
ELIST = "elist"
ELIST_PRIME = "elist`"
E = "e"
E_PRIME = "e`"
N = "n"
N_PRIME = "n`"
nonterminals = {ELIST, ELIST_PRIME, E, E_PRIME, N, N_PRIME}

# create rules
rules = dict()

# create ELIST rules
rules[ELIST] = dict()
for digit in terminal_digits:
    rules[ELIST].update({ digit : [E, ELIST_PRIME] })

# create E rules
rules[E] = dict()
for digit in terminal_digits:
    rules[E].update({ digit : [N, E_PRIME] })

# create N rules
rules[N] = dict()
for digit in terminal_digits:
    rules[N].update({ digit : [digit, N_PRIME] })

# create N_PRIME rules
rules[N_PRIME] = dict()
for digit in terminal_digits:
    rules[N_PRIME].update({ digit : [N] })

# create ELIST_PRIME rules
rules[ELIST_PRIME] = dict()
rules[ELIST_PRIME].update({ COMMA : [COMMA, ELIST] })
rules[ELIST_PRIME].update({ EOF : [] })

# create E_PRIME rules
rules[E_PRIME] = dict()
rules[E_PRIME].update({ EXP : [EXP, E] })
rules[E_PRIME].update({ EOF : [] })
rules[E_PRIME].update({ COMMA : [] })

# create additional N_PRIME rules
rules[N_PRIME].update({ EXP : [] })
rules[N_PRIME].update({ COMMA : [] })
rules[N_PRIME].update({ EOF : [] })

# print error
def printError(stack, input_string, ip):
    message = ""
    message += "Error:\n"
    message += "\tStack:\t" + str(stack) + "\n"
    message += "\tInput:\t" + input_string + "\n"
    message += "\tChar:\t" + "'" + input_string[ip] + "'"
    return message
    # print("Error:")
    # print("\tBlock:\t" + location)
    # print("\tStack:\t" + str(stack))
    # print("\tInput:\t" + input_string)
    # print("\tChar:\t" + "'" + input_string[ip] + "'")






def parse(input_string):
    # create stack
    stack = []

    # push $ and start symbol onto stack
    stack.append("$")
    stack.append("elist")

    # initialize input pointer
    ip = 0

    # append input string with EOF marker
    input_string += "$"

    while not stack[-1] == "$":
        if stack[-1] in terminals or stack[-1] == "$":
            if stack[-1] == input_string[ip]:
                stack.pop()
                ip += 1
            else:
                # message = printError(stack, input_string, ip)
                # print(message)
                raise TerminalException(f"Stack: {stack[-1]}\nIP: {input_string[ip]}")
        elif stack[-1] in rules and input_string[ip] in rules[stack[-1]]:
            top = stack.pop()

            # push rule in reverse onto stack
            for index in range(len(rules[top][input_string[ip]]), 0, -1):
                stack.append(rules[top][input_string[ip]][index - 1])

            # print rule 
            print(top + " -> " + str(rules[top][input_string[ip]]))
        else: 
            # message = printError(stack, input_string, ip)
            # print(message)
            raise RuleNotFoundException(f"Stack: {stack[-1]}\nIP: {input_string[ip]}")