import time


file_name = 'notebook.txt'
while True:
    try:
        with open(file_name, 'x'):
            print('No default notebook was found, created one.')
    
    except Exception:
        pass
        
    try:
        action = int(input(f'''Now using file {file_name}\n(1)\
 Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4)\
 Change the notebook\n(5) Quit\n\nPlease select one: '''))
        
    except ValueError:
        print('Only number value!')
        action = 0
        
    if action == 1:
        with open(file_name) as read:
            print(read.read())
    elif action == 2:
        new_note = input('Write a new note: ')
        with open(file_name,'a') as add_note:
            note = add_note.write(new_note + ':::'
            + time.strftime("%X %x") + '\n')
    elif action == 3:
        with open(file_name, 'w'):
            print('Notes deleted.')
    elif action == 4:
        file_name = str(input('Give the name of the new file: '))
    elif action == 5:
        print('Notebook shutting down, thank you.')
        break
