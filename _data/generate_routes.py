import csv
import os

# Save directly into the collection folder
output_dir = "_taxi_routes"
os.makedirs(output_dir, exist_ok=True)

# Open routes.csv from the _data folder
with open("_data/routes.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        filename = f"{output_dir}/{row['from_slug']}-to-{row['to_slug']}-taxi.md"
        
        with open(filename, "w", encoding="utf-8") as out:
            out.write("---\n")
            out.write("layout: taxi_page\n") 
            
            # Dynamically write all CSV variables into the Front Matter
            for key, value in row.items():
                safe_value = value.replace('"', '\\"')
                out.write(f"{key}: \"{safe_value}\"\n")
            
            out.write(f"title: \"{row['from_location']} to {row['to_location']} Taxi Service | Tour With Anand\"\n")
            out.write(f"description: \"{row['unique_desc']}\"\n")
            
            # === THE NEW FUTURISTIC PERMALINK ===
            # This creates clean URLs like: /taxi/kochi-airport-to-munnar/
            out.write(f"permalink: /taxi/{row['from_slug']}-to-{row['to_slug']}/\n")
            out.write("---\n")
            
print(f"✅ Successfully generated new SEO landing pages inside {output_dir}/")