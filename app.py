import streamlit as st

# ==========================================
# 1. KONFIGURASI HALAMAN & CUSTOM CSS
# ==========================================
st.set_page_config(
    page_title="Digital E-CV | Tim JBAW Corps",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        .stApp {
            background-color: #0b0f19;
            color: #f3f4f6;
        }
        [data-testid="stSidebar"] {
            background-color: #111827;
            border-right: 1px solid #1f2937;
        }
        h1, h2, h3, h4, h5, h6, p, span {
            color: #f9fafb !important;
        }
        .stButton > button {
            background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            padding: 0.5rem 1rem;
        }
        .stButton > button:hover {
            opacity: 0.9;
        }
    </style>
""", unsafe_allow_html=True)

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
        "foto": "https://github.com/muhammadarishidqi-dot/ecv-digital/raw/080a977a158eb0fac621ea2f7764457fbd3394af/WhatsApp%20Image%202026-10-17%20at%2020.11.14.jpeg",
        "email": "muhammadarishidqi@gmail.com",
        "no_telpon": "081384569849",
        "lokasi": "Jakarta, Indonesia",
        "ringkasan": (
            "Mahasiswa Sistem Informasi dan pengembang web yang berfokus pada pembangunan aplikasi "
            "berbasis backend & frontend menggunakan PHP (Laravel), pengelolaan database MySQL, serta perancangan "
            "arsitektur sistem terstruktur menggunakan UML, ERD, dan LRD."
        ),
        "hard_skills": ["PHP 8.2 & Laravel", "MySQL / Database", "Python & Streamlit", "UML, ERD & LRD Modeling"],
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
        "foto": "https://github.com/muhammadarishidqi-dot/ecv-digital/raw/080a977a158eb0fac621ea2f7764457fbd3394af/WhatsApp%20Image%202026-10-17%20at%2018.26.45.jpeg",
        "email": "dwisaputra030204@gmail.com",
        "no_telpon": "0881024853110",
        "lokasi": "Jakarta, Indonesia",
        "ringkasan": (
            "Seorang wakil ketua yang memiliki ketertarikan mendalam pada infrastruktur jaringan dan analitik sistem. "
            "Berpengalaman dalam perancangan basis data, konfigurasi jaringan berbasis Cisco, pengujian kualitas sistem (QA), "
            "serta pengembangan sistem penunjang keputusan untuk mendukung efisiensi operasional organisasi."
        ),
        "hard_skills": ["Database Design", "Cisco Network Configuration", "System Quality Assurance", "Decision Support Systems"],
        "soft_skills": ["Strategic Planning", "Team Coordination", "Analytical Thinking"],
        "pengalaman": [
            {
                "posisi": "Wakil Ketua Umum & System Evaluator",
                "institusi": "JBAW Corps",
                "tahun": "2025 - 2026",
                "deskripsi": "Mengawasi jaminan kualitas sistem dan pengelolaan infrastruktur jaringan pendukung proyek tim."
            }
        ],
        "pendidikan": "S1 Sistem Informasi - Universitas Bina Sarana Informatika",
        "sertifikasi": ["Cisco Network Essentials", "Quality Assurance Workshop"]
    },
    "Fakhri Hamdani": {
        "peran": "Sekretaris Jendral",
        "foto": "https://github.com/muhammadarishidqi-dot/ecv-digital/raw/080a977a158eb0fac621ea2f7764457fbd3394af/Screenshot%202026-10-17%20200917.png",
        "email": "fakhrihamdani30@gmail.com",
        "no_telpon": "088292106089",
        "lokasi": "Padang, Indonesia",
        "ringkasan": (
            "Berperan sebagai pengembang perangkat lunak dengan spesialisasi sebagai fullstack developer yang handal. "
            "Selain mengelola administrasi kesekretariatan dan dokumentasi proyek, ia aktif membangun dan merancang "
            "fungsionalitas aplikasi secara menyeluruh dari sisi antarmuka hingga logika pemrograman di balik layar."
        ),
        "hard_skills": ["Fullstack Web Development", "Frontend & Backend Integration", "Administrative Documentation", "Version Control (Git)"],
        "soft_skills": ["Communication", "Organization", "Time Management"],
        "pengalaman": [
            {
                "posisi": "Sekretaris Jendral & Fullstack Developer",
                "institusi": "JBAW Corps",
                "tahun": "2025 - 2026",
                "deskripsi": "Mengelola dokumentasi resmi tim sekaligus berkontribusi aktif dalam pengembangan fitur aplikasi secara end-to-end."
            }
        ],
        "pendidikan": "S1 Sistem Informasi - Universitas Bina Sarana Informatika",
        "sertifikasi": ["Fullstack Web Programming Certification"]
    },
    "Arip Rahman": {
        "peran": "Wakil Pertimbangan Ketua",
        "foto": "https://github.com/muhammadarishidqi-dot/ecv-digital/raw/080a977a158eb0fac621ea2f7764457fbd3394af/Screenshot%202026-10-17%20200823.png",
        "email": "Arief96.ar@gmail.com",
        "no_telpon": "081245711785",
        "lokasi": "Tasikmalaya, Indonesia",
        "ringkasan": (
            "Seorang profesional kreatif yang memadukan keahlian teknis pengolahan basis data dan perancangan antarmuka visual. "
            "Terampil dalam merancang tata letak UI/UX yang interaktif serta mengolah aset digital dan multimedia melalui keahlian "
            "editing grafis untuk memperkuat estetika produk digital."
        ),
        "hard_skills": ["Database Management", "UI/UX Design", "Graphic & Video Editing", "Figma & Design Tools"],
        "soft_skills": ["Creative Thinking", "Visual Communication", "Attention to Detail"],
        "pengalaman": [
            {
                "posisi": "Wakil Pertimbangan Ketua & UI/UX Specialist",
                "institusi": "JBAW Corps",
                "tahun": "2025 - 2026",
                "deskripsi": "Memberikan pertimbangan strategis visual dan mengelola perancangan antarmuka serta aset kreatif tim."
            }
        ],
        "pendidikan": "S1 Sistem Informasi - Universitas Bina Sarana Informatika",
        "sertifikasi": ["UI/UX Design & Multimedia Editing Course"]
    },
    "Pierro Ariessandy": {
        "peran": "Wakil Pertimbangan Ketua II",
        "foto": "https://github.com/muhammadarishidqi-dot/ecv-digital/raw/080a977a158eb0fac621ea2f7764457fbd3394af/WhatsApp%20Image%202026-10-17%20at%2018.59.46.jpeg",
        "email": "pieroariessandy2004@gmail.com",
        "no_telpon": "085711783214",
        "lokasi": "Banten, Indonesia",
        "ringkasan": (
            "Memiliki kompetensi kuat dalam pengembangan web modern, perancangan struktur basis data yang optimal, "
            "serta pembuatan desain grafis yang komunikatif. Berdedikasi untuk memastikan setiap solusi digital yang "
            "dibangun memiliki performa teknis yang solid dan tampilan visual yang menarik."
        ),
        "hard_skills": ["Web Development", "Database Management", "Graphic Design", "Responsive Layout"],
        "soft_skills": ["Analytical Skills", "Collaboration", "Constructive Feedback"],
        "pengalaman": [
            {
                "posisi": "Wakil Pertimbangan Ketua II",
                "institusi": "JBAW Corps",
                "tahun": "2025 - 2026",
                "deskripsi": "Membantu mengevaluasi fungsionalitas sistem web dan memberikan masukan desain grafis untuk proyek."
            }
        ],
        "pendidikan": "S1 Sistem Informasi - Universitas Bina Sarana Informatika",
        "sertifikasi": ["Web Developer & Graphic Design Training"]
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
    st.markdown("### 🛡️ JBAW CORPS")
    pages = ["🏠 Beranda Tim", "📄 Lihat CV Individual", "🚀 Proyek Tim", "📬 Kontak"]
    menu_utama = st.radio("Navigasi Menu", pages, label_visibility="collapsed")
    st.divider()
    st.caption(f"© 2026 {TEAM_INFO['nama_tim']}")

# ==========================================
# 4. KONTEN HALAMAN
# ==========================================
if menu_utama == "🏠 Beranda Tim":
    st.markdown(f"# 🛡️ Tim {TEAM_INFO['nama_tim']}")
    st.markdown(f"*{TEAM_INFO['tagline']}*")
    st.markdown(f"🏛️ **Institusi:** {TEAM_INFO['kampus']}")
    st.markdown("---")
    
    st.markdown("### 🌟 Struktur Kepengurusan Tim")
    st.info(
        "Website ini menampilkan portofolio kolaboratif serta kurikulum vitae (CV) digital "
        "dari kelima anggota inti **JBAW Corps**. Pilih menu **'Lihat CV Individual'** di sidebar "
        "untuk melihat profil lengkap masing-masing pengurus."
    )
    
    st.markdown("### 👥 Daftar Personil Tim")
    
    # Menggunakan st.container(border=True) agar tampil rapi dan simetris secara otomatis
    names = list(MEMBERS_CV.keys())
    
    # Baris pertama (3 orang)
    cols1 = st.columns(3)
    for i in range(3):
        nama = names[i]
        data = MEMBERS_CV[nama]
        with cols1[i]:
            with st.container(border=True):
                st.image(data["foto"], use_container_width=True)
                st.markdown(f"#### {nama}")
                st.caption(data["peran"])

    # Baris kedua (2 orang)
    cols2 = st.columns(2)
    for i in range(3, 5):
        nama = names[i]
        data = MEMBERS_CV[nama]
        with cols2[i - 3]:
            with st.container(border=True):
                st.image(data["foto"], use_container_width=True)
                st.markdown(f"#### {nama}")
                st.caption(data["peran"])

elif menu_utama == "📄 Lihat CV Individual":
    st.markdown("# 📄 Kurikulum Vitae (CV) Individual Anggota")
    st.markdown("Pilih nama pengurus di bawah ini untuk menampilkan CV profesional secara mendetail.")
    st.markdown("---")

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
        st.markdown(f"📞 **Telepon:** {cv['no_telpon']}")
    with col_biodata:
        st.markdown(f"## {pilihan_anggota}")
        st.markdown(f"### `{cv['peran']}`")
        st.markdown("---")
        st.markdown("#### 📝 Ringkasan Profesional")
        st.write(cv["ringkasan"])

    st.markdown("---")

    col_hard, col_soft = st.columns(2)
    with col_hard:
        st.markdown("#### 💻 Hard Skills")
        for h in cv["hard_skills"]:
            st.markdown(f"- ✅ {h}")
    with col_soft:
        st.markdown("#### 🤝 Soft Skills")
        for s in cv["soft_skills"]:
            st.markdown(f"- ⭐ {s}")

    st.markdown("---")
    st.markdown("#### 💼 Pengalaman & Aktivitas")
    for exp in cv["pengalaman"]:
        with st.container(border=True):
            st.markdown(f"**{exp['posisi']}** | *{exp['institusi']}*")
            st.caption(f"🗓️ Periode: {exp['tahun']}")
            st.write(exp["deskripsi"])

    st.markdown("---")
    col_edu, col_cert = st.columns(2)
    with col_edu:
        with st.container(border=True):
            st.markdown("#### 🎓 Pendidikan")
            st.write(cv["pendidikan"])
    with col_cert:
        with st.container(border=True):
            st.markdown("#### 📜 Sertifikasi")
            for cert in cv["sertifikasi"]:
                st.markdown(f"- 🏅 {cert}")

elif menu_utama == "🚀 Proyek Tim":
    st.markdown("# 🚀 Portofolio Proyek Tim")
    st.markdown("Daftar karya aplikasi yang dikembangkan bersama oleh tim JBAW Corps.")
    st.markdown("---")

    for proj in PROJECTS_TEAM:
        with st.container(border=True):
            st.markdown(f"### 📁 {proj['judul']}")
            st.write(proj["deskripsi"])
            st.markdown(f"**Teknologi:** `{proj['tech']}`")

elif menu_utama == "📬 Kontak":
    st.markdown("# 📬 Hubungi Tim JBAW Corps")
    st.markdown("Kirimkan pesan atau tawaran kolaborasi kepada kelompok kami.")
    st.markdown("---")

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
