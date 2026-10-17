import streamlit as st

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="Digital E-CV | Tim JBAW Corps",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. DATA KELOMPOK & DETAIL CV 5 PERSONEL
# ==========================================
TEAM_INFO = {
    "nama_tim": "JBAW Corps",
    "tagline": "Digital Creative & Software Development Squad",
    "kampus": "Universitas Bina Sarana Informatika",
}

MEMBERS_CV = {
    "Muhammad Ari Shidqi": {
        "peran": "Ketua Umum",
        "foto": "https://api.dicebear.com/7.x/avataaars/svg?seed=AriShidqi",
        "email": "ari.shidqi@email.com",
        "lokasi": "Indonesia",
        "ringkasan": (
            "Mahasiswa Sistem Informasi dan pengembang web yang berfokus pada pembangunan aplikasi "
            "berbasis backend menggunakan PHP (Laravel), pengelolaan database MySQL, serta perancangan "
            "arsitektur sistem terstruktur menggunakan UML, ERD, dan LRD."
        ),
        "hard_skills": ["PHP 8.2 & Laravel", "MySQL / SQL", "Python & Streamlit", "Node.js", "UML & ERD Modeling"],
        "soft_skills": ["Project Leadership", "Problem Solving", "System Analysis"],
        "pengalaman": [
            {
                "posisi": "Ketua Umum & Lead Backend Developer",
                "institusi": "JBAW Corps",
                "tahun": "2025 - 2026",
                "deskripsi": "Memimpin arah pengembangan proyek tim, membangun sistem backend, serta integrasi teknologi web."
            }
        ],
        "pendidikan": "S1 Sistem Informasi - Universitas Bina Sarana Informatika",
        "sertifikasi": ["Digital Transformation Course (2026)", "Backend Development Training"]
    },
    "Dwi Saputra": {
        "peran": "Wakil Ketua Umum",
        "foto": "https://api.dicebear.com/7.x/avataaars/svg?seed=DwiSaputra",
        "email": "dwi.saputra@email.com",
        "lokasi": "Indonesia",
        "ringkasan": (
            "Mendampingi Ketua Umum dalam mengawasi operasional proyek, manajemen koordinasi tim, "
            "serta memastikan kelancaran eksekusi setiap tahapan pengembangan sistem."
        ),
        "hard_skills": ["Project Management", "System Coordination", "HTML/CSS Basic", "Git Collaboration"],
        "soft_skills": ["Strategic Planning", "Team Leadership", "Conflict Resolution"],
        "pengalaman": [
            {
                "posisi": "Wakil Ketua Umum",
                "institusi": "JBAW Corps",
                "tahun": "2025 - 2026",
                "deskripsi": "Mengkoordinasikan divisi teknis dan non-teknis serta membantu manajemen tugas harian tim."
            }
        ],
        "pendidikan": "S1 Sistem Informasi - Universitas Bina Sarana Informatika",
        "sertifikasi": ["Project Management Essentials"]
    },
    "Fakhri Hamdani": {
        "peran": "Sekretaris Jendral",
        "foto": "https://api.dicebear.com/7.x/avataaars/svg?seed=FakhriHamdani",
        "email": "fakhri.hamdani@email.com",
        "lokasi": "Indonesia",
        "ringkasan": (
            "Bertanggung jawab atas administrasi tim, penyusunan dokumentasi resmi proyek, pengelolaan risalah rapat, "
            "serta pencatatan spesifikasi kebutuhan perangkat lunak."
        ),
        "hard_skills": ["Technical Documentation", "Administrative Management", "Data Recording", "Markdown & Office Tools"],
        "soft_skills": ["Communication", "Organization", "Attention to Detail"],
        "pengalaman": [
            {
                "posisi": "Sekretaris Jendral",
                "institusi": "JBAW Corps",
                "tahun": "2025 - 2026",
                "deskripsi": "Mengelola seluruh dokumentasi administrasi dan arsip laporan kegiatan pengembangan proyek."
            }
        ],
        "pendidikan": "S1 Sistem Informasi - Universitas Bina Sarana Informatika",
        "sertifikasi": ["Administrative & Documentation Workshop"]
    },
    "Arip Rahman": {
        "peran": "Wakil Pertimbangan Ketua",
        "foto": "https://api.dicebear.com/7.x/avataaars/svg?seed=AripRahman",
        "email": "arip.rahman@email.com",
        "lokasi": "Indonesia",
        "ringkasan": (
            "Memberikan pertimbangan strategis, evaluasi teknis, serta masukan analitis terkait arah kebijakan "
            "dan pemecahan masalah dalam pengembangan sistem di dalam tim."
        ),
        "hard_skills": ["Strategic Analysis", "Problem Evaluation", "Quality Control Basic", "System Review"],
        "soft_skills": ["Critical Thinking", "Advisory", "Objective Decision Making"],
        "pengalaman": [
            {
                "posisi": "Wakil Pertimbangan Ketua",
                "institusi": "JBAW Corps",
                "tahun": "2025 - 2026",
                "deskripsi": "Memberikan telaah dan pertimbangan pada setiap keputusan besar perancangan arsitektur dan manajemen tim."
            }
        ],
        "pendidikan": "S1 Sistem Informasi - Universitas Bina Sarana Informatika",
        "sertifikasi": ["Critical Thinking & Analysis Course"]
    },
    "Pierro Ariessandy": {
        "peran": "Wakil Pertimbangan Ketua II",
        "foto": "https://api.dicebear.com/7.x/avataaars/svg?seed=PierroAriessandy",
        "email": "pierro.ariessandy@email.com",
        "lokasi": "Indonesia",
        "ringkasan": (
            "Mendukung fungsi pertimbangan strategis, pengawasan kualitas hasil kerja tim, serta memberikan masukan "
            "dari sudut pandang teknis maupun fungsional proyek."
        ),
        "hard_skills": ["Quality Assessment", "Risk Analysis", "Process Evaluation", "Technical Support"],
        "soft_skills": ["Analytical Skills", "Collaboration", "Constructive Feedback"],
        "pengalaman": [
            {
                "posisi": "Wakil Pertimbangan Ketua II",
                "institusi": "JBAW Corps",
                "tahun": "2025 - 2026",
                "deskripsi": "Membantu mengevaluasi hasil pengerjaan fitur dan memberikan saran perbaikan untuk kualitas sistem."
            }
        ],
        "pendidikan": "S1 Sistem Informasi - Universitas Bina Sarana Informatika",
        "sertifikasi": ["Quality Assurance & Evaluation Training"]
    }
}

