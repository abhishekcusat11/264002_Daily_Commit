import re

s=str(input())
c=r"(1|8|9)......."


match = re.search(c, s)
if (match and len(s)==8):

    print("Valid")
else:
    print("Invalid")