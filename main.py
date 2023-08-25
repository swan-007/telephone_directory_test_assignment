import json
from pprint import pprint
from validator import ValidatorPhoneBook


class PhoneBook:
    """Класс для работы с телефонной книгой"""

    valid = ValidatorPhoneBook()

    def get_all(self):
        """Получить все записи"""
        with open("phone_book.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            pprint(data)

    def get_filter(self, **kwargs):
        """Получить отфильтрованные записи"""
        with open("phone_book.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            search = list(
                filter(
                    lambda items: items["name"].title() == kwargs["name"].title()
                    or items["personal_number"] == kwargs["personal_number"]
                    or items["surname"] == kwargs["surname"]
                    or items["company"] == kwargs["company"]
                    or items["id"] == kwargs["id"],
                    data,
                )
            )
            if len(search) < 1:
                pprint("Записи с такими данными нет")
                return
            pprint(search)

    def create_content(self, **kwargs):
        """Создать запись"""
        data_verification = self.valid.create_validator(kwargs)
        if data_verification["Status"] is True:
            with open("phone_book.json.") as f:
                data = json.load(f)
            kwargs["id"] = data_verification["id"]
            data.append(kwargs)
            with open("phone_book.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
                pprint(f"Новая запись добавлена, id = {data_verification['id']}")
        else:
            pprint(data_verification)

    def update_content(self, **kwargs):
        """Изменить запись"""
        data_verification = self.valid.update_validator(kwargs)
        if data_verification["Status"] is True:
            with open("phone_book.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            for i in data:
                if i["id"] == data_verification["final_dict"]["id"]:
                    i.update(data_verification["final_dict"])
            with open("phone_book.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
                pprint("Данные обновлены")
                return data_verification
        pprint(data_verification)


def start(command):
    obj = PhoneBook()
    if command == "g":
        obj.get_all()

    if command == "f":
        obj.get_filter(
            name=input("name-"),
            personal_number=input("personal_number-"),
            surname=input("surname-"),
            company=input("company-"),
            id=input("id-"),
        )
    if command == "c":
        obj.create_content(
            name=input("name-"),
            surname=input("surname-"),
            patronymic=input("patronymic-"),
            working_number=input("working_number-"),
            personal_number=input("personal_number-"),
            company=input("company-"),
        )
    if command == "u":
        obj.update_content(
            id=input("id-"),
            name=input("name-"),
            surname=input("surname-"),
            patronymic=input("patronymic-"),
            working_number=input("working_number-"),
            personal_number=input("personal_number-"),
            company=input("company-"),
        )



if __name__ == "__main__":
    while True:
        start(
            input(
                "Команды: \n "
                "Вывод записей - g \n "
                "Поиск записей - f \n "
                "Добавление записи - c \n "
                "Редактирования записи - u \n"
                " Введите команду -"
            )
        )



