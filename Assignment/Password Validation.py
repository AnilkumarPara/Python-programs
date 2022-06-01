password=input('Please provide the password')
if not (len(password)>=6 and len(password)<=16):
    print("Invalid password, Password should be a minimum of 6 and maximum of 16 chanracters")
else:
    a=0
    small_let=list(range(97,123))
    A=0
    cap_let=list(range(65,91))
    s=0
    sp_char=['$','#','@']
    n=0
    for c in password:
        if c.isdigit():
            if n==0:
                print("in digit")
                n=1
        else:
            if a==0 and (ord(c) in small_let):
                    print("in lower")
                    a=1
            elif A==0 and ord(c) in cap_let:
                    print("in upper")
                    A=1
            elif s==0 and c in sp_char:
                    print("in special")
                    s=1
    print(a,A,s,n)
    if a==1 and A==1 and s==1 and n==1:
        print("User has entered the correct password")
    else:
        print("Invalid password, Password should contain 1 lower case and 1 upper case letter, at least 1 special character [$#@] and At least 1 number between [0-9]")