PROJECTS_TEAM = [
    {
        "judul": "Digital Team E-CV & Portfolio (Streamlit)",
        "deskripsi": "Platform portofolio kolaboratif berbasis Python Streamlit dengan fitur tampilan CV individual 5 personil.",
        "tech": "Python, Streamlit, Git"
    },
    {
        "judul": "Sistem Informasi Peta Jalan ETPD",
        "deskripsi": "Aplikasi web monitoring dan penilaian elektronifikasi transaksi pemerintah daerah.",
        "tech": "Laravel, PHP 8.2, MySQL"
    }
]

# ==========================================
# 3. SIDEBAR NAVIGASI UTAMA
# ==========================================
with st.sidebar:
    st.title(f"🛡️ {TEAM_INFO['nama_tim']}")
    st.caption(TEAM_INFO["tagline"])
    st.divider()
    
    menu_utama = st.radio(
        "Menu Utama:",
        ["🏠 Beranda Tim", "📄 Lihat CV Individual", "🚀 Proyek Tim", "📬 Kontak"]
    )
    st.divider()
    st.caption(f"© 2026 {TEAM_INFO['nama_tim']}")

# ==========================================
# 4. KONTEN HALAMAN
# ==========================================
if menu_utama == "🏠 Beranda Tim":
    st.title(f"🛡️ Tim {TEAM_INFO['nama_tim']}")
    st.subheader(TEAM_INFO["tagline"])
    st.write(f"🏛️ **Institusi:** {TEAM_INFO['kampus']}")
    st.markdown("---")
    
    st.markdown("### 🌟 Struktur Kepengurusan Tim")
    st.write(
        "Website ini menampilkan portofolio kolaboratif serta kurikulum vitae (CV) digital "
        "dari kelima anggota inti **JBAW Corps**. Pilih menu **'Lihat CV Individual'** di sidebar "
        "untuk melihat profil lengkap masing-masing pengurus."
    )
    
    st.markdown("### 👥 Daftar Personil Tim:")
    cols = st.columns(3)
    for idx, (nama, data) in enumerate(MEMBERS_CV.items()):
        with cols[idx % 3]:
            with st.container(border=True):
                st.image(data["foto"], use_container_width=True)
                st.markdown(f"**{nama}**")
                st.caption(data["peran"])

