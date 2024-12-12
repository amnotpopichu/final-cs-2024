'''
import csv

# Set the index of the column to sort by (zero-based)
column_index = 2  # Change this to the column you want to sort by (e.g., 1 for second column)

# Read the CSV file into a list
with open('/Users/leohsia/Documents/coding projects/geomapping-median-salary/final/data.csv', mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Save the header row
    rows = list(reader)    # Read the rest of the rows

# Sort the rows by the specified column in descending order (largest to smallest)
# For numerical sorting, convert the values to float (or int) before sorting
sorted_rows = sorted(rows, key=lambda x: float(x[column_index]), reverse=True)

# Write the sorted rows back to a new CSV file
with open('sorted_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write the header
    writer.writerows(sorted_rows)  # Write the sorted data
'''

#sorter#2
import csv

# Open the original CSV file
with open('/Users/leohsia/Documents/coding projects/geomapping-median-salary/final/sorted_data.csv', mode='r') as infile:
    reader = csv.reader(infile)
    
    # Read all rows into a list
    rows = list(reader)

    # Separate header and data
    header = rows[0]  # Assuming the first row is the header
    data = rows[1:]   # The rest are data rows

    # Reverse the data rows
    reversed_data = list(reversed(data))

# Write to a new CSV file
with open('reversed_data.csv', mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    
    # Write the header first
    writer.writerow(header)
    
    # Write the reversed data
    writer.writerows(reversed_data)

print("Reversed data saved to 'reversed_data.csv'")
