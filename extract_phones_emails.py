import re
import pyperclip

text = pyperclip.paste()


phone_number_regex = re.compile(r'(\d{3}|\(\d{3}\))?-(\d{3})-(\d{4})')  # creating the regex object for phone number patterns

email_regex = re.compile(r"[\w.-]+@[a-zA-Z]+(?:\.[a-z]+)+") # regex object for email pattern

phone_numbres = phone_number_regex.findall(text) # returns all matched occurences of the pattern 
emails = email_regex.findall(text)

print("\nPhone numbers found :\n")
print(phone_numbres)

print("\n\nEmails found :\n")
print(emails)
