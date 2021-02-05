class Employee(object):
    def __init__(self, name, email, one_day_salary):
        self.name = name
        self.email = email
        self.one_day_salary = one_day_salary

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    def work(self):
        return 'I come to the office.'

    def check_salary(self, days):
        return f'Your salary now {days * self.one_day_salary}$'


class Recruiter(Employee):
    def work(self):
        return f'{super().work()[:-1]} and start to hiring.'


class Programmer(Employee):
    def work(self):
        return f'{super().work()[:-1]} and start to coding.'
