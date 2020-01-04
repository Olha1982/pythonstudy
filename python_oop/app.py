from models.custom import Programmer
from models.custom import Recruiter
from models.candidate import Candidate
from models.vacancy import Vacancy
import datetime
import traceback

def validate(emp_list):
    list_emails = []
    for i in emp_list:
        list_emails.append(i.email)
    em_set = set(list_emails)
    if len(list_emails) != len(em_set):
        raise ValueError

def main():
    rec1 = Recruiter ('Andrew', 'and@gmail.com', 200)
    prog1 = Programmer ("Ivan", 'ivan@gmail.com', 100)
    prog2 = Programmer ('Vladimir', 'vlad@gmail.com', 100)
    cand1 = Candidate ('Sofia', 'sof@gmail.com', None, "oiu", 5)
    cand2 = Candidate ('Ann', 'ann@gmail.com', None, "oiu", 5)
    cand3 = Candidate ('Kate','kate@gmail.com', None, "oiu", 5)

    validate([rec1, prog1, prog2, cand1, cand2, cand3])


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        with open('log.txt', 'a') as f:
            message = '{}    {}:\n {} \n\n'.format(
                datetime.datetime.now(),
                err.__class__.__name__,
                traceback.format_exc()
            )
            f.write(message)
