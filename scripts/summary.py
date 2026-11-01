import csv
def read_rows(filename):
    with open(filename, encoding = 'utf-8-sig') as f:
        return list(csv.DictReader(f))

def clean_recorcds(rows, column):
    cleaned_values = []
    for row in rows:
        raw = row[column].strip()
        if raw == '':
            continue
        cleaned_values.append(float(raw))
    return cleaned_values

def summarize_column(cleaned_values):
    if len(cleaned_values) == 0:
        return {
            "Smallest": None,
            "Largest": None,
            "Count": 0,
            "Average": None
        }
    return {
        "Smallest": min(cleaned_values),
        "Largest": max(cleaned_values),
        "Count": len(cleaned_values),
        "Average": sum(cleaned_values) / len(cleaned_values)
    }

rows = read_rows('reduced_buildings.csv')
values = clean_recorcds(rows, 'area_in_meters')
result = summarize_column(values)
print(result)

def summarise_all(filename, column):
    rows = read_rows(filename)
    report = {}
    for col in column:
        cleaned_values = clean_recorcds(rows, col)
        report[col] = summarize_column(cleaned_values)
    return report
report = summarise_all('reduced_buildings.csv', ['area_in_meters', 'confidence'])
for col, stats in report.items():
    print(f"{col} | {stats}")