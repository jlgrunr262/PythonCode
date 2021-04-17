import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex2 = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 415-555-1212.')
mo2 = phoneNumRegex2.search('My cell number is 203-555-6969')
print('Phone number found: ' + mo.group())
print('The other search yields: ' + mo2.group())

phoneNumRegex3 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo3 = phoneNumRegex3.search('My office number is 602-965-2323')
print('The area code is: ' + mo3.group(1))
print('The prefix and number is: '+ mo3.group(2))
print('There are 2 ways to print the full number: ' + mo3.group(0) + ' ' + mo3.group())