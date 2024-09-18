from database import Database
from datetime import datetime

def print_menu():
    print("\n1. Додати нову людину")
    print("2. Пошук людини")
    print("3. Зберегти базу у файл")
    print("4. Завантажити базу з файлу")
    print("5. Вийти")

def main():
    db = Database()

    while True:
        print_menu()
        choice = input("Оберіть дію: ")

        if choice == '1':
            first_name = input("Ім'я: ")
            last_name = input("Прізвище (не обов'язково): ")
            middle_name = input("По-батькові (не обов'язково): ")
            birth_date = input("Дата народження (формати: 12.10.1980, 12 10 1980, 12/10/1980, 12-10-1980): ")
            death_date = input("Дата смерті (не обов'язково): ")
            gender = input("Стать (m/f): ")
            db.add_person(first_name, last_name, middle_name, birth_date, death_date, gender)
            print("Людину додано до бази.")

        elif choice == '2':
            query = input("Введіть ім'я, прізвище або по-батькові для пошуку: ")
            results = db.search_person(query)
            if results:
                for person in results:
                    print(person)
            else:
                print("Нічого не знайдено.")

        elif choice == '3':
            filename = input("Введіть назву файлу для збереження: ")
            db.save_to_file(filename)
            print("Базу збережено.")

        elif choice == '4':
            filename = input("Введіть назву файлу для завантаження: ")
            db.load_from_file(filename)
            print("Базу завантажено.")

        elif choice == '5':
            print("Програма завершила роботу.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
