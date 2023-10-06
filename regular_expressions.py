############################ search(): finds only the first occurance ################################

# step-1
import re 

text ='ABC 123 XYZ 456 @&! 100'

# step-2
pattern = re.compile(r'\d\d\d')

# step-3
match = pattern.search(text) 

print(match) # o/p: <re.Match object; span=(4, 7), match='123'> matched at 4 to 7th index

############################## finditer(): using finditer() returns a iterator object ##########################

# step-1
import re 

text ='ABC 123 XYZ 456 @&! 100'

# step-2
pattern = re.compile(r'\d\d\d')

# step-3
match = pattern.search(text) 

# step-4
find_all_occurance = pattern.finditer(text)

print(find_all_occurance) # <callable_iterator object at 0x00000221875B0AF0>

for match in find_all_occurance:
    print(match)
    # <re.Match object; span=(4, 7), match='123'>
    # <re.Match object; span=(12, 15), match='456'>
    # <re.Match object; span=(20, 23), match='100'>

    print(match.group())
    # 123
    # 456
    # 100

############################## characters for regex ##########################

# \d = matches digits from 0 - 9
# \w = matches any letter, digit, underscore
# \s = matches any space, tab, newline character
# \D = reverse of \d
# \W = reverse of \w
# \S = reverse of \s

#  \d 
text = "abc123"
pattern = re.compile('\d\d')
result = pattern.search(text)
print(result) # <re.Match object; span=(3, 5), match='12'>

# \w
pattern = re.compile('\w\w')
result = pattern.search(text)
print(result) # <re.Match object; span=(0, 2), match='ab'>

pattern = re.compile('\w\w')
iter_result = pattern.finditer(text)
print(iter_result) # <callable_iterator object at 0x000001773C589250>

for result in iter_result:
    print(result)
    #  <re.Match object; span=(0, 2), match='ab'>
    #  <re.Match object; span=(2, 4), match='c1'>
    #  <re.Match object; span=(4, 6), match='23'>

# unable to find special chars
special_char_text = "%$@"
pattern = re.compile(r'\w\w')
res = pattern.search(special_char_text)
print(res)

# \s
text_with_space = "harish Somsole"
pattern = re.compile(r"\s")
res = pattern.search(text_with_space)
print(res) # <re.Match object; span=(6, 7), match=' '>

text_with_mul_spaces = "harish Somsole   "
pattern = re.compile(r"\s\s")
res = pattern.search(text_with_mul_spaces)
print(res) # <re.Match object; span=(14, 16), match='  '>

# \D
text_with_spl_chars = "123$!*bc%@"
pattern = re.compile(r"\D\D\D")
res = pattern.search(text)
print(res) # <re.Match object; span=(3, 6), match='$!*'>

text_with_dsspc = "123 har!sh"
pattern = re.compile(r"\D\D\D\D")
res = pattern.search(text_with_dsspc)
print(res) # <re.Match object; span=(3, 7), match=' har'>

# \S
text_with_spaces = "   123"
pattern = re.compile('\S\S\S')
res = pattern.search(text_with_spaces)
print(res) # <re.Match object; span=(3, 6), match='123'>

# \W
text_with_spaces_and_special_chars = "123abc #@"
pattern = re.compile('\W\W\W')
res = pattern.search(text_with_spaces_and_special_chars)
print(res) # <re.Match object; span=(6, 9), match=' #@'>

##################################################### Symbol chars ###############################################

# () = groups multiple patterns into one => (r'\d\d\d')

# +  = matches 1 or more pattern => \d+

# *  = matches 0 or more => \d*

# {} = repeat specific pattern multiple times => \d{3}, \d{3,5} matches min of 3 digts and max of 5 digits, \d{3,} min 3 to any max

# ?  = optional search or returns shortest possible match => (HiHiHi){1,3}? -> Hi

# .  = matches any characters other than newline => \d.\d (2&3, 2D2,2%2)

# [] = matches all the characters specified within square brackets => [a-zA-Z0-9],[aeiou][0-9][!@#$]

#  | = matches either of the chars (\d|[a-z]) => 4, b

# ^ = caret symbol. Matches the pattern in the beginning of text or in [^abc] it tells not to match pattern in square brackets
        # Ex: ^\d\w\w => 2ab, [^abc] = def

# $ = matches the pattern end of the text (\d\d\d$) => 123


###############   EX-1   #######################################

text = '''
Hi, today is 17-Apr-2021, yesterday was 16-Apr-2021 and tommorrow will be 18-Apr-2021.
My Schedule is free on 26-04-2021, 06.05.2021 and 16/Jun/2021.
You can reach out to me at myname2020@dummy.com or ask_help@demo.net & conference@demo.co.in
you can also call me at one of the following no's +6032-007 1212, +6099.100 3344, 017-9998800 etc. 
'''

# 1. find all dates

# pattern = re.compile(r'\d\d-[A-Za-z]{3}-\d\d\d\d')
# pattern = re.compile(r'\d{2}-[A-Za-z]{3}-\d{4}')

pattern = re.compile(r'\d{2}[./-]([A-Za-z]{3}|\d{2})[./-]\d{4}')

matches_obj = pattern.finditer(text)

for match in matches_obj:
    print(match.group())

# output
# 17-Apr-2021
# 16-Apr-2021
# 18-Apr-2021
# 26-04-2021
# 06.05.2021
# 16/Jun/2021

# 2. find all emails

pattern = re.compile(r'\w+@[a-z]+(\.[a-z]{2,3})+')
matches_obj = pattern.finditer(text)
for match in matches_obj:
    print(match.group())

# output:
# myname2020@dummy.com
# ask_help@demo.net
# conference@demo.co.in

# 3. phone numbers
# +6032-007 1212, +6099.100 3344, 017-9998800

pattern = re.compile(r'(\+\d)?\d{3}[-.]\d{3}(\s?\d{3,4})')
matches_obj = pattern.finditer(text)
for match in matches_obj:
    print(match.group())

# output
# +6032-007 1212
# +6099.100 3344
# 017-9998800
   


############################## EX - 2 (^, $, *) #####################################

text = "Hi, how r u?"

# match a text which starts with 'Hi' and ends with '?'

pattern = re.compile(r"^(Hi).*\?$")
res = pattern.search(text)
print(res) # <re.Match object; span=(0, 12), match='Hi, how r u?'>


###################### sub() substitute ###########################

text = "My income in 2019 was $85,000 but now it is $120,000"

pattern = re.compile(r'\$[0-9,]+')
new_replaced_txt = pattern.sub('****', text)
print(new_replaced_txt) # My income in 2019 was **** but now it is ****


#################################### findall() ##############################

text = "My income in 2019 was $85,000 but now it is $120,000"
pattern = re.compile(r'\$[0-9,]+')
res = pattern.findall(text)
print(res)

# output:
# ['$85,000', '$120,000']