import xml.etree.ElementTree as ET
import xml.dom.minidom

def make_erd_page(root):
    # Base cells
    ET.SubElement(root, "mxCell", id="erd_0")
    ET.SubElement(root, "mxCell", id="erd_1", parent="erd_0")

    # Style definitions
    entity_style = "rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontStyle=1;"
    attr_style = "ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1;fontColor=#000000;fontSize=10;"
    rel_style = "rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontStyle=1;fontSize=10;align=center;"
    line_style = "endArrow=none;html=1;rounded=0;strokeColor=#000000;strokeWidth=1.2;fontSize=10;"

    # 1. SPESIES Entity and its Attributes
    create_vertex(root, "ent_spesies", "spesies", entity_style, 450, 200, 120, 50)
    
    # Attributes for spesies
    create_vertex(root, "att_sp_id", "<u>id</u>", attr_style, 470, 70, 80, 40)
    create_edge(root, "e_sp_id", "", line_style, "att_sp_id", "ent_spesies")
    
    create_vertex(root, "att_sp_nama_umum", "nama_umum", attr_style, 360, 80, 90, 40)
    create_edge(root, "e_sp_nama_umum", "", line_style, "att_sp_nama_umum", "ent_spesies")
    
    create_vertex(root, "att_sp_nama_ilmiah", "nama_ilmiah", attr_style, 280, 120, 90, 40)
    create_edge(root, "e_sp_nama_ilmiah", "", line_style, "att_sp_nama_ilmiah", "ent_spesies")
    
    create_vertex(root, "att_sp_deskripsi", "deskripsi", attr_style, 280, 190, 80, 40)
    create_edge(root, "e_sp_deskripsi", "", line_style, "att_sp_deskripsi", "ent_spesies")
    
    create_vertex(root, "att_sp_image_url", "image_url", attr_style, 320, 260, 80, 40)
    create_edge(root, "e_sp_image_url", "", line_style, "att_sp_image_url", "ent_spesies")
    
    create_vertex(root, "att_sp_created_at", "created_at", attr_style, 580, 80, 80, 40)
    create_edge(root, "e_sp_created_at", "", line_style, "att_sp_created_at", "ent_spesies")
    
    create_vertex(root, "att_sp_updated_at", "updated_at", attr_style, 620, 130, 80, 40)
    create_edge(root, "e_sp_updated_at", "", line_style, "att_sp_updated_at", "ent_spesies")

    # 2. PERFORMA_MODEL Entity and its Attributes
    create_vertex(root, "ent_performa", "performa_model", entity_style, 850, 200, 120, 50)
    
    # Attributes for performa_model
    create_vertex(root, "att_pf_id", "<u>id</u>", attr_style, 870, 70, 80, 40)
    create_edge(root, "e_pf_id", "", line_style, "att_pf_id", "ent_performa")
    
    create_vertex(root, "att_pf_spesies_id", "spesies_id (FK)", attr_style, 980, 80, 95, 40)
    create_edge(root, "e_pf_spesies_id", "", line_style, "att_pf_spesies_id", "ent_performa")
    
    create_vertex(root, "att_pf_total_sampel", "total_sampel", attr_style, 1000, 140, 90, 40)
    create_edge(root, "e_pf_total_sampel", "", line_style, "att_pf_total_sampel", "ent_performa")
    
    create_vertex(root, "att_pf_prediksi_benar", "prediksi_benar", attr_style, 980, 200, 95, 40)
    create_edge(root, "e_pf_prediksi_benar", "", line_style, "att_pf_prediksi_benar", "ent_performa")
    
    create_vertex(root, "att_pf_akurasi", "akurasi", attr_style, 940, 260, 80, 40)
    create_edge(root, "e_pf_akurasi", "", line_style, "att_pf_akurasi", "ent_performa")
    
    create_vertex(root, "att_pf_rata_confidence", "rata_confidence", attr_style, 830, 270, 95, 40)
    create_edge(root, "e_pf_rata_confidence", "", line_style, "att_pf_rata_confidence", "ent_performa")

    # 3. RIWAYAT_KLASIFIKASI Entity and its Attributes
    create_vertex(root, "ent_riwayat", "riwayat_klasifikasi", entity_style, 100, 550, 130, 50)
    
    # Attributes for riwayat_klasifikasi
    create_vertex(root, "att_rw_id", "<u>id</u>", attr_style, 20, 470, 80, 40)
    create_edge(root, "e_rw_id", "", line_style, "att_rw_id", "ent_riwayat")
    
    create_vertex(root, "att_rw_image_path", "image_path", attr_style, 120, 460, 85, 40)
    create_edge(root, "e_rw_image_path", "", line_style, "att_rw_image_path", "ent_riwayat")
    
    create_vertex(root, "att_rw_thumbnail_path", "thumbnail_path", attr_style, 220, 480, 100, 40)
    create_edge(root, "e_rw_thumbnail_path", "", line_style, "att_rw_thumbnail_path", "ent_riwayat")
    
    create_vertex(root, "att_rw_spesies_id", "spesies_terdeteksi_id<br/>(FK)", attr_style, 10, 530, 130, 40)
    create_edge(root, "e_rw_spesies_id", "", line_style, "att_rw_spesies_id", "ent_riwayat")
    
    create_vertex(root, "att_rw_confidence", "confidence", attr_style, 10, 590, 80, 40)
    create_edge(root, "e_rw_confidence", "", line_style, "att_rw_confidence", "ent_riwayat")
    
    create_vertex(root, "att_rw_created_at", "created_at", attr_style, 60, 650, 80, 40)
    create_edge(root, "e_rw_created_at", "", line_style, "att_rw_created_at", "ent_riwayat")

    # 4. KANDIDAT_KLASIFIKASI Entity and its Attributes
    create_vertex(root, "ent_kandidat", "kandidat_klasifikasi", entity_style, 650, 700, 130, 50)
    
    # Attributes for kandidat_klasifikasi
    create_vertex(root, "att_kd_id", "<u>id</u>", attr_style, 670, 800, 80, 40)
    create_edge(root, "e_kd_id", "", line_style, "att_kd_id", "ent_kandidat")
    
    create_vertex(root, "att_kd_riwayat_id", "riwayat_id (FK)", attr_style, 560, 800, 95, 40)
    create_edge(root, "e_kd_riwayat_id", "", line_style, "att_kd_riwayat_id", "ent_kandidat")
    
    create_vertex(root, "att_kd_spesies_id", "spesies_id (FK)", attr_style, 770, 800, 95, 40)
    create_edge(root, "e_kd_spesies_id", "", line_style, "att_kd_spesies_id", "ent_kandidat")
    
    create_vertex(root, "att_kd_confidence", "confidence", attr_style, 800, 740, 80, 40)
    create_edge(root, "e_kd_confidence", "", line_style, "att_kd_confidence", "ent_kandidat")
    
    create_vertex(root, "att_kd_ranking", "ranking", attr_style, 800, 670, 80, 40)
    create_edge(root, "e_kd_ranking", "", line_style, "att_kd_ranking", "ent_kandidat")

    # 5. Relationships & Cardinality Labels
    # spesies (1) : (1) performa_model
    create_vertex(root, "rel_sp_performa", "Memiliki", rel_style, 670, 200, 100, 50)
    create_edge(root, "e_sp_rel_pf", "1", line_style, "ent_spesies", "rel_sp_performa")
    create_edge(root, "e_pf_rel_pf", "1", line_style, "ent_performa", "rel_sp_performa")

    # spesies (1) : (N) riwayat_klasifikasi
    create_vertex(root, "rel_sp_riwayat", "Mendefinisikan", rel_style, 275, 375, 120, 50)
    create_edge(root, "e_sp_rel_rw", "1", line_style, "ent_spesies", "rel_sp_riwayat")
    create_edge(root, "e_rw_rel_rw", "N", line_style, "ent_riwayat", "rel_sp_riwayat")

    # riwayat_klasifikasi (1) : (N) kandidat_klasifikasi
    create_vertex(root, "rel_riwayat_kandidat", "Menghasilkan", rel_style, 375, 625, 120, 50)
    create_edge(root, "e_rw_rel_kd", "1", line_style, "ent_riwayat", "rel_riwayat_kandidat")
    create_edge(root, "e_kd_rel_rw", "N", line_style, "ent_kandidat", "rel_riwayat_kandidat")

    # spesies (1) : (N) kandidat_klasifikasi
    create_vertex(root, "rel_sp_kandidat", "Sebagai Alternatif", rel_style, 540, 450, 120, 50)
    create_edge(root, "e_sp_rel_kd", "1", line_style, "ent_spesies", "rel_sp_kandidat")
    create_edge(root, "e_kd_rel_sp", "N", line_style, "ent_kandidat", "rel_sp_kandidat")


