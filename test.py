from subprocess import call

call(["./manage.py", "test" , "baseuser"])
call(["./manage.py", "test" , "core.tests.TestUrls"])
call(["./manage.py", "test" , "core.tests.TestContactForm"])

