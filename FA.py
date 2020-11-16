from typing import List

from State import State


class FA:
    """
    this class represents the Finite Automata class.
    it stores the states, alphabet, initial state, transitions and final states.
    it has getters and setters for every field and toString to specific parts like:
    states, alphabet, transitions, final states and a string of the whole class.
    """

    def __init__(self):
        self.states = []
        self.alphabet = []
        self.initState = State("")
        self.transitions = []
        self.finalStates = []

    def get_states(self):
        return self.states

    def set_states(self, states):
        self.states = states

    def get_alphabet(self):
        return self.alphabet

    def set_alphabet(self, alph):
        self.alphabet = alph

    def get_initState(self):
        return self.initState

    def set_initState(self, init):
        self.initState = init

    def get_transition(self):
        return self.transitions

    def set_transition(self, trans):
        self.transitions = trans

    def get_finalStates(self):
        return self.finalStates

    def set_finalStates(self, fstates):
        self.finalStates = fstates

    def print_states(self):
        s = ""
        s += "states:\n[ "
        for i in self.states:
            s += i.get_identifier() + " "
        s += "]\n"
        return s

    def print_alphabet(self):
        s = ""
        s += "alphabet:\n[ "
        for i in self.alphabet:
            s += i + " "
        s += "]\n"
        return s

    def print_transitions(self):
        s = ""
        s += "transitions:\n[ "
        for i in self.transitions:
            s += i.get_state().get_identifier() + " " + i.get_letter() + " -> "
            for j in i.get_result():
                s += str(j.get_identifier()) + " "
            s += "\n"
        s += "]\n"
        return s

    def print_finalState(self):
        s = ""
        s += "final state:\n[ "
        for i in self.finalStates:
            s += i + " "
        s += "]\n"
        return s

    """
    Checks if the FA is Deterministic or not
    """

    def isDFA(self):
        for trans in self.transitions:
            if len(trans.get_result()) > 1:
                return False
        return True

    def isAccepted(self, sequence):
        if len(sequence) == 0 and self.initState in self.finalStates:
            return True
        currentState = self.initState
        for char in sequence:
            currentState = self.nextState(currentState, char)
            if currentState is None:
                return False
        return currentState.get_identifier() in self.finalStates

    def nextState(self, currentState, currentChar):
        for trans in self.transitions:
            if currentChar == trans.get_letter() and trans.get_state().get_identifier() == currentState.get_identifier():
                return trans.get_result()[0]
        return None

    def __str__(self):
        s = ""
        s += "states:\n[ "
        for i in self.states:
            s += i.get_identifier() + " "
        s += "]\n"

        s += "alphabet:\n[ "
        for i in self.alphabet:
            s += i + " "
        s += "]\n"

        s += "initial state:\n"
        s += self.initState.get_identifier() + "\n"

        s += "transitions:\n[ "
        for i in self.transitions:
            s += i.get_state().get_identifier() + " " + i.get_letter() + " " + i.get_result().get_identifier() + "\n"
        s += "]\n"

        s += "final state:\n[ "
        for i in self.finalStates:
            s += i + " "
        s += "]\n"
        return s
