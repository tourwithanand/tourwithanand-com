import csv
import os

# 1. Create the dedicated folder for the generated tour pages
output_dir = "_tours"
os.makedirs(output_dir, exist_ok=True)

# 2. Path to your correct CSV file
csv_path = "_data/tours_data.csv"

try:
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            # 3. Create the markdown filename using the package_slug
            filename = f"{output_dir}/{row['package_slug']}.md"
            
            with open(filename, "w", encoding="utf-8") as out:
                out.write("---\n")
                # Ensure this matches whatever you named your HTML file in the _layouts folder
                out.write("layout: kerala_tours_layout\n")
                
                # 4. Dynamically write all CSV variables safely into the Front Matter
                for key, value in row.items():
                    if value is None:
                        value = ""
                    
                    if isinstance(value, list):
                        value = ", ".join(value)
                        
                    # Safely escape any double quotes inside your text so it doesn't break Jekyll
                    safe_value = str(value).replace('"', '\\"')
                    
                    out.write(f'{key}: "{safe_value}"\n')
                
                # 5. Write the SEO permalink requested for foreign tourists
                out.write(f'permalink: /south-india-tours/{row["package_slug"]}/\n')
                out.write("---\n")
                
            print(f"✅ Generated: {filename}")

    print(f"\n🎉 SUCCESS: All Kerala Tour PSEO pages generated in {output_dir}/")

except FileNotFoundError:
    print(f"❌ ERROR: Could not find the CSV file at {csv_path}. Please check the filename.")