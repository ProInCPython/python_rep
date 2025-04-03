import re
f = open("text.txt", "r")
s = f.readline()

emails = re.findall("[\w.-]+@[\w.-]+\.\w+", s) # символы@символы.символы
phone_numbers = re.findall("\+7-\d{3}-\d{3}-\d{2}-\d{2}", s)
capital_words = re.findall("[A-Z]\w+", s)

print(*emails)
print(*phone_numbers)
print(*capital_words)

emails_f = open("emails.txt", "w")
numbers_f = open("phones.txt", "w")
capital_words_f = open("capital_words.txt", "w")

emails_f.write(" ".join(emails))
numbers_f.write(" ".join(phone_numbers))
capital_words_f.write(" ".join(capital_words))

emails_f.close()
numbers_f.close()
capital_words_f.close()


f.close()
