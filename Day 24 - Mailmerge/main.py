TEMPLATE_FILE = r"C:\PathSanitized\Starting Letter Template.txt"
NAMES_FILE = r"C:\PathSanitized\Names\List of Names.txt"
OUTPUT_DIR = r"C:\PathSanitized\Ready To Send"

with open(TEMPLATE_FILE, "r") as f:
    template = f.read()

with open(NAMES_FILE, "r") as f:
    names = [line.strip() for line in f if line.strip()]

for name in names:
    letter = template.replace("[name]", name)
    output_path = f"{OUTPUT_DIR}\\invite_{name}.txt"
    with open(output_path, "w") as f:
        f.write(letter)

print(f"Generated {len(names)} invites in '{OUTPUT_DIR}/'")
