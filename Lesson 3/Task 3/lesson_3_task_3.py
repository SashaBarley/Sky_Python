from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Улица Пушкина", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Улица Лермонтова", "20", "10")

mailing = Mailing(to_address, from_address, 1000, "555555")

print("Отправление", mailing.track, "из", from_address.index, from_address.city, from_address.street, from_address.house, "-", from_address.room, 
      "в", to_address.index, to_address.city, to_address.street, to_address.house, "-", to_address.room, ". Стоимость", mailing.cost, "рублей.")
