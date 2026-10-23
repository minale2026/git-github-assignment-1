import csv

# Fictional example data for learning purposes only.
# These records are not real people and must not be used for clinical decisions.
sample_records = [
    {"id": 1, "age_months": 12, "sex": "F", "weight_kg": 8.4},
    {"id": 2, "age_months": 18, "sex": "M", "weight_kg": 10.1},
    {"id": 3, "age_months": 24, "sex": "F", "weight_kg": 11.2},
    {"id": 4, "age_months": 30, "sex": "M", "weight_kg": 12.8},
    {"id": 5, "age_months": 36, "sex": "F", "weight_kg": 13.6},
]

output_file = "sample_data.csv"
fieldnames = ["id", "age_months", "sex", "weight_kg"]

with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(sample_records)

print(f"Created {output_file} with {len(sample_records)} fictional records.")
