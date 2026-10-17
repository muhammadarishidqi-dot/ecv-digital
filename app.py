import streamlit as st

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="Digital E-CV | Muhammad Ari Shidqi",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. DATA PROFIL (Terpisah dari Komponen UI)
# ==========================================
PROFILE_DATA = {
    "nama": "Muhammad Ari Shidqi",
    "headline": "Web Developer | Backend & System Modeling Enthusiast",
    "lokasi": "Indonesia",
    "ringkasan": (
        "Mahasiswa dan pengembang web yang berfokus pada pembangunan aplikasi "
        "berbasis backend menggunakan PHP (Laravel), pengelolaan database MySQL, "
        "serta integrasi sistem dengan Node.js dan Python. Terbiasa merancang "
        "arsitektur sistem secara terstruktur menggunakan UML, ERD, dan LRD "
        "untuk menghasilkan solusi digital yang fungsional dan tepat guna."
    ),
    "foto_url": "https://api.dicebear.com/7.x/avataaars/svg?seed=AriShidqi",
    "quick_stats": [
        {"label": "Fokus Keahlian", "value": "Backend & Web Dev"},
        {"label": "Tech Stack Utama", "value": "Laravel, PHP, MySQL"},
        {"label": "Status", "value": "Open to Opportunities"}
    ]
}

# ==========================================
# 3. KOMPONEN NAVIGASI (SIDEBAR)
# ==========================================
def render_sidebar():
    with st.sidebar:
        st.image(PROFILE_DATA["foto_url"], width=120)
        st.markdown(f"### {PROFILE_DATA['nama']}")
        st.caption(PROFILE_DATA["headline"])
        st.divider()
        
        menu = st.radio(
            "Navigasi Halaman:",
            options=[
                "🏠 Home & About",
                "🛠️ Skills",
                "💼 Experience",
                "🚀 Projects",
                "🎓 Education",
                "📬 Contact"
            ]
        )
        st.divider()
        st.caption("© 2026 Digital E-CV")
    return menu

# ==========================================
# 4. KOMPONEN TAMPILAN PER HALAMAN
# ==========================================
def render_home_about():
    col1, col2 = st.columns([1, 3], gap="large")
    
    with col1:
        st.image(PROFILE_DATA["foto_url"], use_container_width=True)
        
    with col2:
        st.title(PROFILE_DATA["nama"])
        st.subheader(PROFILE_DATA["headline"])
        st.write(f"📍 **Lokasi:** {PROFILE_DATA['lokasi']}")
        st.markdown("---")
        st.markdown("### Tentang Saya")
        st.write(PROFILE_DATA["ringkasan"])

    st.divider()
    
    cols = st.columns(3)
    for idx, stat in enumerate(PROFILE_DATA["quick_stats"]):
        with cols[idx]:
            st.metric(label=stat["label"], value=stat["value"])

def render_placeholder(nama_halaman):
    st.title(nama_halaman)
    st.info(f"Bagian **{nama_halaman}** akan kita isi pada Sub-Goal berikutnya!")

# ==========================================
# 5. PROGRAM UTAMA (MAIN ROUTER)
# ==========================================
def main():
    pilihan_menu = render_sidebar()
    
    if pilihan_menu == "🏠 Home & About":
        render_home_about()
    elif pilihan_menu == "🛠️ Skills":
        render_placeholder("🛠️ Kompetensi & Keahlian (Skills)")
    elif pilihan_menu == "💼 Experience":
        render_placeholder("💼 Pengalaman (Experience)")
    elif pilihan_menu == "🚀 Projects":
        render_placeholder("🚀 Portofolio Proyek (Projects)")
    elif pilihan_menu == "🎓 Education":
        render_placeholder("🎓 Pendidikan & Sertifikasi (Education)")
    elif pilihan_menu == "📬 Contact":
        render_placeholder("📬 Kontak & Tautan Profesional (Contact)")

if __name__ == "__main__":
    main()
