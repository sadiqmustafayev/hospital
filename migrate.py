from subprocess import call

call(["./manage.py", "makemigrations"])
call(["./manage.py", "migrate"])
call(["./manage.py", "runserver"])


