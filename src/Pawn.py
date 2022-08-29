class Pawn:

    def __init__(self, color: str):
        self.color = color

    def __repr__(self):
        return f"Pawn: {self.color}"