import hashlib


def problem_choice(email, seminar, problems):
    email = email.strip().lower()
    assert "@minerva.kgi.edu" in email
    seminar = seminar.strip().lower()
    enc = (email + seminar).encode()
    md5 = hashlib.md5(enc).hexdigest()
    ind = int(md5, 16) % len(problems)
    return problems[ind]


if __name__ == '__main__':
    email = input('Please enter your student email address:')
    print('For seminar 3.2:')
    print(problem_choice(email, '3.2', ['2-Logging', '3-Graphics']))
