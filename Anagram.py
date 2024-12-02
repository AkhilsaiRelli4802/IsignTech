def anagramcheck(string1,string2):
    str1=string1.lower()
    str2=string2.lower()
    if sorted(str1)==sorted(str2):
        return True
    else:
        return False
z=anagramcheck("Listen","Silent")
print(z)