from State import State


class Transition:
    def __init__(self):
        self.state = State()
        self.letter = ""
        self.result = State()

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

