class Vet:
    def __init__(self, name, earnings = 0, id = None):
        self.name = name
        self.earnings = earnings
        self.id = id

    def add_to_earnings(self, amount):
        self.earnings += amount
        return
