user_input = input("Enter yes or no: ")
## User input compare karne ke liye (case-insensitive comparison)

if user_input.lower() == "yes":
    print("You agreed!")


code = "ab12"
print(code.upper())
### Data normalize karna ho
### Codes compare karna ho 
##  Coupon codes, product IDs etc.


email = input("Enter email: ").strip()
## Real life me bahut important
## User form bharte waqt extra spaces daal deta hai. to remove spaces we use strip

text = "I hate bugs"
print(text.replace("hate", "love"))
### Word censoring, Data cleaning, File path fixing


data = "Joyi,20,Delhi"
info = data.split(",")
print(info)
## split() — Use Case --  Jab data ko todna ho
## CSV file reading, Input parsing, Sentence ko words me todna

words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)
## join() — Use Case -- Jab list ko wapas string banana ho
## Sentence banana, CSV file likhna, Data formatting

text = "Python is awesome"
if text.find("awesome") != -1:
    print("Word found")
## find() — Use Case -- Check karna ho ki koi word exist karta hai ya nahi
## Validation, Keyword search, Basic search system

password = "aaBBcc11"
print(password.count("a"))
## count() — Use Case -- Password validation
# Character frequency
# Data analysis



