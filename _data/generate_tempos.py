import csv
import os
import re

# Output folder
output_dir = "_tempo_routes"
os.makedirs(output_dir, exist_ok=True)

# CSV file
csv_path = "_data/tempo_routes.csv"
if not os.path.exists(csv_path):
    csv_path = "_data/routes.csv"


def make_slug(text):
    """Convert text to SEO-friendly slug."""
    if not text:
        return "unknown"
    text = text.lower().strip()
    text = text.replace("&", "and")
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text


try:
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:

            # Use existing to_slug if available; otherwise create one
            slug = row.get("to_slug", "").strip()

            if not slug:
                slug = make_slug(
                    row.get("to_location")
                    or row.get("destination")
                    or row.get("place")
                    or row.get("to")
                    or ""
                )

            filename = os.path.join(
                output_dir,
                f"kochi-to-{slug}-tempo.md"
            )

            with open(filename, "w", encoding="utf-8") as out:

                out.write("---\n")
                out.write("layout: tempo_page\n")

                for key, value in row.items():
                    if value is None:
                        value = ""
                    value = str(value).replace('"', '\\"')
                    out.write(f'{key}: "{value}"\n')

                out.write(f'to_slug: "{slug}"\n')
                out.write(f'permalink: /tempo-traveller/kochi-to-{slug}/\n')
                out.write("---\n")

            print(f"✅ Generated: {filename}")

    print(f"\n🎉 Successfully generated all Tempo Traveller pages in {output_dir}")

except FileNotFoundError:
    print(f"❌ CSV not found: {csv_path}")