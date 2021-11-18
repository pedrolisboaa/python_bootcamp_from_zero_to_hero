def myfunc(mystring):
    new = []
    s = list(mystring.lower())
    n = 0
    for item in s:
        if n % 2 == 0:
            new.append(s[n].lower())
            n = n + 1
        else:
            new.append(s[n].upper())
            n = n + 1

    return ''.join(new)