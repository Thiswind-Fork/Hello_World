import pickle
name = str(raw_input("What is your name?"))
age = str(raw_input("How old are you??"))
colour = str(raw_input("What is your favourite colour?"))
food = str(raw_input("What is your favourite food?"))

my_list = [name + '\n', age + '\n', colour + '\n', food + '\n']
new_file = open('answers.pkl', 'w')
pickle.dump(my_list, new_file)
new_file.close()
