class Person:

    def __init__(self, name, patronymic, surname, phones: dict):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.phones = phones

    def get_phone(self):
        return self.phones.get('private')

    def get_name(self):
        return ' '.join((self.surname, self.name, self.patronymic))

    def get_work_phone(self):
        return self.phones.get('work')

    def get_sms_text(self):
        text = "Уважаемый {} {}! Примите участие в нашем беспроигрышном конкурсе для физических лиц"
        return text.format(self.name, self.patronymic)


class Company:

    def __init__(self, company_name, company_type, phones, *persons):
        self.company_name = company_name
        self.company_type = company_type
        self.phones = phones
        self.persons = persons

    def get_phone(self):
        if 'contact' in self.phones:
            return self.phones['contact']
        for person in self.persons:
            work_phone = person.get_work_phone()
            if work_phone is not None:
                return work_phone

    def get_name(self):
        return self.company_name

    def get_sms_text(self):
        text = ('Для компании {} есть супер предложение!'
                ' Примите участие в нашем беспроигрышном конкурсе для {}')
        return text.format(self.company_name, self.company_type)


def send_sms(*args):
    for i in args:
        phone = i.get_phone()
        if phone is not None:
            sms = f'Отправлено СМС на номер {phone} с текстом: {i.get_sms_text()}'
        else:
            sms = f'Не удалось отправить сообщение абоненту: {i.get_name()}'
        print(sms)


person1 = Person("Степан", "Петрович", "Джобсов", {"private": 555})
person2 = Person("Боря", "Иванович", "Гейтсов", {"private": 777, "work": 888})
person3 = Person("Семен", "Робертович", "Возняцкий", {"work": 789})
person4 = Person("Леонид", "Арсенович", "Торвальдсон", {})
company1 = Company("Яблочный комбинат", "ООО", {"contact": 111}, person1, person3)
company2 = Company("ПластОкно", "АО", {"non_contact": 222}, person2)
company3 = Company("Пингвинья ферма", "Ltd", {"non_contact": 333}, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)