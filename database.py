import json
from person import Person

class Database:
    def __init__(self):
        self.people = []

    def add_person(self, first_name, last_name='', middle_name='', birth_date=None, death_date=None, gender=None):
        """Додає нову людину в базу."""
        person = Person(first_name, last_name, middle_name, birth_date, death_date, gender)
        self.people.append(person)

    def search_person(self, query):
        """Пошук запису в базі за частиною імені, прізвища або по-батькові."""
        results = [person for person in self.people if query.lower() in person.first_name.lower() or
                   query.lower() in person.last_name.lower() or query.lower() in person.middle_name.lower()]
        return results

    def save_to_file(self, filename):
        """Зберігає базу даних у файл."""
        with open(filename, 'w', encoding='utf-8') as f:
            data = [vars(person) for person in self.people]
            json.dump(data, f, ensure_ascii=False, indent=4, default=str)

    def load_from_file(self, filename):
        """Завантажує базу даних з файлу."""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.people = [Person(**person) for person in data]
