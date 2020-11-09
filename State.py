class State:
    """
    this class only stores a string for the identifier of the class. It has getters and setters for it.
    """
    def __init__(self, id):
        self.identifier = id

    def get_identifier(self):
        return self.identifier
    def set_identifier(self,id):
        self.identifier = id
