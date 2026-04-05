# Calculate electricity bill using slabs

units = int(input("Enter total numbers of units consuem:"))

slab1 = 0
slab2 = 0
slab3 = 0
calBill = 0

if(units < 100):
    slab1  = units
else :
    slab1 = 100
    units = units - 100

if(units > 100):
    slab2 = 100
    units = units - 100
else:
    slab3 = units
    

slab3 = units

print(slab1, slab2, slab3)
calBill = slab1 * 5 + slab2 * 8 + slab3 * 10
print(f"Your Electricity bill is {calBill} Rs")


