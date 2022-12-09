def rev(s):
    half= len(s)//2
    s1 = s[:half][::-1]
    s2=s[half:][::-1]
    return f'{s1}{s2}'
x= input("enter:")
print(rev(x))    