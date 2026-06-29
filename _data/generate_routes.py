import csv
import os
from datetime import date

# Ensure the _posts folder exists in the root directory
output_dir = "_posts"
os.makedirs(output_dir, exist_ok=True)

# Get today's date for Jekyll's required naming format
today_date = date.today().strftime("%Y-%m-%d")

# Open routes.csv from the _data folder
with open("_data/routes.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        # Add the date prefix to the filename so Jekyll processes it as a live page
        filename = f"{output_dir}/{today_date}-{row['from_slug']}-to-{row['to_slug']}-taxi.md"
        
        with open(filename, "w", encoding="utf-8") as out:
            out.write("---\n")
            out.write("layout: taxi_page\n") 
            
            # Dynamically write all CSV variables into the Front Matter
            for key, value in row.items():
                # Escape double quotes in CSV text to prevent YAML errors
                safe_value = value.replace('"', '\\"')
                out.write(f"{key}: \"{safe_value}\"\n")
            
            # SEO Meta Data
            out.write(f"title: \"{row['from_location']} to {row['to_location']} Taxi Service | Tour With Anand\"\n")
            out.write(f"description: \"{row['unique_desc']}\"\n")
            
            # The permalink pushes the final live URL under your 24x7 service folder
            out.write(f"permalink: /24x7-kochi-airport-taxi-service/{row['from_slug']}-to-{row['to_slug']}-taxi/\n")
            out.write("---\n")
            
print(f"✅ Successfully generated new SEO landing pages inside {output_dir}/")