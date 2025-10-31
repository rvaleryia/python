class Lead:
    def __init__(self, name):
        self.name = name
    def change_name(lead, new_name):
        lead.name = new_name

lead = Lead("Lera")
print(lead.name)

lead.change_name("Valera")
print(lead.name)