elif menu_utama == "📄 Lihat CV Individual":
    st.title("📄 Kurikulum Vitae (CV) Individual Anggota")
    st.write("Pilih nama pengurus di bawah ini untuk menampilkan CV profesional secara mendetail.")
    st.divider()

    pilihan_anggota = st.selectbox(
        "🔍 Pilih Personil Tim:",
        options=list(MEMBERS_CV.keys())
    )

    cv = MEMBERS_CV[pilihan_anggota]
    st.markdown("---")

    col_foto, col_biodata = st.columns([1, 3], gap="large")
    with col_foto:
        st.image(cv["foto"], use_container_width=True)
        st.markdown(f"📍 **Lokasi:** {cv['lokasi']}")
        st.markdown(f"✉️ **Email:** {cv['email']}")
    with col_biodata:
        st.title(pilihan_anggota)
        st.subheader(cv["peran"])
        st.markdown("---")
        st.markdown("### 📝 Ringkasan Profesional")
        st.write(cv["ringkasan"])

    st.markdown("---")

    col_hard, col_soft = st.columns(2)
    with col_hard:
        st.markdown("### 💻 Hard Skills")
        for h in cv["hard_skills"]:
            st.markdown(f"- ✅ {h}")
    with col_soft:
        st.markdown("### 🤝 Soft Skills")
        for s in cv["soft_skills"]:
            st.markdown(f"- ⭐ {s}")

    st.markdown("---")
    st.markdown("### 💼 Pengalaman & Aktivitas")
    for exp in cv["pengalaman"]:
        with st.container(border=True):
            st.markdown(f"#### {exp['posisi']} | *{exp['institusi']}*")
            st.caption(f"🗓️ Periode: {exp['tahun']}")
            st.write(exp["deskripsi"])

    st.markdown("---")
    col_edu, col_cert = st.columns(2)
    with col_edu:
        st.markdown("### 🎓 Pendidikan")
        st.write(cv["pendidikan"])
    with col_cert:
        st.markdown("### 📜 Sertifikasi")
        for cert in cv["sertifikasi"]:
            st.markdown(f"- 🏅 {cert}")

elif menu_utama == "🚀 Proyek Tim":
    st.title("🚀 Portofolio Proyek Tim")
    st.write("Daftar karya aplikasi yang dikembangkan bersama oleh tim JBAW Corps.")
    st.divider()

    for proj in PROJECTS_TEAM:
        with st.container(border=True):
            st.subheader(proj["judul"])
            st.write(proj["deskripsi"])
            st.markdown(f"**Teknologi:** `{proj['tech']}`")

elif menu_utama == "📬 Kontak":
    st.title("📬 Hubungi Tim JBAW Corps")
    st.write("Kirimkan pesan atau tawaran kolaborasi kepada kelompok kami.")
    st.divider()

    with st.form("contact_form", clear_on_submit=True):
        nama = st.text_input("Nama Pengirim")
        email = st.text_input("Email Pengirim")
        pesan = st.text_area("Pesan")
        submit = st.form_submit_button("Kirim Pesan")

        if submit:
            if not nama or not email or not pesan:
                st.error("⚠️ Mohon lengkapi semua kolom!")
            elif "@" not in email:
                st.warning("⚠️ Format email tidak valid!")
            else:
                st.success(f"✅ Terima kasih, {nama}! Pesan berhasil dikirim ke tim.")
