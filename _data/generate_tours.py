import csv
import os

# Create a new collection directory for tour packages to keep them separate from taxis and blogs
output_dir = "_tour_packages"
os.makedirs(output_dir, exist_ok=True)

# Read the tours data CSV
csv_file_path = "_data/tours_data.csv"

try:
    with open(csv_file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            filename = f"{output_dir}/{row['package_slug']}.md"
            
            with open(filename, "w", encoding="utf-8") as out:
                out.write("---\n")
                
                # This will link to the new layout we build next
                out.write("layout: tour_page\n")
                
                # Dynamically write all CSV columns into the Front Matter
                for key, value in row.items():
                    # Escape quotes inside text to prevent YAML build errors
                    safe_value = value.replace('"', '\\"')
                    out.write(f"{key}: \"{safe_value}\"\n")
                
                # Set SEO title, description, and the critical Hub-and-Spoke permalink
                out.write(f"title: \"{row['package_name']} | Tour With Anand\"\n")
                out.write(f"description: \"{row['meta_desc']}\"\n")
                out.write(f"permalink: /south-india-tours/{row['package_slug']}/\n")
                
                out.write("---\n")
                
    print(f"✅ Successfully generated Tour Package landing pages inside {output_dir}/")
except FileNotFoundError:
    print(f"❌ Error: Could not find {csv_file_path}. Please ensure your CSV is saved in the _data folder.")
