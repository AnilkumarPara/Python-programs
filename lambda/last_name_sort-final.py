# We have a list of names and we need to sort the names by last name of a person
names_1=['Anitha P', 'Avish Jain ', 'Narendra Modi', 'Sachin Tendulkar','Rahul Dravid']
print("--- Normal Function---")
fn_ln_list=[]
for name in names_1:
    fn_ln_list.append(name.split())


sorted_names=sorted(fn_ln_list,key=lambda fn_ln:fn_ln[-1])
final_sorted_names=[]
for fullname in sorted_names:
    final_sorted_names.append(' '.join(fullname))
print(final_sorted_names)


names_2=['Anitha P', 'Avish Jain ', 'Narendra Modi', 'Sachin Tendulkar','Rahul Dravid']
print("--- Lambda Function---")

names_2.sort(key=lambda name:name.split()[-1])
print(names_2)
