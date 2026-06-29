import csv
import os

# 1. Create the folder for the generated markdown files
output_dir = "taxi-routes"
os.makedirs(output_dir, exist_ok=True)

# 2. Open your updated CSV file
with open("D2DPSEO.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    # 3. Loop through each row to create a dedicated page
    for row in reader:
        # Create a clean filename for the Markdown file
        filename = f"{output_dir}/{row['from_slug']}-to-{row['to_slug']}-taxi.md"
        
        with open(filename, "w", encoding="utf-8") as out:
            # Start the YAML Front Matter
            out.write("---\n")
            
            # Point to your middle-layer HTML layout
            out.write("layout: taxi_page\n") 
            
            # Dynamically write all variables from the CSV (including the 3 new ones)
            for key, value in row.items():
                out.write(f"{key}: \"{value}\"\n")
            
            # Write the crucial SEO variables required by Jekyll
            out.write(f"title: \"{row['from_location']} to {row['to_location']} Taxi Service | Tour With Anand\"\n")
            out.write(f"description: \"{row['unique_desc']}\"\n")
            
            # The nested permalink structure to build topic authority
            out.write(f"permalink: /24x7-kochi-airport-taxi-service/{row['from_slug']}-to-{row['to_slug']}-taxi/\n")
            
            # End the YAML Front Matter
            out.write("---\n")
            
print("✅ Successfully generated Jekyll route files with the nested Hub & Spoke URL structure!")
