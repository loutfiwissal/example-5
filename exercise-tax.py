AGE=int(input("please enter your age: "))
S=input("please enter your sexe: ")
if S=="homme" and AGE>=20:
    print("pay tax")
elif S=="femme" and AGE>=18 and AGE<=35:
    print("pay tax")
else:
    print("do not pay tax")
