def message_finder(text, pattern='diagnal', mode='first_letter'):
    secret_message = []
    lines = text.split('\n')
    if pattern == 'diagnal':
       for index_of_line, line in enumerate(lines):
        words = line.split(' ')
        if len(words) > index_of_line:
            if mode == 'first_letter':
               secret_message.append(words[index_of_line][0])
            elif mode == 'last_letter':
               secret_message.append(words[index_of_line][-1])

    elif pattern == 'reverse_diagnal':
        last_index = len(lines[0].split(' ')) - 2

        for index_of_line, line in enumerate(lines):
            words = line.split(" ")           
            if words[last_index]:
                if mode == 'first_letter':
                    secret_message.append(words[last_index][0])
                elif mode == 'last_letter':
                    secret_message.append(words[last_index][-1])
            last_index -= 1

        
        
    return ''.join(secret_message)


print(message_finder('hello\nand interesting', 'diagnal', 'first_letter'))
    
print(message_finder('tell him\n turph i'))