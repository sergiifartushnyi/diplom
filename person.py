from datetime import datetime

class Person:
    def __init__(self, first_name, last_name='', middle_name='', birth_date=None, death_date=None, gender=None):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_date = self.parse_date(birth_date)
        self.death_date = self.parse_date(death_date)
        self.gender = gender

    def parse_date(self, date_str):
        """Перетворення дати з різних форматів в стандартний."""
        if not date_str:
            return None
        for fmt in ('%d.%m.%Y', '%d %m %Y', '%d/%m/%Y', '%d-%m-%Y'):
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        raise ValueError(f"Невірний формат дати: {date_str}")

    def get_age(self):
        """Обчислює вік на основі дати народження та смерті або поточної дати."""
        end_date = self.death_date or datetime.now()
        age = end_date.year - self.birth_date.year - ((end_date.month, end_date.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def __str__(self):
        age_str = f"{self.get_age()} років"
        gender_str = "чоловік" if self.gender == 'm' else "жінка"
        birth_str = f"Народився: {self.birth_date.strftime('%d.%m.%Y')}"
        death_str = f"Помер: {self.death_date.strftime('%d.%m.%Y')}" if self.death_date else ""
        return f"{self.first_name} {self.last_name} {self.middle_name} {age_str}, {gender_str}. {birth_str}. {death_str}"
