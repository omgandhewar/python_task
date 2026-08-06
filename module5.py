print("------ Memory Detective ------")

v1 = int(input("Enter value for v1: "))
v2 = int(input("Enter value for v2: "))
v3 = int(input("Enter value for v3: "))

print("\nValues")
print("v1 =", v1)
print("v2 =", v2)
print("v3 =", v3)

print("\nMemory Addresses")
print("id(v1) =", id(v1))
print("id(v2) =", id(v2))
print("id(v3) =", id(v3))

if id(v1) == id(v3):
    print("\nv1 and v3 point to the same memory location.")
else:
    print("\nv1 and v3 point to different memory locations.")