def make_activity_classification_page(root):
    # Base cells
    ET.SubElement(root, "mxCell", id="act_class_0")
    ET.SubElement(root, "mxCell", id="act_class_1", parent="act_class_0")

    # Swimlanes (extended height to 1460)
    create_vertex_child(root, "cl_lane_user", "Pengguna", "swimlane;html=1;startSize=30;fillColor=#E3F2FD;strokeColor=#1565C0;fontColor=#0D47A1;fontStyle=1;align=center;", 40, 40, 220, 1460, "act_class_1")
    create_vertex_child(root, "cl_lane_system", "Sistem", "swimlane;html=1;startSize=30;fillColor=#E8F5E9;strokeColor=#2E7D32;fontColor=#1B5E20;fontStyle=1;align=center;", 260, 40, 260, 1460, "act_class_1")
    create_vertex_child(root, "cl_lane_db", "Database", "swimlane;html=1;startSize=30;fillColor=#FFE0B2;strokeColor=#E65100;fontColor=#E65100;fontStyle=1;align=center;", 520, 40, 220, 1460, "act_class_1")

    # Pengguna Lane Nodes
    create_vertex_child(root, "cl_init", "", "ellipse;html=1;fillColor=#000000;strokeColor=none;shadow=0;", 140, 100, 20, 20, "act_class_1")
    create_vertex_child(root, "cl_act_open", "Membuka Menu<br/>Classification", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1565C0;strokeWidth=1.5;fontColor=#0D47A1;", 90, 150, 120, 50, "act_class_1")
    create_vertex_child(root, "cl_act_upload", "Upload Gambar<br/>Kupu-Kupu", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1565C0;strokeWidth=1.5;fontColor=#0D47A1;", 90, 230, 120, 50, "act_class_1")
    
    # Success path views
    create_vertex_child(root, "cl_act_view_success", "Melihat Hasil<br/>Klasifikasi", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1565C0;strokeWidth=1.5;fontColor=#0D47A1;", 90, 1215, 120, 50, "act_class_1")
    
    # Fail path views
    create_vertex_child(root, "cl_act_view_fail", "Melihat Pesan<br/>Gagal Dideteksi", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1565C0;strokeWidth=1.5;fontColor=#0D47A1;", 90, 1300, 120, 50, "act_class_1")
    
    create_vertex_child(root, "cl_final", "", "ellipse;html=1;shape=mxgraph.sysml.finalState;fillColor=#000000;strokeColor=#1565C0;strokeWidth=2;shadow=0;", 140, 1390, 20, 20, "act_class_1")

    # Sistem Lane Nodes
    create_vertex_child(root, "cl_act_validate", "Validasi File Gambar", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 230, 120, 50, "act_class_1")
    create_vertex_child(root, "cl_dec_valid", "", "rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;", 370, 310, 40, 40, "act_class_1")
    create_vertex_child(root, "cl_act_error", "Menampilkan Pesan<br/>Error", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 380, 120, 50, "act_class_1")
    create_vertex_child(root, "cl_act_send_api", "Kirim Gambar ke<br/>FastAPI Backend", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 460, 120, 50, "act_class_1")
    create_vertex_child(root, "cl_act_preprocess", "Preprocessing Citra<br/>(Resize &amp; Normalisasi)", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 540, 120, 50, "act_class_1")
    create_vertex_child(root, "cl_act_inference", "Inferensi Model<br/>EfficientNet-B0", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 620, 120, 50, "act_class_1")
    create_vertex_child(root, "cl_act_generate", "Menghasilkan Prediksi<br/>(Spesies &amp; Confidence Score)", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 700, 120, 50, "act_class_1")
    
    # Threshold Decision Node with custom label
    create_vertex_child(root, "cl_dec_threshold", "Apakah Confidence<br/>Score &ge; 65%?", "rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontSize=10;align=center;", 340, 780, 100, 60, "act_class_1")
    
    # Success path nodes in Sistem
    create_vertex_child(root, "cl_act_req_details", "Sistem mengambil detail<br/>spesies dari database", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 880, 120, 50, "act_class_1")
    create_vertex_child(root, "cl_act_save_history", "Sistem menyimpan hasil<br/>ke tabel riwayat_klasifikasi", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 960, 120, 50, "act_class_1")
    create_vertex_child(root, "cl_act_save_candidates", "Sistem menyimpan kandidat<br/>prediksi ke tabel kandidat_klasifikasi", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 1040, 120, 50, "act_class_1")
    create_vertex_child(root, "cl_act_get_latest_history", "Sistem mengambil data<br/>riwayat klasifikasi terbaru", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 1120, 120, 50, "act_class_1")
    create_vertex_child(root, "cl_act_display_success", "Sistem menampilkan:<br/>• Nama spesies<br/>• Nama ilmiah<br/>• Confidence Score<br/>• Prediction History", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;align=left;spacingLeft=10;", 325, 1200, 130, 80, "act_class_1")
    
    # Fail path node in Sistem
    create_vertex_child(root, "cl_act_display_fail", "Sistem menampilkan pesan:<br/>\"Gagal Dideteksi\"", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 1300, 120, 50, "act_class_1")

    # Database Lane Nodes
    create_vertex_child(root, "cl_act_db_send_details", "Database mengirim<br/>detail spesies", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E65100;strokeWidth=1.5;fontColor=#E65100;", 570, 880, 120, 50, "act_class_1")
    create_vertex_child(root, "cl_act_db_save_history", "Database menyimpan<br/>data riwayat", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E65100;strokeWidth=1.5;fontColor=#E65100;", 570, 960, 120, 50, "act_class_1")
    create_vertex_child(root, "cl_act_db_save_candidates", "Database menyimpan<br/>kandidat prediksi", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E65100;strokeWidth=1.5;fontColor=#E65100;", 570, 1040, 120, 50, "act_class_1")
    create_vertex_child(root, "cl_act_db_send_history", "Database mengirim<br/>data riwayat", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E65100;strokeWidth=1.5;fontColor=#E65100;", 570, 1120, 120, 50, "act_class_1")

    # Edges
    edge_style = "edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#555555;strokeWidth=1.2;"

    create_edge_child(root, "cl_e1", "", edge_style, "cl_init", "cl_act_open", "act_class_1")
    create_edge_child(root, "cl_e2", "", edge_style, "cl_act_open", "cl_act_upload", "act_class_1")
    create_edge_child(root, "cl_e3", "", edge_style, "cl_act_upload", "cl_act_validate", "act_class_1")
    create_edge_child(root, "cl_e4", "", edge_style, "cl_act_validate", "cl_dec_valid", "act_class_1")

    # Decision branches for image validity
    create_edge_child(root, "cl_e5_invalid", "Tidak Valid", edge_style + "entryX=1;entryY=0.5;", "cl_dec_valid", "cl_act_error", "act_class_1")
    create_edge_child(root, "cl_e6_loop", "", edge_style + "exitX=0;exitY=0.5;entryX=1;entryY=0.5;", "cl_act_error", "cl_act_upload", "act_class_1")
    create_edge_child(root, "cl_e5_valid", "Valid", edge_style, "cl_dec_valid", "cl_act_send_api", "act_class_1")

    # Backend API pipeline
    create_edge_child(root, "cl_e7", "", edge_style, "cl_act_send_api", "cl_act_preprocess", "act_class_1")
    create_edge_child(root, "cl_e8", "", edge_style, "cl_act_preprocess", "cl_act_inference", "act_class_1")
    create_edge_child(root, "cl_e9", "", edge_style, "cl_act_inference", "cl_act_generate", "act_class_1")
    create_edge_child(root, "cl_e10", "", edge_style, "cl_act_generate", "cl_dec_threshold", "act_class_1")

    # Decision branches for threshold
    create_edge_child(root, "cl_e11_ya", "YA", edge_style, "cl_dec_threshold", "cl_act_req_details", "act_class_1")
    create_edge_child(root, "cl_e12", "", edge_style, "cl_act_req_details", "cl_act_db_send_details", "act_class_1")
    create_edge_child(root, "cl_e13", "", edge_style + "exitX=0.5;exitY=1;entryX=1;entryY=0.5;", "cl_act_db_send_details", "cl_act_save_history", "act_class_1")
    create_edge_child(root, "cl_e14", "", edge_style, "cl_act_save_history", "cl_act_db_save_history", "act_class_1")
    create_edge_child(root, "cl_e15", "", edge_style + "exitX=0.5;exitY=1;entryX=1;entryY=0.5;", "cl_act_db_save_history", "cl_act_save_candidates", "act_class_1")
    create_edge_child(root, "cl_e16", "", edge_style, "cl_act_save_candidates", "cl_act_db_save_candidates", "act_class_1")
    create_edge_child(root, "cl_e17", "", edge_style + "exitX=0.5;exitY=1;entryX=1;entryY=0.5;", "cl_act_db_save_candidates", "cl_act_get_latest_history", "act_class_1")
    create_edge_child(root, "cl_e18", "", edge_style, "cl_act_get_latest_history", "cl_act_db_send_history", "act_class_1")
    create_edge_child(root, "cl_e19", "", edge_style + "exitX=0.5;exitY=1;entryX=1;entryY=0.5;", "cl_act_db_send_history", "cl_act_display_success", "act_class_1")
    create_edge_child(root, "cl_e20", "", edge_style, "cl_act_display_success", "cl_act_view_success", "act_class_1")
    create_edge_child(root, "cl_e21", "", edge_style, "cl_act_view_success", "cl_final", "act_class_1")

    # Fail path
    create_edge_child(root, "cl_e11_tidak", "TIDAK", edge_style, "cl_dec_threshold", "cl_act_display_fail", "act_class_1")
    create_edge_child(root, "cl_e22", "", edge_style, "cl_act_display_fail", "cl_act_view_fail", "act_class_1")
    create_edge_child(root, "cl_e23", "", edge_style, "cl_act_view_fail", "cl_final", "act_class_1")


def make_activity_dataset_page(root):
    # Base cells
    ET.SubElement(root, "mxCell", id="act_data_0")
    ET.SubElement(root, "mxCell", id="act_data_1", parent="act_data_0")

    # Swimlanes
    create_vertex_child(root, "dt_lane_user", "PENGGUNA", "swimlane;html=1;startSize=30;fillColor=#E3F2FD;strokeColor=#1565C0;fontColor=#0D47A1;fontStyle=1;align=center;", 40, 40, 220, 680, "act_data_1")
    create_vertex_child(root, "dt_lane_system", "SISTEM", "swimlane;html=1;startSize=30;fillColor=#E8F5E9;strokeColor=#2E7D32;fontColor=#1B5E20;fontStyle=1;align=center;", 260, 40, 260, 680, "act_data_1")
    create_vertex_child(root, "dt_lane_db", "DATABASE (SUPABASE)", "swimlane;html=1;startSize=30;fillColor=#FFE0B2;strokeColor=#E65100;fontColor=#E65100;fontStyle=1;align=center;", 520, 40, 220, 680, "act_data_1")

    # Pengguna Lane Nodes
    create_vertex_child(root, "dt_init", "", "ellipse;html=1;fillColor=#000000;strokeColor=none;shadow=0;", 140, 100, 20, 20, "act_data_1")
    create_vertex_child(root, "dt_act_open", "Membuka Menu<br/>Dataset", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1565C0;strokeWidth=1.5;fontColor=#0D47A1;", 90, 150, 120, 50, "act_data_1")
    create_vertex_child(root, "dt_act_select", "Memilih Spesies<br/>Kupu-Kupu", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1565C0;strokeWidth=1.5;fontColor=#0D47A1;", 90, 390, 120, 50, "act_data_1")
    create_vertex_child(root, "dt_final", "", "ellipse;html=1;shape=mxgraph.sysml.finalState;fillColor=#000000;strokeColor=#1565C0;strokeWidth=2;shadow=0;", 140, 630, 20, 20, "act_data_1")

    # Sistem Lane Nodes
    create_vertex_child(root, "dt_act_get_species", "Mengambil Data<br/>Daftar Spesies", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 150, 120, 50, "act_data_1")
    create_vertex_child(root, "dt_act_display_list", "Menampilkan Daftar<br/>Spesies Kupu-Kupu", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 310, 120, 50, "act_data_1")
    create_vertex_child(root, "dt_act_get_detail", "Mengambil Detail<br/>Spesies Terpilih", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;", 330, 390, 120, 50, "act_data_1")
    create_vertex_child(root, "dt_act_display_detail", "Menampilkan Detail:<br/>• Nama Spesies<br/>• Nama Ilmiah<br/>• Deskripsi<br/>• Gambar Referensi", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#2E7D32;strokeWidth=1.5;fontColor=#1B5E20;align=left;spacingLeft=10;", 330, 540, 130, 70, "act_data_1")

    # Database Lane Nodes
    create_vertex_child(root, "dt_act_query_list", "Mengirim Data<br/>Daftar Spesies", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E65100;strokeWidth=1.5;fontColor=#E65100;", 570, 150, 120, 50, "act_data_1")
    create_vertex_child(root, "dt_act_query_detail", "Mengirim Data Detail<br/>(Deskripsi &amp; Gambar)", "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#E65100;strokeWidth=1.5;fontColor=#E65100;", 570, 390, 120, 50, "act_data_1")

    # Edges
    edge_style = "edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#555555;strokeWidth=1.2;"

    create_edge_child(root, "dt_e1", "", edge_style, "dt_init", "dt_act_open", "act_data_1")
    create_edge_child(root, "dt_e2", "", edge_style, "dt_act_open", "dt_act_get_species", "act_data_1")
    create_edge_child(root, "dt_e3", "", edge_style, "dt_act_get_species", "dt_act_query_list", "act_data_1")
    
    # Send back list to display
    create_edge_child(root, "dt_e4", "", edge_style + "exitX=0.5;exitY=1;entryX=0.5;entryY=0;", "dt_act_query_list", "dt_act_display_list", "act_data_1")
    create_edge_child(root, "dt_e5", "", edge_style, "dt_act_display_list", "dt_act_select", "act_data_1")
    
    # Detail request
    create_edge_child(root, "dt_e6", "", edge_style, "dt_act_select", "dt_act_get_detail", "act_data_1")
    create_edge_child(root, "dt_e7", "", edge_style, "dt_act_get_detail", "dt_act_query_detail", "act_data_1")
    
    # Display detail and finish
    create_edge_child(root, "dt_e8", "", edge_style + "exitX=0.5;exitY=1;entryX=0.5;entryY=0;", "dt_act_query_detail", "dt_act_display_detail", "act_data_1")
    create_edge_child(root, "dt_e9", "", edge_style, "dt_act_display_detail", "dt_final", "act_data_1")


# Helper function to create vertex (parent = 1)
def create_vertex(parent, id_val, value, style, x, y, w, h):
    cell = ET.SubElement(parent, "mxCell", id=id_val, value=value, style=style, vertex="1", parent="erd_1")
    geo = ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h))
    geo.set("as", "geometry")
    return cell

# Helper function to create edge (parent = 1)
def create_edge(parent, id_val, value, style, source, target):
    cell = ET.SubElement(parent, "mxCell", id=id_val, value=value, style=style, edge="1", parent="erd_1", source=source, target=target)
    geo = ET.SubElement(cell, "mxGeometry", relative="1")
    geo.set("as", "geometry")
    return cell

# Helper function to create vertex with specific parent (relative grouping)
def create_vertex_child(parent, id_val, value, style, x, y, w, h, parent_id):
    cell = ET.SubElement(parent, "mxCell", id=id_val, value=value, style=style, vertex="1", parent=parent_id)
    geo = ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h))
    geo.set("as", "geometry")
    return cell

# Helper function to create edge with specific parent (relative grouping)
def create_edge_child(parent, id_val, value, style, source, target, parent_id):
    cell = ET.SubElement(parent, "mxCell", id=id_val, value=value, style=style, edge="1", parent=parent_id, source=source, target=target)
    geo = ET.SubElement(cell, "mxGeometry", relative="1")
    geo.set("as", "geometry")
    return cell


# Assemble multi-page mxfile
mxfile = ET.Element("mxfile", host="Electron", modified="2026-06-20T00:48:51Z", agent="Mozilla/5.0", version="21.6.8")

# Page 1: ERD
diagram_erd = ET.SubElement(mxfile, "diagram", id="page_erd", name="1. Entity Relationship Diagram (ERD)")
model_erd = ET.SubElement(diagram_erd, "mxGraphModel", dx="1000", dy="800", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="827", pageHeight="1169", math="0", shadow="0")
root_erd = ET.SubElement(model_erd, "root")
make_erd_page(root_erd)

# Page 2: Activity Diagram Klasifikasi
diagram_act_class = ET.SubElement(mxfile, "diagram", id="page_act_class", name="2. Activity Diagram Klasifikasi")
model_act_class = ET.SubElement(diagram_act_class, "mxGraphModel", dx="1000", dy="800", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="827", pageHeight="1169", math="0", shadow="0")
root_act_class = ET.SubElement(model_act_class, "root")
make_activity_classification_page(root_act_class)

# Page 3: Activity Diagram Dataset
diagram_act_data = ET.SubElement(mxfile, "diagram", id="page_act_data", name="3. Activity Diagram Dataset Referensi")
model_act_data = ET.SubElement(diagram_act_data, "mxGraphModel", dx="1000", dy="800", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="827", pageHeight="1169", math="0", shadow="0")
root_act_data = ET.SubElement(model_act_data, "root")
make_activity_dataset_page(root_act_data)

# Generate String
xml_str = ET.tostring(mxfile, encoding="utf-8")
dom = xml.dom.minidom.parseString(xml_str)
pretty_xml = dom.toprettyxml(indent="  ")

# Write to file
output_file = "d:\\klasifikasi_kupukupu\\butterfly_classification_diagrams.drawio"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(pretty_xml)

print(f"Generated multi-page Draw.io diagram at {output_file}")
