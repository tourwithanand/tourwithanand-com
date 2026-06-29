import csv
import os

# 1. Ensure the taxi-routes folder exists for the .md files
output_dir = "taxi-routes"
os.makedirs(output_dir, exist_ok=True)

# 2. Open your updated D2DPSEO.csv file
with open("D2DPSEO.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    # 3. Loop through each row to create a dedicated Markdown file
    for row in reader:
        # Create a clean filename for the Markdown file
        filename = f"{output_dir}/{row['from_slug']}-to-{row['to_slug']}-taxi.md"
        
        with open(filename, "w", encoding="utf-8") as out:
            # Start the YAML Front Matter
            out.write("---\n")
            
            # Point to your middle-layer template (taxi_page.html)
            out.write("layout: taxi_page\n") 
            
            # Dynamically write all variables from the CSV
            for key, value in row.items():
                out.write(f"{key}: \"{value}\"\n")
            
            # SEO Metadata
            out.write(f"title: \"{row['from_location']} to {row['to_location']} Taxi Service | Tour With Anand\"\n")
            out.write(f"description: \"{row['unique_desc']}\"\n")
            
            # Nested permalink structure for topic authority
            # All generated pages will live under the /24x7-kochi-airport-taxi-service/ subpage
            out.write(f"permalink: /24x7-kochi-airport-taxi-service/{row['from_slug']}-to-{row['to_slug']}-taxi/\n")
            
            # End the YAML Front Matter
            out.write("---\n")
            
print("✅ Successfully generated all route files with nested URL structure!")
