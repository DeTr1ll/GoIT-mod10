from collections import UserDict
class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)
        self.validate_phone()

    def validate_phone(self):
        if not self.value.isdigit() or len(self.value) != 10:
            raise ValueError("Invalid phone number format. It should be 10 digits.")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        old_phone_obj = self.find_phone(old_phone)
        
        if old_phone_obj:
            old_phone_obj.value = new_phone
        else:
            raise ValueError("Phone number not found in the record.")

    def find_phone(self, phone):
        return next((p for p in self.phones if p.value == phone), None)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]