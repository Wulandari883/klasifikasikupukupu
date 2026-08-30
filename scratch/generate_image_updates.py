import os

species_list = [
    "ADONIS",
    "AMERICAN SNOOT",
    "AN 88",
    "BANDED PEACOCK",
    "BECKERS WHITE",
    "BLACK HAIRSTREAK",
    "CABBAGE WHITE",
    "CHESTNUT",
    "CLODIUS PARNASSIAN",
    "CLOUDED SULPHUR",
    "COPPER TAIL",
    "CRECENT",
    "CRIMSON PATCH",
    "EASTERN COMA",
    "GOLD BANDED",
    "GREAT EGGFLY",
    "GREY HAIRSTREAK",
    "INDRA SWALLOW",
    "JULIA",
    "LARGE MARBLE",
    "MALACHITE",
    "MANGROVE SKIPPER",
    "METALMARK",
    "MONARCH",
    "MORNING CLOAK",
    "ORANGE OAKLEAF",
    "ORANGE TIP",
    "ORCHARD SWALLOW",
    "PAINTED LADY",
    "PAPER KITE",
    "PEACOCK",
    "PINE WHITE",
    "PIPEVINE SWALLOW",
    "PURPLE HAIRSTREAK",
    "QUESTION MARK",
    "RED ADMIRAL",
    "RED SPOTTED PURPLE",
    "SCARCE SWALLOW",
    "SILVER SPOT SKIPPER",
    "SIXSPOT BURNET",
    "SKIPPER",
    "SOOTYWING",
    "SOUTHERN DOGFACE",
    "STRAITED QUEEN",
    "TWO BARRED FLASHER",
    "ULYSES",
    "VICEROY",
    "WOOD SATYR",
    "YELLOW SWALLOW TAIL",
    "ZEBRA LONG WING"
]

sql_statements = []
for species in species_list:
    filename = species.lower().replace(" ", "_") + ".jpg"
    image_url = f"/assets/spesies/{filename}"
    sql = f"UPDATE spesies SET image_url = '{image_url}' WHERE nama_umum = '{species}';"
    sql_statements.append(sql)

output_path = os.path.join(os.path.dirname(__file__), "update_images.sql")
with open(output_path, "w") as f:
    f.write("\n".join(sql_statements) + "\n")

print(f"Generated SQL script with {len(sql_statements)} statements at {output_path}")
