from datetime import date
from subprocess import call

today = date.today().strftime("%d-%m-%Y")
x = f"Update {today}"

call(["sudo", "git", "add", "."])
call(["sudo", "git", "commit", "-m", "FINAL"])
call(["git", "push"])
