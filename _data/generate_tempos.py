import csv
import os

# 1. Create the dedicated collection folder
output_dir = "_tempo_routes"
os.makedirs(output_dir, exist_ok=True)

# 2. Open your CSV data file
csv_path = "_data/tempo_routes.csv"

# Fallback just in case you named it routes.csv
if not os.path.exists(csv_path):
    csv_path = "_data/routes.csv"

try:
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            # 3. Create the markdown filename
            filename = f"{output_dir}/kochi-to-{row['to_slug']}-tempo.md"
            
            with open(filename, "w", encoding="utf-8") as out:
                out.write("---\n")
                out.write("layout: tempo_page\n")
                
                # 4. Dynamically write all CSV variables safely into the Front Matter
                for key, value in row.items():
                    if value is None:
                        value = ""
                    
                    # Bulletproof fix: If Python accidentally reads a list due to extra commas, join it back into a string
                    if isinstance(value, list):
                        value = ", ".join(value)
                        
                    # Safely escape any double quotes inside your text so it doesn't break Jekyll
                    safe_value = str(value).replace('"', '\\"')
                    
                    out.write(f'{key}: "{safe_value}"\n')
                
                # 5. Write the consolidated, clean SEO permalink
                out.write(f'permalink: /tempo-traveller/kochi-to-{row["to_slug"]}/\n')
                out.write("---\n")
                
            print(f"✅ Generated: {filename}")

    print(f"\n🎉 SUCCESS: All Tempo Traveller & Urbania PSEO pages generated in {output_dir}/")

except FileNotFoundError:
    print(f"❌ ERROR: Could not find the CSV file at {csv_path}. Please make sure your data file is uploaded.")