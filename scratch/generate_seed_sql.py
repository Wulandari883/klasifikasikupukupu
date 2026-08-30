import json

# Actual 50 classes from model
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

# Scientific names mapping
scientific_names = {
    'adonis': 'Lysandra bellargus',
    'american snoot': 'Libytheana carinenta',
    'an 88': 'Diaethria clymena',
    'banded peacock': 'Papilio palinurus',
    'beckers white': 'Pontia beckerii',
    'black hairstreak': 'Satyrium pruni',
    'cabbage white': 'Pieris rapae',
    'chestnut': 'Ariadne merione',
    'clodius parnassian': 'Parnassius clodius',
    'clouded sulphur': 'Colias philodice',
    'copper tail': 'Lycaena pyrrhogaster',
    'crecent': 'Phyciodes tharos',
    'crimson patch': 'Chlosyne janais',
    'eastern coma': 'Polygonia comma',
    'gold banded': 'Autochton cellus',
    'great eggfly': 'Hypolimnas bolina',
    'grey hairstreak': 'Strymon melinus',
    'indra swallow': 'Papilio indra',
    'julia': 'Dryas iulia',
    'large marble': 'Euchloe ausonides',
    'malachite': 'Siproeta stelenes',
    'mangrove skipper': 'Phocides pigmalion',
    'metalmark': 'Calephelis borealis',
    'monarch': 'Danaus plexippus',
    'morning cloak': 'Nymphalis antiopa',
    'orange oakleaf': 'Kallima inachus',
    'orange tip': 'Anthocharis cardamines',
    'orchard swallow': 'Papilio aegeus',
    'painted lady': 'Vanessa cardui',
    'paper kite': 'Idea leuconoe',
    'peacock': 'Aglais io',
    'pine white': 'Neophasia menapia',
    'pipevine swallow': 'Battus philenor',
    'purple hairstreak': 'Favonius quercus',
    'question mark': 'Polygonia interrogationis',
    'red admiral': 'Vanessa atalanta',
    'red spotted purple': 'Limenitis arthemis',
    'scarce swallow': 'Iphiclides podalirius',
    'silver spot skipper': 'Epargyreus clarus',
    'sixspot burnet': 'Zygaena filipendulae',
    'skipper': 'Hesperiidae',
    'sootywing': 'Pholisora catullus',
    'southern dogface': 'Zerene cesonia',
    'straited queen': 'Danaus eresimus',
    'two barred flasher': 'Astraptes fulgerator',
    'ulyses': 'Papilio ulysses',
    'viceroy': 'Limenitis archippus',
    'wood satyr': 'Megisto cymela',
    'yellow swallow tail': 'Papilio rutulus',
    'zebra long wing': 'Heliconius charithonia'
}

