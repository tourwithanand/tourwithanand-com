import csv
import os
from datetime import date

# 1. Save directly into the foolproof _posts folder
output_dir = "_posts"
os.makedirs(output_dir, exist_ok=True)

# Automatically get today's date for the Jekyll filename requirement
today = date.today().isoformat()

# Open routes.csv from the _data folder
with open("_data/routes.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        # 2. Add the date prefix to the filename (e.g., 2026-07-05-kochi-to-munnar.md)
        filename = f"{output_dir}/{today}-{row['from_slug']}-to-{row['to_slug']}-taxi.md"
        
        with open(filename, "w", encoding="utf-8") as out:
            out.write("---\n")
            out.write("layout: taxi_page\n") 
            
            # Dynamically write all CSV variables into the Front Matter
            for key, value in row.items():
                safe_value = value.replace('"', '\\"')
                out.write(f"{key}: \"{safe_value}\"\n")
            
            out.write(f"title: \"{row['from_location']} to {row['to_location']} Taxi Service | Tour With Anand\"\n")
            out.write(f"description: \"{row['unique_desc']}\"\n")
            
            # 3. THE MAGIC OVERRIDE: This stops it from acting like a blog post
            # and pushes it to the clean, futuristic URL!
            out.write(f"permalink: /taxi/{row['from_slug']}-to-{row['to_slug']}/\n")
            out.write("---\n")
            
print(f"✅ Successfully generated new SEO landing pages inside {output_dir}/")