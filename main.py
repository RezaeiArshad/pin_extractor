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
        last_index = -1
        for line in lines:  
            words = line.split(' ')        
            if words[last_index]:
                if mode == 'first_letter':
                    secret_message.append(words[last_index][0])
                elif mode == 'last_letter':
                    secret_message.append(words[last_index][-1])
            last_index -= 1
    elif pattern == 'zigzag':
        last_index = -1        
        for index_of_line, line in enumerate(lines):
            words = line.split(' ') 
            if index_of_line == 0 or index_of_line % 2 == 0:
                if len(words) > index_of_line:
                    if mode == 'first_letter':
                        secret_message.append(words[index_of_line][0])
                    elif mode == 'last_letter':                    
                        secret_message.append(words[index_of_line][-1]) 
            elif index_of_line % 2 == 1:
                if words[last_index]:
                    if mode == 'first_letter':
                        secret_message.append(words[last_index][0])
                    elif mode == 'last_letter':
                        secret_message.append(words[last_index][-1])
                last_index -= 1       
    return ''.join(secret_message)

print(message_finder('hello\nand interesting', 'diagnal', 'first_letter'))
print(message_finder('abduct\nwhen truth dies\nalibi wont talk\nmess to be made', 'reverse_diagnal', 'last_letter'))
print(message_finder("well I'm out\nsee you maybe", 'zigzag', 'first_letter'))