from smartphone import Smartphone

iPhone = Smartphone("iPhone", "XS", "+79999999999")
samsung = Smartphone("Samsung", "A1", "+79998888888")
motorola = Smartphone("Motorola", "A1200", "+79997777777")
nokia = Smartphone("Nokia", "2100", "+79996666666")
fly = Smartphone("Fly", "DS150", "+79998888888")


catalog = [iPhone, samsung, motorola, nokia, fly]

for phone in catalog:
    print(phone.brand, phone.model, phone.number)
