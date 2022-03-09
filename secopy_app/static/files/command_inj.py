import subprocess

hostname = '!'
password = "something"
input_password = input("Please enter your password: ")
if password == input_password:
  print("Logged!")
else:
  print("Incorect password!")


#subprocess.Popen([ 'nslookup', hostname ], ... , shell=False)
