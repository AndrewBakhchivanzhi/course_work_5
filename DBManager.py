import psycopg2


class DBManager:
    def __init__(self, conn):
        self.conn = conn

    def get_companies_and_vacancies_count(self):
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(f"SELECT company_name, COUNT(vacancies_name) AS count_vacancies  "
                            f"FROM employers "
                            f"JOIN vacancies USING (employer_id) "
                            f"GROUP BY employers.company_name")
                result = cur.fetchall()
            self.conn.commit()
        return result

    def get_all_vacancies(self):
        with  self.conn:
            with self.conn.cursor() as cur:
                cur.execute(f"SELECT employers.company_name, vacancies.vacancies_name, "
                            f"vacancies.payment, vacancies_url "
                            f"FROM employers "
                            f"JOIN vacancies USING (employer_id)")
                result = cur.fetchall()
            self.conn.commit()
        return result

    def get_avg_salary(self):
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(f"SELECT AVG(payment) as avg_payment FROM vacancies ")
                result = cur.fetchall()
            self.conn.commit()
        return result

    def get_vacancies_with_higher_salary(self):
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(f"SELECT * FROM vacancies "
                            f"WHERE payment > (SELECT AVG(payment) FROM vacancies) ")
                result = cur.fetchall()
            self.conn.commit()
        return result

    def get_vacancies_with_keyword(self, keyword):
        with self.conn:
            with self.conn.cursor() as cur:
                cur.execute(f"SELECT * FROM vacancies "
                            f"WHERE lower(vacancies_name) LIKE '%{keyword}%' "
                            f"OR lower(vacancies_name) LIKE '%{keyword}'"
                            f"OR lower(vacancies_name) LIKE '{keyword}%';")
                result = cur.fetchall()
            self.conn.commit()
        return result