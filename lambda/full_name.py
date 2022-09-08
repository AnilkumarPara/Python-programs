'''I have a web page where user creates a account, He enters first name and last name
Some Users enters with some spaces also
Finally when he logins in we need to  show the full_name'''
print("--- Normal Function---")
def full_name(first_name,last_name):
    first_name=first_name.strip()
    last_name=last_name.strip()
    return first_name.title()+" "+last_name.title()
print(full_name('sachin ',' Tendulkar '))

print("--- lambda Function---")
full_name_1=lambda first_name,last_name:((first_name.strip()).title())+" "+((last_name.strip()).title())
print(full_name_1('sachin ',' Tendulkar '))
