import xml.etree.ElementTree as ET
import xml.dom.minidom

def create_vertex_child(parent, id_val, value, style, x, y, w, h, parent_id):
    cell = ET.SubElement(parent, "mxCell", id=id_val, value=value, style=style, vertex="1", parent=parent_id)
    geo = ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h))
    geo.set("as", "geometry")
    return cell

def create_edge_child(parent, id_val, value, style, source, target, parent_id):
    cell = ET.SubElement(parent, "mxCell", id=id_val, value=value, style=style, edge="1", parent=parent_id, source=source, target=target)
    geo = ET.SubElement(cell, "mxGeometry", relative="1")
    geo.set("as", "geometry")
    return cell

def make_single_diagram():
    # Assemble mxfile
    mxfile = ET.Element("mxfile", host="Electron", modified="2026-06-20T02:12:16Z", agent="Mozilla/5.0", version="21.6.8")
    diagram = ET.SubElement(mxfile, "diagram", id="page_klasifikasi", name="Activity Diagram Klasifikasi")
    model = ET.SubElement(diagram, "mxGraphModel", dx="1000", dy="800", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="827", pageHeight="1169", math="0", shadow="0")
    root = ET.SubElement(model, "root")

    ET.SubElement(root, "mxCell", id="0")
    ET.SubElement(root, "mxCell", id="1", parent="0")

    # Swimlanes (extended height to 1460)
    create_vertex_child(root, "cl_lane_user", "Pengguna", "swimlane;html=1;startSize=30;fillColor=#E3F2FD;strokeColor=#1565C0;fontColor=#0D47A1;fontStyle=1;align=center;", 40, 40, 220, 1460, "1")
    create_vertex_child(root, "cl_lane_system", "Sistem", "swimlane;html=1;startSize=30;fillColor=#E8F5E9;strokeColor=#2E7D32;fontColor=#1B5E20;fontStyle=1;align=center;", 260, 40, 260, 1460, "1")
    create_vertex_child(root, "cl_lane_db", "Database", "swimlane;html=1;startSize=30;fillColor=#FFE0B2;strokeColor=#E65100;fontColor=#E65100;fontStyle=1;align=center;", 520, 40, 220, 1460, "1")

    # Pengguna Lane Nodes
    create_vertex_child(root, "cl_init", "", "ellipse;html=1;fillColor=#000000;strokeColor=none;shadow=0;", 140, 100, 20, 20, "1")
    create_vertex_child(root, "cl_act_open", "Membuka Menu<br/>Classification", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1565C0;strokeWidth=1.5;fontColor=#0D47A1;", 90, 150, 120, 50, "1")
    create_vertex_child(root, "cl_act_upload", "Upload Gambar<br/>Kupu-Kupu", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1565C0;strokeWidth=1.5;fontColor=#0D47A1;", 90, 230, 120, 50, "1")
    
    # Success path views
    create_vertex_child(root, "cl_act_view_success", "Melihat Hasil<br/>Klasifikasi", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1565C0;strokeWidth=1.5;fontColor=#0D47A1;", 90, 1215, 120, 50, "1")
    
    # Fail path views
    create_vertex_child(root, "cl_act_view_fail", "Melihat Pesan<br/>Gagal Dideteksi", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1565C0;strokeWidth=1.5;fontColor=#0D47A1;", 90, 1300, 120, 50, "1")
    
    create_vertex_child(root, "cl_final", "", "ellipse;html=1;shape=mxgraph.sysml.finalState;fillColor=#000000;strokeColor=#1565C0;strokeWidth=2;shadow=0;", 140, 1390, 20, 20, "1")

    # Sistem Lane Nodes
    create_vertex_child(root, "cl_act_validate", "Validasi File Gambar", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 230, 120, 50, "1")
    create_vertex_child(root, "cl_dec_valid", "", "rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;", 370, 310, 40, 40, "1")
    create_vertex_child(root, "cl_act_error", "Menampilkan Pesan<br/>Error", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 380, 120, 50, "1")
    create_vertex_child(root, "cl_act_send_api", "Kirim Gambar ke<br/>FastAPI Backend", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 460, 120, 50, "1")
    create_vertex_child(root, "cl_act_preprocess", "Preprocessing Citra<br/>(Resize &amp; Normalisasi)", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 540, 120, 50, "1")
    create_vertex_child(root, "cl_act_inference", "Inferensi Model<br/>EfficientNet-B0", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 620, 120, 50, "1")
    create_vertex_child(root, "cl_act_generate", "Menghasilkan Prediksi<br/>(Spesies &amp; Confidence Score)", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 700, 120, 50, "1")
    
    # Threshold Decision Node with custom label
    create_vertex_child(root, "cl_dec_threshold", "Apakah Confidence<br/>Score &ge; 65%?", "rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontSize=10;align=center;", 340, 780, 100, 60, "1")
    
    # Success path nodes in Sistem
    create_vertex_child(root, "cl_act_req_details", "Sistem mengambil detail<br/>spesies dari database", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 880, 120, 50, "1")
    create_vertex_child(root, "cl_act_save_history", "Sistem menyimpan hasil<br/>ke tabel riwayat_klasifikasi", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 960, 120, 50, "1")
    create_vertex_child(root, "cl_act_save_candidates", "Sistem menyimpan kandidat<br/>prediksi ke tabel kandidat_klasifikasi", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 1040, 120, 50, "1")
    create_vertex_child(root, "cl_act_get_latest_history", "Sistem mengambil data<br/>riwayat klasifikasi terbaru", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 1120, 120, 50, "1")
    create_vertex_child(root, "cl_act_display_success", "Sistem menampilkan:<br/>• Nama spesies<br/>• Nama ilmiah<br/>• Confidence Score<br/>• Prediction History", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;align=left;spacingLeft=10;", 325, 1200, 130, 80, "1")
    
    # Fail path node in Sistem
    create_vertex_child(root, "cl_act_display_fail", "Sistem menampilkan pesan:<br/>\"Gagal Dideteksi\"", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 1300, 120, 50, "1")

    # Database Lane Nodes
    create_vertex_child(root, "cl_act_db_send_details", "Database mengirim<br/>detail spesies", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E65100;strokeWidth=1.5;fontColor=#E65100;", 570, 880, 120, 50, "1")
    create_vertex_child(root, "cl_act_db_save_history", "Database menyimpan<br/>data riwayat", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E65100;strokeWidth=1.5;fontColor=#E65100;", 570, 960, 120, 50, "1")
    create_vertex_child(root, "cl_act_db_save_candidates", "Database menyimpan<br/>kandidat prediksi", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E65100;strokeWidth=1.5;fontColor=#E65100;", 570, 1040, 120, 50, "1")
    create_vertex_child(root, "cl_act_db_send_history", "Database mengirim<br/>data riwayat", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E65100;strokeWidth=1.5;fontColor=#E65100;", 570, 1120, 120, 50, "1")

    # Edges
    edge_style = "edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#555555;strokeWidth=1.2;"

    create_edge_child(root, "cl_e1", "", edge_style, "cl_init", "cl_act_open", "1")
    create_edge_child(root, "cl_e2", "", edge_style, "cl_act_open", "cl_act_upload", "1")
    create_edge_child(root, "cl_e3", "", edge_style, "cl_act_upload", "cl_act_validate", "1")
    create_edge_child(root, "cl_e4", "", edge_style, "cl_act_validate", "cl_dec_valid", "1")

    # Decision branches for image validity
    create_edge_child(root, "cl_e5_invalid", "Tidak Valid", edge_style + "entryX=1;entryY=0.5;", "cl_dec_valid", "cl_act_error", "1")
    create_edge_child(root, "cl_e6_loop", "", edge_style + "exitX=0;exitY=0.5;entryX=1;entryY=0.5;", "cl_act_error", "cl_act_upload", "1")
    create_edge_child(root, "cl_e5_valid", "Valid", edge_style, "cl_dec_valid", "cl_act_send_api", "1")

    # Backend API pipeline
    create_edge_child(root, "cl_e7", "", edge_style, "cl_act_send_api", "cl_act_preprocess", "1")
    create_edge_child(root, "cl_e8", "", edge_style, "cl_act_preprocess", "cl_act_inference", "1")
    create_edge_child(root, "cl_e9", "", edge_style, "cl_act_inference", "cl_act_generate", "1")
    create_edge_child(root, "cl_e10", "", edge_style, "cl_act_generate", "cl_dec_threshold", "1")

    # Decision branches for threshold
    create_edge_child(root, "cl_e11_ya", "YA", edge_style, "cl_dec_threshold", "cl_act_req_details", "1")
    create_edge_child(root, "cl_e12", "", edge_style, "cl_act_req_details", "cl_act_db_send_details", "1")
    create_edge_child(root, "cl_e13", "", edge_style + "exitX=0.5;exitY=1;entryX=1;entryY=0.5;", "cl_act_db_send_details", "cl_act_save_history", "1")
    create_edge_child(root, "cl_e14", "", edge_style, "cl_act_save_history", "cl_act_db_save_history", "1")
    create_edge_child(root, "cl_e15", "", edge_style + "exitX=0.5;exitY=1;entryX=1;entryY=0.5;", "cl_act_db_save_history", "cl_act_save_candidates", "1")
    create_edge_child(root, "cl_e16", "", edge_style, "cl_act_save_candidates", "cl_act_db_save_candidates", "1")
    create_edge_child(root, "cl_e17", "", edge_style + "exitX=0.5;exitY=1;entryX=1;entryY=0.5;", "cl_act_db_save_candidates", "cl_act_get_latest_history", "1")
    create_edge_child(root, "cl_e18", "", edge_style, "cl_act_get_latest_history", "cl_act_db_send_history", "1")
    create_edge_child(root, "cl_e19", "", edge_style + "exitX=0.5;exitY=1;entryX=1;entryY=0.5;", "cl_act_db_send_history", "cl_act_display_success", "1")
    create_edge_child(root, "cl_e20", "", edge_style, "cl_act_display_success", "cl_act_view_success", "1")
    create_edge_child(root, "cl_e21", "", edge_style, "cl_act_view_success", "cl_final", "1")

    # Fail path
    create_edge_child(root, "cl_e11_tidak", "TIDAK", edge_style, "cl_dec_threshold", "cl_act_display_fail", "1")
    create_edge_child(root, "cl_e22", "", edge_style, "cl_act_display_fail", "cl_act_view_fail", "1")
    create_edge_child(root, "cl_e23", "", edge_style, "cl_act_view_fail", "cl_final", "1")

    # Generate String
    xml_str = ET.tostring(mxfile, encoding="utf-8")
    dom = xml.dom.minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent="  ")

    # Write to file
    output_path = "d:\\klasifikasi_kupukupu\\activity_diagram.drawio"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(pretty_xml)

    print(f"Generated single page Activity Diagram at {output_path}")

if __name__ == "__main__":
    make_single_diagram()