# Indonesian descriptions from ClassificationTab
descriptions = {
  "adonis": "Kupu-kupu berwarna biru cerah pada bagian atas sayap jantan dengan pola hitam di tepinya.",
  "american snoot": "Memiliki ciri khas moncong panjang yang menyerupai paruh kecil pada bagian kepala.",
  "an 88": "Memiliki pola unik menyerupai angka 88 pada bagian bawah sayap.",
  "banded peacock": "Memiliki warna hijau metalik dengan pita gelap melintang pada sayap.",
  "beckers white": "Kupu-kupu berwarna putih dengan bercak gelap halus di bagian ujung sayap.",
  "black hairstreak": "Memiliki warna cokelat gelap dengan garis oranye kecil dan ekor halus di bagian sayap belakang.",
  "cabbage white": "Kupu-kupu putih kecil yang umum ditemukan dengan bintik hitam kecil di sayap depan.",
  "chestnut": "Memiliki warna cokelat kemerahan menyerupai kastanye dengan motif yang sederhana.",
  "clodius parnassian": "Memiliki sayap putih transparan dengan bintik merah dan hitam yang khas.",
  "clouded sulphur": "Kupu-kupu berwarna kuning terang dengan tepian sayap berwarna hitam gelap.",
  "copper tail": "Memiliki ekor berwarna tembaga kemerahan yang berkilau di bagian bawah sayap.",
  "crecent": "Kupu-kupu kecil dengan pola warna jingga-hitam menyerupai bulan sabit.",
  "crimson patch": "Memiliki bercak merah tua (crimson) yang mencolok pada sayap hitamnya.",
  "eastern coma": "Memiliki sayap bergelombang dengan tanda putih menyerupai tanda koma di bagian bawah sayap.",
  "gold banded": "Kupu-kupu dengan pita berwarna emas kekuningan yang melintang di sayap cokelat gelapnya.",
  "great eggfly": "Memiliki pola bercak besar pada sayap dengan motif melingkar biru-putih yang khas pada jantan.",
  "grey hairstreak": "Sayap berwarna abu-abu dengan bintik oranye kecil dan ekor tipis di bagian belakang.",
  "indra swallow": "Kupu-kupu hitam besar dengan ekor khas swallowtail dan barisan bintik kuning krem.",
  "julia": "Memiliki sayap oranye terang yang memanjang dengan motif garis hitam tipis.",
  "large marble": "Memiliki pola guratan hijau-putih seperti marmer di bagian bawah sayap.",
  "malachite": "Berwarna hijau muda berkilau menyerupai batu malakit dengan pola hitam kontras.",
  "mangrove skipper": "Kupu-kupu berbadan kokoh dengan warna cokelat dan kilauan biru di pangkal sayap.",
  "metalmark": "Kupu-kupu kecil dengan bintik-bintik mengkilap seperti logam di permukaan sayap.",
  "monarch": "Kupu-kupu ikonik berukuran besar dengan sayap oranye kemerahan dan urat-urat hitam tebal.",
  "morning cloak": "Sayap berwarna cokelat gelap keunguan dengan pinggiran kuning terang dan bintik biru.",
  "orange oakleaf": "Sayap bawah menyerupai daun kering cokelat, namun bagian atas berwarna oranye-biru cerah.",
  "orange tip": "Ujung sayap depan berwarna oranye terang yang sangat kontras dengan warna dasar putih.",
  "orchard swallow": "Kupu-kupu swallowtail besar berwarna hitam dengan bercak merah dan putih.",
  "painted lady": "Memiliki pola kompleks berwarna oranye, hitam, dan putih dengan bintik-bintik halus.",
  "paper kite": "Sayap putih transparan dengan pola garis-garis hitam tipis seperti layang-layang kertas.",
  "peacock": "Memiliki pola lingkaran mata besar berwarna-warni menyerupai ekor burung merak.",
  "pine white": "Kupu-kupu putih bersih dengan urat hitam halus, sering ditemukan di hutan pinus.",
  "pipevine swallow": "Kupu-kupu swallowtail hitam dengan kilauan biru metalik di sayap belakang.",
  "purple hairstreak": "Memiliki kilauan warna ungu kebiruan yang indah di bagian atas sayap cokelatnya.",
  "question mark": "Memiliki tanda perak menyerupai tanda tanya pada bagian bawah sayap.",
  "red admiral": "Memiliki pita merah-oranye melintang di sayap hitam dengan bintik putih di ujungnya.",
  "red spotted purple": "Kupu-kupu biru gelap dengan bintik-bintik oranye-merah di bagian bawah sayap.",
  "scarce swallow": "Kupu-kupu swallowtail berwarna kuning pucat dengan garis-garis hitam vertikal menyerupai zebra.",
  "silver spot skipper": "Memiliki bercak perak mengkilap yang mencolok di bagian bawah sayap belakang.",
  "sixspot burnet": "Ngengat siang hari berwarna hitam dengan enam bercak merah terang pada sayap depan.",
  "skipper": "Kupu-kupu kecil dengan tubuh tegap dan antena melengkung khas.",
  "sootywing": "Memiliki sayap hitam pekat menyerupai jelaga dengan bintik-bintik putih kecil.",
  "southern dogface": "Pola kuning-hitam di sayap depan menyerupai siluet kepala anjing pudel.",
  "straited queen": "Kupu-kupu berwarna cokelat oranye dengan pola garis-garis putih halus di sepanjang urat sayap.",
  "two barred flasher": "Memiliki dua pita hijau mengkilap di sayap cokelat gelap dan terbang sangat cepat.",
  "ulyses": "Kupu-kupu swallowtail besar dengan warna biru elektrik yang sangat menakjubkan.",
  "viceroy": "Sangat menyerupai kupu-kupu Monarch, namun memiliki garis hitam tambahan melintang di sayap belakang.",
  "wood satyr": "Memiliki pola beberapa mata lingkaran kecil berwarna cokelat di sayapnya.",
  "yellow swallow tail": "Kupu-kupu swallowtail berwarna kuning cerah dengan pola garis hitam tebal.",
  "zebra long wing": "Memiliki pola garis hitam dan kuning memanjang menyerupai zebra pada kedua sayap."
}

