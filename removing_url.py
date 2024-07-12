import pandas as pd
import re

# Load the Excel file
df = pd.read_excel('modifi_emoji_file.xlsx')

# Function to remove URLs and "\t" from the end of each text using regex
def clean_text(text):
    # Define regex pattern to match URLs at the end of the text
    url_pattern_end = r' http[s]?://\S+$'
    # Remove URLs from the end of each text
    text = re.sub(url_pattern_end, '', text)
    # Remove "\t" from the text
    text = text.replace('\t', '')
    return text

# Apply the function to the desired column
df['TEXT'] = df['TEXT'].apply(clean_text)

# Save the modified DataFrame back to Excel
df.to_excel('url.xlsx', index=False)

print("URLs and '\\t' at the end of texts removed and Excel file saved successfully.")

