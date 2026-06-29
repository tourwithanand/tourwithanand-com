import csv
import os
from datetime import date

# 1. Look "up" one level from _data and save directly into the _posts folder
output_dir = "../_posts"
os.makedirs(output_dir, exist_ok=True)

# 2. Get today's date for Jekyll's required naming format
today_date = date.today().strftime("%Y-%m-%d")

# 3. Open your routes.csv file
with open("routes.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        # 4. Add the date prefix to the filename so Jekyll processes it!
        filename = f"{output_dir}/{today_date}-{row['from_slug']}-to-{row['to_slug']}-taxi.md"
        
        with open(filename, "w", encoding="utf-8") as out:
            out.write("---\n")
            out.write("layout: taxi_page\n") 
            
            for key, value in row.items():
                out.write(f"{key}: \"{value}\"\n")
            
            out.write(f"title: \"{row['from_location']} to {row['to_location']} Taxi Service | Tour With Anand\"\n")
            out.write(f"description: \"{row['unique_desc']}\"\n")
            
            # The permalink overrides the _posts folder, putting the live URL exactly where you want it
            out.write(f"permalink: /24x7-kochi-airport-taxi-service/{row['from_slug']}-to-{row['to_slug']}-taxi/\n")
            out.write("---\n")
            
print("✅ Successfully generated Jekyll files in the _posts folder with date prefixes!")