with  open("wards.csv") as f:
    lines = f.readlines()
print(f"Number of lines: {len(lines)}")
print("\n")

for line in lines:
    print(line.strip())
print("\n")

for line in lines[1:]:
    part = line.strip().split(",")
    ward = part[0]
    area = part[1]
    print(f"{ward} has an area of {area}")
print("\n")

for line in lines[1:]:
    part = line.strip().split(",")
    ward = part[0]
    area_km2 = float(part[1])
    area_hectares = area_km2 * 100
    print(f"{ward} is {area_hectares} hectares")
print("\n")

for line in lines[1:]:
    part = line.strip().split(",")
    ward = part[0]
    area_km2 = float(part[1])
    if area_km2 > 9:
        size = "Large"
    else:
        size = "Small"
    print(f"{ward} is {size}")
print("\n")

total = 0
def classify(area):
    if area > 9:
        return "large"
    else:
        return "small"

for line in lines[1:]:
    part = line.strip().split(",")
    ward = part[0]
    area_km2 = float(part[1])
    total += area_km2
    size = classify(area_km2)
    print(f"{ward} is {size}")
print(f"The total area is {total} square kilometers")
