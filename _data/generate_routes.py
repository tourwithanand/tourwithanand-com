import csv
import os

# Save directly into the new collection folder
output_dir = "_taxi_routes"
os.makedirs(output_dir, exist_ok=True)

# Open routes.csv from the _data folder
with open("_data/routes.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        # No date prefix needed for Collections!
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
            
            # The permalink pushes the final live URL exactly where you want it
            out.write(f"permalink: /24x7-kochi-airport-taxi-service/{row['from_slug']}-to-{row['to_slug']}-taxi/\n")
            out.write("---\n")
            
print(f"✅ Successfully generated new SEO landing pages inside {output_dir}/")
