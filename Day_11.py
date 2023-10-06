


# Step 1 Create regex for Phone number.

import  re

text = """

# Put Your text here

"""
phoneRegex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?   # area code
                        (\s|-|\.)?           # seprator
                        (\d{3})              # first three disit
                        (\s|-|\.)            # seprator
                        (\d{4})              # last four digits
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?                        
)''', re.VERBOSE)


# Step 2 creating regex for email.

emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+=]+     # username
                        @
                        [a-zA-Z.-]+          # domain name
                        (\.[a-zA-Z]{2,4})    # dot something

)''', re.VERBOSE)

matches = []
for groups in phoneRegex.findall(text):
    phoneNumber = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNumber += ' x' + groups[8]
    matches.append(phoneNumber)
for groups  in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    text = '\n'.join(matches)
    print("text is processing")
    print(text)
else:
    print(f"No Phone number or Email address is found.")    
    
