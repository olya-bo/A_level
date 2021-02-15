from models import *
from datetime import datetime


def main():
    # hr = Recruiter('Ivan', 'ivan@gmail.com', 200)
    # programmer1 = Programmer('Jon', 'jon@gmail.com', 450)
    # programmer2 = Programmer('Kto_to_ne_ya', 'programist@gmail.com', 10**10)
    programmer3 = Programmer('Kto_to_ne_ya1', 'programist1@gmail.com', 10 ** 10)
    candidate1 = Candidate('Admin Admin', 'admin@gmail.com', 'Big Data Analytics', 'Commercial awareness', 'grade_A')
    candidate1.work()
    # candidate2 = Candidate('Quack Quack', 'quack@gmail.com', 'Cyber security', 'Communication', 'grade_B')
    # candidate3 = Candidate('Big Boss', 'bidboss@gmail.com', '5G Technology', 'Problem solving', 'grade_C')
    # vacancy1 = Vacancy('developer', 'Ability to work under pressure', 'Senior')
    # vacancy2 = Vacancy('hr', 'Organisation', 'Middle')


if __name__ == "__main__":
    try:
        main()
    except (UnableToWorkException, ValueError) as e:
        with open("logs.txt", 'a+') as logs:
            now = datetime.today()
            logs.write(f'{now.strftime("%d-%m-%Y")}: {now.strftime("%H:%M:%S")}    {type(e).__name__}, {e}\n')

print('Done')
