#! /usr/bin/python3

import re, pyperclip

# TODO: Create regex for phone numbers
phoneRegex = re.compile(r'''
       (
       ((\d\d\d) | (\(\d\d\d\)))?   # area code (optional)
       (\s | -)                     # first separator
       \d\d\d                       # first 3 digits
       (\s | -)                     # second separator
       \d\d\d\d                     # last 4 digits
       ((ext(\.)?\s | x)    \d{5})? # extension (optional)
       )
        
        ''', re.VERBOSE)

# TODO: Create regex for emails
emailRegex = re.compile(r'''
    [a-zA-Z0-9_.+]+  # name part
    @                # symbol
    [a-zA-Z0-9_.+]+  # domain
    
''', re.VERBOSE)

# TODO: Get the text off clipboard
text = pyperclip.paste()
print(text)

# TODO: Extract the email/phone from the text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

phoneNumbers = []
for number in extractedPhone:
    phoneNumbers.append(number[0])

# TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(phoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

