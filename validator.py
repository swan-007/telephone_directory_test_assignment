import json


class ValidatorPhoneBook:
    """Класс для валидации данных"""

    def create_validator(self, validated_data):
        """Валидация при создании"""
        if {"name", "surname", "working_number", "personal_number", "company"}.issubset(
            validated_data
        ):
            with open("phone_book.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            search = list(
                filter(
                    lambda x: x["personal_number"] == validated_data["personal_number"],
                    data,
                )
            )
            if search:
                return {
                    "Status": False,
                    "Errors": "Пользователь с таким номером уже существует",
                }
            if (
                len(validated_data["personal_number"]) > 12
                or len(validated_data["personal_number"]) < 11
            ):
                return {"Status": False, "Errors": "Номер указан некорректно"}
            else:
                len_data = len(data)
                return {"Status": True, "id": str(len_data + 1)}
        return {"Status": False, "Errors": "Не указаны все необходимые аргументы"}

    def update_validator(self, validated_data):
        """Валидация при редактировании"""
        final_dict = dict(filter(lambda items: items[1], validated_data.items()))
        if {"id"}.issubset(final_dict):
            if final_dict.get("personal_number"):
                if (
                    len(final_dict["personal_number"]) > 12
                    or len(final_dict["personal_number"]) < 11
                ):
                    return {"Status": False, "Errors": "Номер указан некорректно"}
                with open("phone_book.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                search = list(
                    filter(
                        lambda x: x["personal_number"] == final_dict["personal_number"],
                        data,
                    )
                )
                if search:
                    return {"Status": False, "Errors": "Номер уже существует"}
                else:
                    return {"Status": True, "final_dict": final_dict}
            else:
                return {"Status": True, "final_dict": final_dict}
        return {"Status": False, "Errors": "Для обновления нужен id"}
