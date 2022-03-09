import re
from sys import argv

#have to found out if there is an input
try:
    input_text = str(argv[1])
except:
    print("No input.")
    exit(1)

#whitelisting with regex
if re.search("^Hello$", input_text):
    print(argv[1])
else:
    print("Wrong input. Has to be Hello.")

#blacklisting
#trying to catch all mistakes
if len(input_text) == 5:
    if not input_text.isdigit():
        if input_text.startswith("H"):
            if input_text.endswith("o"):
                #insufficient...can print Hallo
                print(input_text)
            else:
                print("Error end.")
        else:
            print("Error start.")
    else:
        print("Error digits")
else:
    print("Error lenght")