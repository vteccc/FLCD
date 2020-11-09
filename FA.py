from typing import List

from State import State


class FA:

    def __init__(self):
        self.states = []
        self.alphabet = []
        self.initState = State()
        self.transitions = []
        self.finalStates = []

    def get_states(self):
        return self.states
    def set_states(self,states):
        self.states = states

    def get_alphabet(self):
        return self.alphabet
    def set_alphabet(self, alph):
        self.alphabet = alph

    def get_initState(self):
        return self.initState
    def set_initState(self,init):
        self.initState = init

    def get_transition(self):
        return self.transitions
    def set_transition(self,trans):
        self.transitions = trans

    def get_finalStates(self):
        return self.finalStates
    def set_finalStates(self,fstates):
        self.finalStates = fstates

    def transformationFunc(self):
        pass

