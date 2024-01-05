import pandas as pd

input_file_path = 'Exam_Table.csv'
df = pd.read_csv(input_file_path)

# Create a new column 'HRID' based on the concatenation of 'location', 'site', and 'replicate'
df['HRID'] = df.apply(lambda row: f"{row['Location']}-{row['Site']}-{row['Replicate']}".replace(',', '-'), axis=1)

output_file_path = 'b6_output6.csv'  
df.to_csv(output_file_path, index=False)

print(f"New file created with HRID column: {output_file_path}")