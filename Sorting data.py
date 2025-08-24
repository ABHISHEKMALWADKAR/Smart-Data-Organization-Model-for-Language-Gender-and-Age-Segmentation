import pandas as pd

# Read the tab-separated text file into a DataFrame
df = pd.read_csv("D:\\PYTHON\\SOFTWARE DEVELOPMENT\\Final project\\Languages.txt", sep="\t")

# Get user input for gender
gender_input = input("Enter gender to filter (e.g., Female): ").strip()
age_input = input("Enter age to filter (e.g., 20): ").strip()
country_input = input("Enter country to filter (e.g., India): ").strip()
language_input = input("Enter language to filter (e.g., Hindi): ").strip()


# Filter the DataFrame by the given gender (case-insensitive)
filtered_df = df[
    (df['Gender'].str.lower() == gender_input.lower()) &
    (df['Age'].astype(str) == age_input) &
    (df['Country'].str.lower() == country_input.lower()) &
    (
    df['Native Language'].str.lower().str.contains(language_input.lower()) |
    df['Other Languages'].str.lower().str.contains(language_input.lower())
    )
]

# Write the filtered DataFrame to an Excel file
filtered_df.to_csv("D:\\PYTHON\\SOFTWARE DEVELOPMENT\\Final project\\Sorted data.csv", index=False)

print(f"Filtered data for gender '{gender_input}' saved to Sorted.csv")

