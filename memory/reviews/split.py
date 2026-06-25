from pathlib import Path
import re

INPUT_FILE = "reviews.md"
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

def sanitize_filename(name):
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    return name.strip()

current_title = None
current_content = []

with open(INPUT_FILE, encoding="utf-8") as f:
    for line in f:
        stripped = line.strip()

        if stripped.startswith("## "):
            if current_title:
                (OUTPUT_DIR / f"{sanitize_filename(current_title)}.md").write_text(
                    "".join(current_content),
                    encoding="utf-8"
                )

            current_title = stripped[3:].strip()
            current_content = [line]

        elif current_title:
            current_content.append(line)

if current_title:
    (OUTPUT_DIR / f"{sanitize_filename(current_title)}.md").write_text(
        "".join(current_content),
        encoding="utf-8"
    )

print("Découpage terminé.")