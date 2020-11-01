from baseball.enums.AttributeEnum import Attribute


class PlayerAttribute:

    def __init__(self, attribute: Attribute, value):

        self.attribute = attribute
        self.value = value

    def __repr__(self):

        return f"<Attribute: ({self.attribute.value}: {self.value})>"
