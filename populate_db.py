import sqlite3

DATABASE = 'not_telegram.db'


def populate_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()

        cursor.execute("DELETE FROM Products")

        products = [
            ('Product1', 'Описание 1', 1000),
            ('Product2', 'Описание 2', 2000),
            ('Product3', 'Описание 3', 3000),
            ('Product4', 'Описание 4', 4000)
        ]

        cursor.executemany("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", products)

        conn.commit()
        print("Таблица Products успешно заполнена.")


if __name__ == '__main__':
    populate_db()
