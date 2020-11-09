from State import State


class Transition:
    """
    this class represents a transition between a state, a letter and its result ( a state ).
    it has getters and setters for every field.
    """
    def __init__(self, id, letter,result):
        self.state = id
        self.letter = letter
        self.result = result

    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state

    def get_letter(self):
        return self.letter
    def set_letter(self,letter):
        self.letter = letter

    def get_result(self):
        return self.result
    def set_result(self, result):
        self.result = result

