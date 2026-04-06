# Calculate electricity bill using slabs (Breaking them into parts)

units = int(input("Enter total numbers of units consuem:"))

slab1 = 0
slab2 = 0
slab3 = 0
calBill = 0

# First 100 units → Rs 5 per unit
# Next 100 units → Rs 8 per unit
# Above 200 units → Rs 10 per unit

if(units <= 100):
    slab1  = units
    units = 0
else :
    slab1 = 100
    units = units - 100

if(units <= 100):
    slab2 = units
    units = 0
else:
    slab2 = 100
    units = units - 100
    
slab3 = units

print(slab1, slab2, slab3)
calBill = slab1 * 5 + slab2 * 8 + slab3 * 10
print(f"Your Electricity bill is {calBill} Rs")


