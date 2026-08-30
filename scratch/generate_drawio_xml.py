import xml.etree.ElementTree as ET
import xml.dom.minidom

# Initialize XML Structure
mxfile = ET.Element("mxfile", host="Electron", modified="2026-06-20T00:36:35Z", agent="Mozilla/5.0", version="21.6.8")
diagram = ET.SubElement(mxfile, "diagram", id="activity-diagram", name="Activity Diagram Klasifikasi Kupu-Kupu")
mxGraphModel = ET.SubElement(diagram, "mxGraphModel", dx="1000", dy="800", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="827", pageHeight="1169", math="0", shadow="0")
root = ET.SubElement(mxGraphModel, "root")

# Base elements
ET.SubElement(root, "mxCell", id="0")
ET.SubElement(root, "mxCell", id="1", parent="0")

# Helper function to create vertex
def create_vertex(id_val, value, style, x, y, w, h):
    cell = ET.SubElement(root, "mxCell", id=id_val, value=value, style=style, vertex="1", parent="1")
    geo = ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h))
    geo.set("as", "geometry")
    return cell

# Helper function to create edge
def create_edge(id_val, value, style, source, target):
    cell = ET.SubElement(root, "mxCell", id=id_val, value=value, style=style, edge="1", parent="1", source=source, target=target)
    geo = ET.SubElement(cell, "mxGeometry", relative="1")
    geo.set("as", "geometry")
    return cell

# 1. Swimlanes (Containers)
# Lane 1: Pengguna
create_vertex("lane_user", "PENGGUNA", "swimlane;html=1;startSize=30;fillColor=#E3F2FD;strokeColor=#1565C0;fontColor=#0D47A1;fontStyle=1;align=center;", 40, 40, 220, 960)
# Lane 2: Sistem
create_vertex("lane_system", "SISTEM", "swimlane;html=1;startSize=30;fillColor=#E8F5E9;strokeColor=#2E7D32;fontColor=#1B5E20;fontStyle=1;align=center;", 260, 40, 260, 960)
# Lane 3: Database
create_vertex("lane_db", "DATABASE (SUPABASE)", "swimlane;html=1;startSize=30;fillColor=#FFE0B2;strokeColor=#E65100;fontColor=#E65100;fontStyle=1;align=center;", 520, 40, 220, 960)

# 2. Nodes in PENGGUNA Lane (x base offset = 40, centered around x = 150)
create_vertex("init", "", "ellipse;html=1;fillColor=#000000;strokeColor=none;shadow=0;", 140, 100, 20, 20)
create_vertex("act_open", "Membuka Halaman<br/>Klasifikasi", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1565C0;strokeWidth=1.5;fontColor=#0D47A1;", 90, 150, 120, 50)
create_vertex("act_upload", "Mengunggah Citra<br/>Kupu-Kupu", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1565C0;strokeWidth=1.5;fontColor=#0D47A1;", 90, 230, 120, 50)
create_vertex("act_view_detail", "Melihat Detail<br/>Spesies", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1565C0;strokeWidth=1.5;fontColor=#0D47A1;", 90, 820, 120, 50)
create_vertex("final", "", "ellipse;html=1;shape=mxgraph.sysml.finalState;fillColor=#000000;strokeColor=#1565C0;strokeWidth=2;shadow=0;", 140, 910, 20, 20)

# 3. Nodes in SISTEM Lane (x base offset = 260, centered around x = 390)
create_vertex("act_validate", "Validasi File Gambar", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 230, 120, 50)
create_vertex("dec_valid", "", "rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;", 370, 310, 40, 40)
create_vertex("act_error", "Menampilkan Pesan<br/>Error", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 380, 120, 50)
create_vertex("act_send_api", "Mengirim Citra ke<br/>FastAPI Backend", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 450, 120, 50)
create_vertex("act_preprocess", "Preprocessing Citra<br/>(Resize &amp; Normalisasi)", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 520, 120, 50)
create_vertex("act_inference", "Inferensi Model<br/>EfficientNet-B0", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 590, 120, 50)
create_vertex("act_generate", "Menghasilkan Prediksi<br/>(Spesies, Confidence,<br/>Kandidat)", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 660, 120, 55)
create_vertex("act_display_result", "Menampilkan Hasil<br/>Klasifikasi", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 820, 120, 50)

# 4. Nodes in DATABASE Lane (x base offset = 520, centered around x = 630)
create_vertex("act_get_details", "Mengambil Detail<br/>Spesies dari DB", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E65100;strokeWidth=1.5;fontColor=#E65100;", 570, 660, 120, 50)
create_vertex("act_save_history", "Menyimpan Riwayat<br/>Klasifikasi", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E65100;strokeWidth=1.5;fontColor=#E65100;", 570, 730, 120, 50)
create_vertex("act_save_candidates", "Menyimpan Kandidat<br/>Prediksi", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E65100;strokeWidth=1.5;fontColor=#E65100;", 570, 800, 120, 50)

# 5. Edges
edge_style = "edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#555555;strokeWidth=1.2;"

create_edge("e1", "", edge_style, "init", "act_open")
create_edge("e2", "", edge_style, "act_open", "act_upload")
create_edge("e3", "", edge_style, "act_upload", "act_validate")
create_edge("e4", "", edge_style, "act_validate", "dec_valid")

# Decision branches
create_edge("e5_invalid", "Tidak Valid", edge_style + "entryX=1;entryY=0.5;", "dec_valid", "act_error")
create_edge("e6_loop", "", edge_style + "exitX=0;exitY=0.5;entryX=1;entryY=0.5;", "act_error", "act_upload")
create_edge("e5_valid", "Valid", edge_style, "dec_valid", "act_send_api")

# Processing pipeline
create_edge("e7", "", edge_style, "act_send_api", "act_preprocess")
create_edge("e8", "", edge_style, "act_preprocess", "act_inference")
create_edge("e9", "", edge_style, "act_inference", "act_generate")

# Database interaction
create_edge("e10", "", edge_style, "act_generate", "act_get_details")
create_edge("e11", "", edge_style, "act_get_details", "act_save_history")
create_edge("e12", "", edge_style, "act_save_history", "act_save_candidates")

# Return values and display
create_edge("e13", "", edge_style + "exitX=0;exitY=0.5;entryX=1;entryY=0.5;", "act_save_candidates", "act_display_result")
create_edge("e14", "", edge_style, "act_display_result", "act_view_detail")
create_edge("e15", "", edge_style, "act_view_detail", "final")

# Generate String
xml_str = ET.tostring(mxfile, encoding="utf-8")
dom = xml.dom.minidom.parseString(xml_str)
pretty_xml = dom.toprettyxml(indent="  ")

# Write to file
output_file = "d:\\klasifikasi_kupukupu\\activity_diagram.drawio"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(pretty_xml)

print(f"Draw.io XML successfully written to {output_file}")
