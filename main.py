import psycopg2

from utils import create_table, add_to_table

from DBManager import DBManager

if __name__ == "__main__":

    create_table()
    conn = psycopg2.connect(host="localhost", database="hh_vacancy",
                            user="postgres", password="krot123.A")

    employers_list = [3529, 78638, 4006, 561525, 64174, 8642172, 9498120, 816144, 2180]
    dbmanager = DBManager(conn)
    add_to_table(employers_list, conn)

    while True:

        task = input(
            "Введите 1, чтобы получить список всех компаний и количество вакансий у каждой компании\n"
            "Введите 2, чтобы получить список всех вакансий с указанием названия компании, "
            "названия вакансии и зарплаты и ссылки на вакансию\n"
            "Введите 3, чтобы получить среднюю зарплату по вакансиям\n"
            "Введите 4, чтобы получить список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
            "Введите 5, чтобы получить список всех вакансий, в названии которых содержатся переданные в метод слова\n"
            "Введите Стоп, чтобы завершить работу\n"
        ).lower()

        if task == "стоп":
            conn.close()
            break
        elif task == '1':
            print(dbmanager.get_companies_and_vacancies_count())
            print()
        elif task == '2':
            print(dbmanager.get_all_vacancies())
            print()
        elif task == '3':
            print(dbmanager.get_avg_salary())
            print()
        elif task == '4':
            print(dbmanager.get_vacancies_with_higher_salary())
            print()
        elif task == '5':
            keyword = input('Введите ключевое слово: ')
            print(dbmanager.get_vacancies_with_keyword(keyword))
            print()
        else:
            print('Неправильный запрос')
            conn.close()