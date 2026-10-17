import streamlit as st
from html import escape

st.set_page_config(
    page_title="Digital E-CV | JBAW Corps",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
:root { --bg:#071326; --panel:#0c1b32; --panel2:#102541; --line:#1c3557; --blue:#2f8cff; --blue2:#67b4ff; --text:#edf5ff; --muted:#9eb3ce; }
.stApp { background: radial-gradient(ellipse at 75% 0%, #102c50 0%, var(--bg) 42%); color:var(--text); font-family:'DM Sans',sans-serif; }
[data-testid="stHeader"] { background:rgba(7,19,38,.75); }
[data-testid="stSidebar"] { background:linear-gradient(180deg,#08162a,#0b1d35); border-right:1px solid var(--line); }
[data-testid="stSidebar"] * { color:var(--text); }
.block-container { padding-top:2.2rem; padding-bottom:3rem; max-width:1500px; }
h1,h2,h3,h4 { font-family:'Manrope',sans-serif!important; letter-spacing:-.035em; color:var(--text)!important; }
p,li,label,.stMarkdown { color:var(--text); }
small,.muted { color:var(--muted)!important; }
[data-testid="stRadio"] label { padding: .55rem .7rem; border-radius:10px; }
[data-testid="stRadio"] label:hover { background:#132b49; }
.stButton>button, .stFormSubmitButton>button { border:1px solid #2d82e9; background:linear-gradient(135deg,#1676e8,#2f9bff); color:white; border-radius:10px; padding:.62rem 1.05rem; font-weight:700; transition:all .2s ease; }
.stButton>button:hover,.stFormSubmitButton>button:hover { border-color:#79bdff; box-shadow:0 8px 24px #1676e833; transform:translateY(-1px); color:white; }
.stSelectbox [data-baseweb="select"]>div,.stTextInput input,.stTextArea textarea { background:#0b1c32; border-color:#294465; color:var(--text); border-radius:10px; }
hr { border-color:var(--line)!important; }
.eyebrow { text-transform:uppercase; letter-spacing:.18em; color:var(--blue2); font-size:.76rem; font-weight:800; margin-bottom:.65rem; }
.hero { padding:2.6rem; border:1px solid #23466e; border-radius:24px; background:linear-gradient(120deg,rgba(18,49,84,.98),rgba(8,24,45,.94)); position:relative; overflow:hidden; box-shadow:0 24px 70px #00000025; }
.hero:after { content:''; position:absolute; width:300px;height:300px;right:-80px;top:-100px;border-radius:50%;background:radial-gradient(circle,#268bff44,transparent 68%); }
.hero h1 { font-size:clamp(2.4rem,5vw,4.5rem)!important; line-height:1.02; margin:.15rem 0 .75rem; }
.hero p { color:#c2d4ea; max-width:760px; line-height:1.75; }
.stat { background:#0b1d34; border:1px solid #1b385c; border-radius:15px; padding:1rem 1.1rem; height:100%; }
.stat-number { color:#73baff; font-size:1.55rem; font-weight:800; font-family:'Manrope',sans-serif; }
.stat-label { color:#9eb3ce; font-size:.82rem; margin-top:.2rem; }
.section-head { margin:2rem 0 1rem; }
.member-card,.project-card,.detail-panel { background:linear-gradient(160deg,#102541,#0a192d); border:1px solid #1d3a5e; border-radius:18px; padding:1.15rem; height:100%; transition:transform .2s ease,border-color .2s ease,box-shadow .2s ease; }
.member-card:hover,.project-card:hover { transform:translateY(-4px); border-color:#338fff; box-shadow:0 15px 34px #00000025; }
.member-photo { display:block; width:100%; height:205px; object-fit:cover; object-position:center 22%; border-radius:12px; border:1px solid #31577e; margin-bottom:1rem; background:#132b49; }
.profile-photo { display:block; width:100%; height:auto; max-height:460px; object-fit:contain; object-position:center top; border-radius:12px; border:1px solid #31577e; margin-bottom:1rem; background:#071326; }
.member-name { font-family:'Manrope',sans-serif; font-size:1.05rem; font-weight:800; margin-bottom:.3rem; }
.profile-heading { text-align:center; padding:.15rem .25rem .85rem; border-bottom:1px solid #1b3553; margin-bottom:.35rem; }
.profile-name { font-family:'Manrope',sans-serif; font-size:1.15rem; font-weight:800; line-height:1.35; color:#edf5ff; margin:.65rem 0 .5rem; overflow-wrap:anywhere; }
.role-pill { display:inline-flex; align-items:center; justify-content:center; max-width:100%; white-space:normal; text-align:center; line-height:1.4; border:1px solid #2c70b9; background:linear-gradient(135deg,#12345a,#102744); color:#a9d5ff; padding:.42rem .8rem; border-radius:999px; font-size:.78rem; font-weight:700; margin:.1rem auto .35rem; box-shadow:0 4px 14px #1676e81a; }
.profile-photo { margin-bottom:.75rem; }
.detail-panel .info-line:last-child { border-bottom:0; }
.member-card { display:flex; flex-direction:column; }
.member-photo { object-position:center 22%; }
@media(max-width:700px){.profile-name{font-size:1.05rem}.role-pill{font-size:.74rem}}
.card-copy { color:#b5c8df; font-size:.88rem; line-height:1.6; }
.skill-pill { display:inline-block; background:#102b4a; border:1px solid #24496f; color:#b9dcff; padding:.28rem .55rem; border-radius:7px; font-size:.75rem; margin:.18rem .12rem .1rem 0; }
.project-icon { width:48px;height:48px;border-radius:13px;background:#123b68;border:1px solid #2464a2;display:flex;align-items:center;justify-content:center;font-size:1.35rem;margin-bottom:1rem; }
.info-line { padding:.55rem 0; border-bottom:1px solid #1b3553; color:#c0d1e5; overflow-wrap:anywhere; }
.footer { color:#7893b4; font-size:.8rem; padding-top:1.5rem; margin-top:2.5rem; border-top:1px solid #1b3553; }
[data-testid="stForm"] { background:#0b1c32; border:1px solid #1d3a5e; border-radius:18px; padding:1.3rem; }
@media(max-width:700px){.hero{padding:1.5rem}.member-photo{height:180px}}
</style>
""", unsafe_allow_html=True)

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
        "deskripsi": "Platform portofolio kolaboratif berbasis Python Streamlit dengan fitur tampilan CV individual 5 personil yang terintegrasi secara seamless.",
        "tech": "Python, Streamlit, HTML/CSS"
    },
    {
        "judul": "Sistem Informasi Peta Jalan ETPD",
        "deskripsi": "Aplikasi web monitoring dan penilaian elektronifikasi transaksi pemerintah daerah dengan fitur multi-role otorisasi dan validasi dokumen.",
        "tech": "Laravel, PHP 8.2, MySQL"
    }
]


# Sidebar navigasi
with st.sidebar:
    st.markdown("<div style='font-size:2rem;margin:0.4rem 0'>🛡️</div><h2 style='margin:0'>JBAW CORPS</h2><p style='color:#8eabd0!important;font-size:.85rem'>Digital E-CV & Portfolio</p>", unsafe_allow_html=True)
    st.divider()
    pages = ["🏠  Beranda Tim", "📄  CV Individual", "🚀  Proyek Tim", "✉️  Kontak"]
    default_page = st.session_state.pop("selected_page", "Beranda Tim")
    page_labels = {"Beranda Tim": pages[0], "CV Individual": pages[1], "Proyek Tim": pages[2], "Kontak": pages[3]}
    menu_utama = st.radio("NAVIGASI", pages, index=pages.index(page_labels.get(default_page, pages[0])), label_visibility="visible")
    st.divider()
    st.markdown("<div style='color:#7f9bbd;font-size:.78rem;line-height:1.7'>Digital Creative<br>Software Development Squad</div>", unsafe_allow_html=True)
    st.caption(f"© 2026 {TEAM_INFO['nama_tim']}")

if menu_utama == "🏠  Beranda Tim":
    st.markdown(f"""<div class='hero'><div class='eyebrow'>DIGITAL E-CV · TEAM PORTFOLIO</div><h1>{escape(TEAM_INFO['nama_tim'])}</h1><h3 style='font-weight:600;color:#c8e2ff!important'>{escape(TEAM_INFO['tagline'])}</h3><p>Kolaborasi, kreativitas, dan teknologi dalam satu tim. Kenali personel, keahlian, serta proyek digital yang kami kembangkan bersama.</p><div style='margin-top:1.2rem;color:#b6d7f9'>⌂ &nbsp; {escape(TEAM_INFO['kampus'])}</div></div>""", unsafe_allow_html=True)
    st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)
    a,b,c = st.columns(3)
    for col,number,label in [(a,str(len(MEMBERS_CV)),"Personel Tim"),(b,str(sum(len(m['hard_skills']) for m in MEMBERS_CV.values())),"Keahlian Teknis"),(c,str(len(PROJECTS_TEAM)),"Proyek Tim")]:
        with col: st.markdown(f"<div class='stat'><div class='stat-number'>{number}</div><div class='stat-label'>{label}</div></div>",unsafe_allow_html=True)
    st.markdown("<div class='section-head'><div class='eyebrow'>TIM KAMI</div><h2>Profil Anggota</h2><p style='color:#9eb3ce'>Kenali orang-orang di balik ide dan solusi digital JBAW Corps.</p></div>",unsafe_allow_html=True)
    cols = st.columns(3, gap="medium")
    for i,(nama,data) in enumerate(MEMBERS_CV.items()):
        with cols[i%3]:
            # Beranda dibuat fokus pada foto saja; jabatan, deskripsi, dan daftar skill disembunyikan.
            st.markdown(
                f"<div class='member-card' style='padding:.8rem'><img class='member-photo' style='height:260px;margin-bottom:0' src='{escape(data['foto'], quote=True)}' alt='Foto anggota {escape(nama, quote=True)}'></div>",
                unsafe_allow_html=True,
            )
            if st.button("Lihat CV →", key=f"member_{i}", use_container_width=True):
                st.session_state["selected_member"] = nama
                st.session_state["selected_page"] = "CV Individual"
                st.rerun()

elif menu_utama == "📄  CV Individual":
    st.markdown("<div class='eyebrow'>PROFIL PROFESIONAL</div><h1>CV Individual</h1><p style='color:#9eb3ce'>Informasi, pengalaman, dan keahlian anggota JBAW Corps.</p>",unsafe_allow_html=True)
    default_name = st.session_state.get("selected_member", list(MEMBERS_CV.keys())[0])
    options = list(MEMBERS_CV.keys())
    pilihan_anggota = st.selectbox("Pilih anggota", options, index=options.index(default_name) if default_name in options else 0)
    st.session_state["selected_member"] = pilihan_anggota
    cv = MEMBERS_CV[pilihan_anggota]
    left,right = st.columns([1,2.4],gap="large")
    with left:
        st.markdown(f"<div class='detail-panel'><img class='profile-photo' src='{escape(cv['foto'], quote=True)}' alt='Foto {escape(pilihan_anggota, quote=True)}'><div class='profile-heading'><div class='profile-name'>{escape(pilihan_anggota)}</div><div class='role-pill'>{escape(cv['peran'])}</div></div><div class='info-line'>⌖ &nbsp; {escape(cv['lokasi'])}</div><div class='info-line'>✉ &nbsp; {escape(cv['email'])}</div><div class='info-line'>☎ &nbsp; {escape(cv['no_telpon'])}</div></div>",unsafe_allow_html=True)
    with right:
        st.markdown(f"<div class='eyebrow'>RINGKASAN</div><h2>{escape(pilihan_anggota)}</h2><p style='color:#b9cce2;line-height:1.8'>{escape(cv['ringkasan'])}</p>",unsafe_allow_html=True)
        st.markdown("<div class='section-head'><h3>Keahlian</h3></div>",unsafe_allow_html=True)
        x,y = st.columns(2)
        with x:
            st.markdown("**Hard Skills**")
            for skill in cv["hard_skills"]: st.markdown(f"<span class='skill-pill'>{escape(skill)}</span>",unsafe_allow_html=True)
        with y:
            st.markdown("**Soft Skills**")
            for skill in cv["soft_skills"]: st.markdown(f"<span class='skill-pill'>{escape(skill)}</span>",unsafe_allow_html=True)
    st.markdown("<div class='section-head'><div class='eyebrow'>PERJALANAN PROFESIONAL</div><h2>Pengalaman & Aktivitas</h2></div>",unsafe_allow_html=True)
    for exp in cv["pengalaman"]:
        # Informasi jabatan tidak ditampilkan; institusi, periode, dan uraian pengalaman tetap ada.
        st.markdown(f"<div class='detail-panel'><div style='color:#73baff;font-weight:600'>{escape(exp['institusi'])} · {escape(exp['tahun'])}</div><p style='color:#b9cce2;line-height:1.7;margin-bottom:0'>{escape(exp['deskripsi'])}</p></div>",unsafe_allow_html=True)
    x,y=st.columns(2,gap="medium")
    with x:
        cert_edu = f"<div class='detail-panel'><div class='eyebrow'>PENDIDIKAN</div><h3>🎓 Pendidikan</h3><p class='card-copy'>{escape(cv['pendidikan'])}</p></div>"
        st.markdown(cert_edu,unsafe_allow_html=True)
    with y:
        certs = ''.join(f"<li>{escape(cert)}</li>" for cert in cv['sertifikasi'])
        st.markdown(f"<div class='detail-panel'><div class='eyebrow'>PENGEMBANGAN DIRI</div><h3>📜 Sertifikasi</h3><ul>{certs}</ul></div>",unsafe_allow_html=True)

elif menu_utama == "🚀  Proyek Tim":
    st.markdown("<div class='eyebrow'>KARYA & INOVASI</div><h1>Portofolio Proyek</h1><p style='color:#9eb3ce'>Solusi digital yang dikembangkan dan dirancang oleh JBAW Corps.</p>",unsafe_allow_html=True)
    cols=st.columns(2,gap="large")
    for i,proj in enumerate(PROJECTS_TEAM):
        with cols[i%2]:
            st.markdown(f"<div class='project-card'><div class='project-icon'>{'⌘' if i==0 else '▦'}</div><div class='eyebrow'>PROJECT 0{i+1}</div><h2 style='font-size:1.4rem'>{escape(proj['judul'])}</h2><p class='card-copy' style='min-height:100px'>{escape(proj['deskripsi'])}</p><div style='color:#8fbfff;font-size:.76rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;margin:.9rem 0 .4rem'>Teknologi</div><span class='skill-pill'>{escape(proj['tech'])}</span></div>",unsafe_allow_html=True)

elif menu_utama == "✉️  Kontak":
    st.markdown("<div class='eyebrow'>MARI TERHUBUNG</div><h1>Hubungi JBAW Corps</h1><p style='color:#9eb3ce'>Punya pertanyaan, ide, atau peluang kolaborasi? Kirimkan pesan kepada tim kami.</p>",unsafe_allow_html=True)
    left,right=st.columns([1,1.4],gap="large")
    with left:
        st.markdown("<div class='detail-panel'><div class='eyebrow'>JBAW CORPS</div><h2>Let's build something meaningful.</h2><p class='card-copy'>Kami terbuka untuk kolaborasi, diskusi ide, dan pengembangan solusi digital.</p><div class='info-line'>⌂ &nbsp; Universitas Bina Sarana Informatika</div><div class='info-line'>✉ &nbsp; Kontak anggota tersedia pada halaman CV Individual</div></div>",unsafe_allow_html=True)
    with right:
        with st.form("contact_form", clear_on_submit=True):
            st.markdown("### Kirim pesan")
            nama=st.text_input("Nama lengkap",placeholder="Masukkan nama Anda")
            email=st.text_input("Alamat email",placeholder="nama@email.com")
            pesan=st.text_area("Pesan",placeholder="Ceritakan kebutuhan atau ide kolaborasi Anda...",height=150)
            submit=st.form_submit_button("Kirim Pesan →",use_container_width=True)
            if submit:
                if not nama.strip() or not email.strip() or not pesan.strip(): st.error("Mohon lengkapi semua kolom sebelum mengirim.")
                elif "@" not in email or "." not in email.rsplit("@",1)[-1]: st.warning("Format email belum valid. Periksa kembali alamat email Anda.")
                else: st.success(f"Terima kasih, {nama}! Formulir berhasil divalidasi. Catatan: pesan belum dikirim ke email/database karena integrasi pengiriman belum tersedia.")

st.markdown(f"<div class='footer'>© 2026 {escape(TEAM_INFO['nama_tim'])} · Digital Creative & Software Development Squad</div>",unsafe_allow_html=True)
