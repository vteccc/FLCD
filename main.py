from lab4.FA import FA

# ht = HashTable()
# print(ht.hash("f"))
# print(ht.hash("c"))
# print(ht.hash("r"))
# print(ht.hash("i"))
# print(ht.hash("p"))
#
# print(ht)

# from Scanner import Scanner
#
# scanner = Scanner("prerr.txt")
# scanner.run()

from lab4.State import State
from lab4.Transition import Transition

fa = FA()
states = []
alpha = []
transitions = []
final = []
"""
reading from the file FAa.in and parse the file to fin in the specific FA class with State classes and Transitions classes.
"""
with open("lab4/FA.in", "r") as file:
    line = file.readline()
    line = line.rstrip()
    line = line.split(", ")
    for i in line:
        states.append(State(i))
    fa.set_states(states)
    fa.set_initState(states[0])

    line = file.readline()
    line = line.rstrip()
    line = line.split(", ")
    for i in line:
        alpha.append(i)
    fa.set_alphabet(alpha)
    for line in file:
        if '=' in line:
            line = line.rstrip()
            line = line.split(" ")
            res = line[3].split(",")
            l =[]
            for i in res:
                l.append(State(i))
            t = Transition(State(line[0]), line[1], l)
            transitions.append(t)
        else:
            for i in line:
                final.append(i)
    fa.set_transition(transitions)
    fa.set_finalStates(final)

boi = 1

while boi == 1:
    print("1. Display set of states\n"
                + "2. Display alphabet\n"
                + "3. Display transitions\n"
                + "4. Display final states\n"
                + "5. Check if it is DFA\n"
                + "6. Check a sequence\n"
                + "0. Quit\n")
    op = str(input("insert option: "))
    if op == "1":
        print(fa.print_states())
    if op == "2":
        print(fa.print_alphabet())
    if op == "3":
        print(fa.print_transitions())
    if op == "4":
        print(fa.print_finalState())
    if op == "5":
        print("DFA check: "+str(fa.isDFA()))
    if op == "6":
        if(fa.isDFA()):
            inp = str(input("insert sequence: "))
            print(inp+" acceptance is: "+str(fa.isAccepted(inp)))
        else:
            print("Non-DFA!")
    if op == "0":
        boi = 0