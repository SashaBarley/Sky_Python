class User():
    first_name = 'имя'
    last_name = 'фамилия'

    def __init__(self, name, sName):
        
        self.first_name = name
        self.last_name = sName
    
    def sayFname(self):
        print("Имя ", self.first_name)
        
    def saySname (self):
        print("Фамилия  ", self.last_name)
    
    def fullName (self):
        print("Мое полное имя ", self.first_name, self.last_name)

# alex = User("Александр", "Ячменев")
# alex.sayFname()
# alex.saySname()
# alex.fullName()