class AgeError(Exception):
    pass


class AvgScoreError(Exception):
    def __init__(self, score, subject, avr_score):
        self.score = score
        self.subject = subject
        self.avr_score = avr_score
        message = f"не відповідні данні між {self.score} / {self.subject} != {self.avr_score}"
        super().__init__(message)


user_result = {'id': 1, 'age': 45, 'avr_score': None, 'subject': 5, 'score': 334 }



def my_func(user_result: dict):
    age, score, subject, avg_subject = user_result['age'], user_result['score'], user_result['subject'], user_result['avr_score']
    if not(18 < age < 65):
        raise AgeError(f'Юзер має вік {age}, а має бути 18 до 65')
    if age == 45:
        raise AgeError('Юзеру 45 років')
    if score / subject != avg_subject:
        raise AvgScoreError(score, subject, avg_subject)

assert  1 == 0, 'цього не може бути'

# try:
my_func(user_result)

# except AgeError as e:
#     print(e)
#
# except Exception as e:
#     print(e)