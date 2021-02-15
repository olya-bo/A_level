class UnableToWorkException(Exception):
    pass

class Employee(object):
    def __init__(self, name, email, one_day_salary):
        self.name = name
        self.one_day_salary = one_day_salary
        self.email = self.check_email(email)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    def check_email(self, email):
        with open('email.txt', 'a+') as email_write:
            email_write.seek(0, 0)
            if email in email_write.read().splitlines():
                raise ValueError("This email already exists")
            else:
                email_write.write(email + '\n')
        return email

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


class Candidate(object):
    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade


    def work(self):
        raise UnableToWorkException("I'm not hired yet, lol")


class Vacancy(object):
    def __init__(self,  title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level