# Baseline model performances mapping or generating realistic values
# Baseline values from original AnalyticsTab baseline
baselines = {
  "BANDED ORANGE HELICONIAN": {"correct": 82, "total": 85, "avg_confidence": 94.20},
  "BECKERS WHITE": {"correct": 76, "total": 80, "avg_confidence": 91.80},
  "BLACK HAIRSTREAK": {"correct": 68, "total": 75, "avg_confidence": 89.50},
  "CABBAGE WHITE": {"correct": 87, "total": 90, "avg_confidence": 95.10},
  "GREAT EGGFLY": {"correct": 92, "total": 95, "avg_confidence": 96.50},
  "GREY HAIRSTREAK": {"correct": 65, "total": 72, "avg_confidence": 88.70},
  "JULIA": {"correct": 85, "total": 88, "avg_confidence": 94.80},
  "PURPLE HAIRSTREAK": {"correct": 70, "total": 76, "avg_confidence": 90.10},
  "MONARCH": {"correct": 94, "total": 98, "avg_confidence": 97.20},
  "PEACOCK": {"correct": 88, "total": 92, "avg_confidence": 93.40},
  "PIPEVINE SWALLOW": {"correct": 81, "total": 86, "avg_confidence": 91.90},
  "QUESTION MARK": {"correct": 79, "total": 85, "avg_confidence": 90.50},
  "RED SPOTTED PURPLE": {"correct": 83, "total": 89, "avg_confidence": 92.10},
  "VICEROY": {"correct": 86, "total": 91, "avg_confidence": 93.80}
}

sql_lines = []

# Clear existing tables (optional, but good for seeding cleanly)
sql_lines.append("TRUNCATE TABLE public.performa_model CASCADE;")
sql_lines.append("TRUNCATE TABLE public.spesies CASCADE;")

# Seeding Species
print("Generating SQL for Species...")
for idx, m_class in enumerate(model_classes, 1):
    sp_id = f"LPD-{idx:03d}"
    name_upper = m_class.upper()
    scientific = scientific_names.get(m_class, "Lepidoptera")
    desc = descriptions.get(m_class, "Deskripsi spesies belum tersedia.")
    
    # Escape quotes
    desc_esc = desc.replace("'", "''")
    scientific_esc = scientific.replace("'", "''")
    name_upper_esc = name_upper.replace("'", "''")
    
    status = "TERVERIFIKASI"
    # Make a few pending review for realism
    verified = "true"
    if idx % 7 == 0:
        status = "PENDING_REVIEW"
        verified = "false"
        
    sql = f"INSERT INTO public.spesies (id, nama_umum, nama_ilmiah, deskripsi, status_verifikasi, is_verified) VALUES ('{sp_id}', '{name_upper_esc}', '{scientific_esc}', '{desc_esc}', '{status}', {verified});"
    sql_lines.append(sql)

# Seeding Model Performance
print("Generating SQL for Model Performance...")
import random
random.seed(42) # For reproducible random values

for idx, m_class in enumerate(model_classes, 1):
    sp_id = f"LPD-{idx:03d}"
    name_upper = m_class.upper()
    
    # Find matching baseline or generate one
    baseline = None
    for b_name, b_val in baselines.items():
        if b_name == name_upper or b_name in name_upper or name_upper in b_name:
            baseline = b_val
            break
            
    if baseline:
        correct = baseline["correct"]
        total = baseline["total"]
        avg_conf = baseline["avg_confidence"]
    else:
        # Generate realistic values (accuracy between 75% and 98%)
        total = random.randint(70, 95)
        accuracy_pct = random.uniform(0.78, 0.97)
        correct = int(total * accuracy_pct)
        avg_conf = round(accuracy_pct * 100 - random.uniform(1, 4), 2)
        
    sql = f"INSERT INTO public.performa_model (id, spesies_id, jumlah_benar, jumlah_total, avg_confidence) VALUES (gen_random_uuid(), '{sp_id}', {correct}, {total}, {avg_conf});"
    sql_lines.append(sql)

# Altering riwayat_klasifikasi table columns
sql_lines.insert(0, "ALTER TABLE public.riwayat_klasifikasi ALTER COLUMN image_path TYPE text;")
sql_lines.insert(1, "ALTER TABLE public.riwayat_klasifikasi ALTER COLUMN thumbnail_path TYPE text;")

with open("seed.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(sql_lines))

print("seed.sql generated successfully!")
