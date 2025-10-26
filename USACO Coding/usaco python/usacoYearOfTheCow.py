zodiac_map = {
    "Ox": 0, "Tiger": 1, "Rabbit": 2, "Dragon": 3, "Snake": 4, 
    "Horse": 5, "Goat": 6, "Monkey": 7, "Rooster": 8, "Dog": 9, 
    "Pig": 10, "Rat": 11
}

input_lines = [
    "Mildred born in previous Dragon year from Bessie",
    "Gretta born in previous Monkey year from Mildred",
    "Elsie born in next Ox year from Gretta",
    "Paulina born in next Dog year from Bessie"
]


cow_years = { "Bessie": 0 }
cow_zodiacs = { "Bessie": "Ox" }
sum = 0

for line in input_lines:
    seg = line.split()
    name = seg[0]
    pn = seg[3]
    zodiac = seg[4]
    end_cow = seg[7]
    
    
    
    diff = zodiac_map[zodiac] - zodiac_map[cow_zodiacs[end_cow]]
    
    if pn == "previous":
        while diff >= 0:
            diff -= 12
    else:  
        while diff <= 0:
            diff += 12
    
    cow_years[name] = cow_years[end_cow] + diff
    cow_zodiacs[name] = zodiac

print(cow_years["Elsie"])