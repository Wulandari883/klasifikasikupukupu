dataset_species = [
    "BANDED ORANGE HELICONIAN", "BECKERS WHITE", "BLACK HAIRSTREAK", "CABBAGE WHITE", "DANAID EGGFLY",
    "GREAT EGGFLY", "GREEN HAIRSTREAK", "GREY HAIRSTREAK", "HELICONIUS CHARITONIUS", "HELICONIUS ERATO",
    "JULIA", "PURPLE HAIRSTREAK", "VANESSA ATALANTA", "VANESSA CARDUI", "ULYSSES BUTTERFLY",
    "MONARCH BUTTERFLY", "BLUE MORPHO", "OLD WORLD SWALLOWTAIL", "PEACOCK BUTTERFLY", "SMALL TORTOISESHELL",
    "COMMA BUTTERFLY", "AMERICAN PAINTED LADY", "RED-SPOTTED PURPLE", "COMMON BUCKEYE", "SUMMER AZURE",
    "EASTERN TIGER SWALLOWTAIL", "SPICEBUSH SWALLOWTAIL", "BLACK SWALLOWTAIL", "PIPEVINE SWALLOWTAIL", "ZEBRA SWALLOWTAIL",
    "CLOUDLESS SULPHUR", "ORANGE SULPHUR", "CLOUDED SULPHUR", "SLEEPY ORANGE", "LITTLE YELLOW",
    "QUEEN BUTTERFLY", "GREAT SPANGLED FRITILLARY", "SMALL PEARL-BORDERED FRITILLARY", "PEARL CRESCENT", "SILVERY CHECKERSPOT",
    "BALTIMORE CHECKERSPOT", "QUESTION MARK BUTTERFLY", "MOURNING CLOAK", "VICEROY BUTTERFLY", "HACKBERRY EMPEROR",
    "TAWNY EMPEROR", "NORTHERN PEARLY-EYE", "LITTLE WOOD-SATYR", "COMMON RINGLET", "COMMON WOOD-NYMPH"
]

model_classes = [
    'adonis', 'american snoot', 'an 88', 'banded peacock', 'beckers white',
    'black hairstreak', 'cabbage white', 'chestnut', 'clodius parnassian', 'clouded sulphur',
    'copper tail', 'crecent', 'crimson patch', 'eastern coma', 'gold banded',
    'great eggfly', 'grey hairstreak', 'indra swallow', 'julia', 'large marble',
    'malachite', 'mangrove skipper', 'metalmark', 'monarch', 'morning cloak',
    'orange oakleaf', 'orange tip', 'orchard swallow', 'painted lady', 'paper kite',
    'peacock', 'pine white', 'pipevine swallow', 'purple hairstreak', 'question mark',
    'red admiral', 'red spotted purple', 'scarce swallow', 'silver spot skipper', 'sixspot burnet',
    'skipper', 'sootywing', 'southern dogface', 'straited queen', 'two barred flasher',
    'ulyses', 'viceroy', 'wood satyr', 'yellow swallow tail', 'zebra long wing'
]

print("Dataset species count:", len(dataset_species))
print("Model classes count:", len(model_classes))

print("\nModel classes NOT in dataset:")
for m in model_classes:
    matched = False
    for d in dataset_species:
        # Check direct or loose match
        d_clean = d.lower().replace(" butterfly", "").replace("-", " ")
        m_clean = m.lower().replace("-", " ")
        if d_clean == m_clean or m_clean in d_clean or d_clean in m_clean:
            matched = True
            break
    if not matched:
        print(f" - {m}")

print("\nDataset species NOT in model classes:")
for d in dataset_species:
    matched = False
    for m in model_classes:
        d_clean = d.lower().replace(" butterfly", "").replace("-", " ")
        m_clean = m.lower().replace("-", " ")
        if d_clean == m_clean or m_clean in d_clean or d_clean in m_clean:
            matched = True
            break
    if not matched:
        print(f" - {d}")
