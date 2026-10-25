from itertools import islice
import csv
with open("buildings.csv", encoding = "utf-8-sig") as f:
    reader = list(islice(csv.DictReader(f), 1000000))
print(f"Number of rows: {len(reader)}")
print(f"The columns are: {list(reader[0].keys())}")

with open("reduced_buildings.csv", 'w', newline = '', encoding = "utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames = reader[0].keys())
    writer.writeheader()
    writer.writerows(reader)

values = []
for row in reader:
    value = float(row['area_in_meters'])
    values.append(value)

print(f"\nSmallest: {min(values)}\nLargest: {max(values)}\nCount: {len(values)}\n")

items = []
for row in reader:
    item = row['area_in_meters'].strip()
    if item == "":
        continue
    items.append(float(item))
print(f"Smallest: {min(items)}\nLargest: {max(items)}\nCount: {len(items)}\n")

def inspect_column(filename, column):
    with open(filename, encoding = 'utf-8-sig' ) as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == '':
            continue
        values.append(float(raw))
    return{
        f"Smallest: {min(values)}",
        f"Largest: {max(values)}",
        f"Count: {len(values)}"
    }
area_result = inspect_column('reduced_buildings.csv', 'area_in_meters')
confidence_result = inspect_column('reduced_buildings.csv', 'confidence')

print(f"Area: {area_result}\nConfidence Level: {confidence_result}")