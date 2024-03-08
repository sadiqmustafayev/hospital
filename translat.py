from subprocess import call


call(["./manage.py", "makemessages","-l","az"])
call(["./manage.py", "compilemessages"])
