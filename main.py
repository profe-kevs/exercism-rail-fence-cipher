def encode(message, rails):
    message = message.replace(' ', '')
    r = [[] for i in range(rails)]

    go_down = True
    go_up = False
    mod = 0
    for i, ch in enumerate(message):

        if(mod == rails - 1):
            go_up = True
            go_down = False

        if(mod == 0):
            go_up = False
            go_down = True
        
        # For DEBUG:
        # print("i", i)
        # print("mod", mod)
        # print("down", go_down)
        # print("up", go_up)
        # print("-------")
        
        r[mod].append(ch)
        
        if(go_down):
            mod = mod + 1
        if(go_up):
            mod = mod - 1
        


        

    return ''.join([item for sub_list in r for item in sub_list])
    


def decode(encoded_message, rails):
    encoded_message = encoded_message.replace(' ', '')
    
    r = [[] for _ in range(rails)]

    go_down = True
    go_up = False
    mod = 0
    for i, ch in enumerate(encoded_message):

        if(mod == rails - 1):
            go_up = True
            go_down = False

        if(mod == 0):
            go_up = False
            go_down = True
        
        
        r[mod].append(1)
        
        if(go_down):
            mod = mod + 1
        if(go_up):
            mod = mod - 1

    # print(r)
    lenghts = [len(item) for item in r]
    # print(lenghts)
    message = ""
    acum = 0
    for i, l in enumerate(lenghts):
        print(encoded_message[acum:l + acum])
        r[i] = encoded_message[acum:l + acum]
        acum = acum + l

    
    go_down = True
    go_up = False
    mod = 0
    for i, ch in enumerate(encoded_message):

        if(mod == rails - 1):
            go_up = True
            go_down = False

        if(mod == 0):
            go_up = False
            go_down = True
        
        
        message = message + r[mod][0]

        r[mod] = r[mod][1:]
        
        if(go_down):
            mod = mod + 1
        if(go_up):
            mod = mod - 1
        

    return message


print(decode("TEITELHDVLSNHDTISEIIEA", 3))