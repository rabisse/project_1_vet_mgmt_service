class Owner:
    def __init__(self, name, phone, email, bill = 0, id = None):
        self.name = name
        self.phone = phone
        self.email = email
        self.bill = bill
        self.id = id

    def add_to_bill(self, amount):
        self.bill += amount
        return
