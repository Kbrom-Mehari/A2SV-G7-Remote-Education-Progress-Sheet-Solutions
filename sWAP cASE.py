def swap_case(s):
    x = ""
    for ch in s:
        if(ch.islower()):
            x += ch.upper()
        elif(ch.isupper()):
            x += ch.lower()
        else:
            x += ch
    return x
