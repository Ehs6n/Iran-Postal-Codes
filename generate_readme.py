import json
import glob

rows = []
for file in sorted(glob.glob("Alborz.json")):
    with open(file, "r") as f:
        data = json.load(f)
        for entry in data:
            rows.append(
                f"| {entry['provinceCode']} | {entry['townshipName']} | {entry['townshipCode']} |"
            )

markdown = "| Province Code | City Name | Zip Code |\n| --- | --- | --- |\n" + "\n".join(rows)
with open("README.md", "w") as md_file:
    md_file.write(markdown)
