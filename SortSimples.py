A, B, C = map(int, input("").split())

cont1 = int(A)
cont2 = int(B)
cont3 = int(C)

if A <= B and A <= C:
	print(A)
elif B <= A and B <= C:
	print(B)
elif C <= A and C <=B:
	print(C)

if A >= B and A <= C:
	print(A)
elif A <= B and A >= C:
	print(A)
elif B >= A and B <= C:
	print(B)
elif B <= A and B >= C:
	print(B)
elif C >= A and C <= B:
	print(C)
elif C <= A and C >= B:
	print(C)

if A >= B and A >= C:
	print(A)
elif B >= A and B >= C:
	print(B)
elif C >= A and C >= B:
	print(C)

print(f"\n{cont1}\n{cont2}\n{cont3}")