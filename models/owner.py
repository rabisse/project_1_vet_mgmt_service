class Owner:
    def __init__(self, name, phone, email, bill = 0, id = None):
        self.name = name
        self.phone = phone
        self.email = email
        self.bill = bill
        self.pet_list = []
        self.id = id
