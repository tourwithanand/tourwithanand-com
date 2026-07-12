import csv
import os

# Save directly into the group travel collection folder
output_dir = "_tempo_routes"
os.makedirs(output_dir, exist_ok=True)

# Open the tempo_routes.csv from the _data folder
with open("_data/tempo_routes.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        filename = f"{output_dir}/kochi-to-{row['destination_slug']}-tempo.md"
        
        with open(filename, "w", encoding="utf-8") as out:
            out.write("---\n")
            out.write("layout: tempo_page\n")
            
            # Dynamically write all CSV variables into the Front Matter
            for key, value in row.items():
                safe_value = value.replace('"', '\\"')
                out.write(f"{key}: \"{safe_value}\"\n")
            
            # The Title Tag explicitly mentions Ernakulam & Airport
            out.write(f"title: \"Tempo & Urbania Rentals: Kochi, Ernakulam & Airport to {row['destination_name']} | Tour With Anand\"\n")
            
            # === THE NEW CONSOLIDATED PERMALINK ===
            # This creates clean URLs like: /tempo-traveller/kochi-to-munnar/
            out.write(f"permalink: /tempo-traveller/kochi-to-{row['destination_slug']}/\n")
            
            out.write("---\n")
            
print(f"✅ Successfully generated Consolidated Group Travel pages inside {output_dir}/")