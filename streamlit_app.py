import streamlit as st

# ==========================================
# KONFIGURASI & CSS CUSTOM
# ==========================================

st.set_page_config(
    page_title="Kalkulator Kimia",
    page_icon="⚗️",
    layout="wide"
)

# CSS Custom untuk tampilan yang lebih menarik
st.markdown("""
<style>
    /* Styling Utama */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Styling Headers */
    h1 {
        color: #1e3a5f;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    
    /* Styling Cards */
    .card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    
    /* Styling Rumus */
    .rumus-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    /* Styling Hasil */
    .hasil-box {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
    }
    
    /* Styling Unsur Periodik */
    .unsur-card {
        background: white;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }
    
    /* Styling Tab Headers */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #667eea;
        color: white;
        border-radius: 8px 8px 0 0;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# DATA UNSUR PERIODIK
# ==========================================

UNSUR = {
    "H": {"nomor": 1, "nama": "Hidrogen", "massa": 1.008, "warna": "#FF6B6B"},
    "He": {"nomor": 2, "nama": "Helium", "massa": 4.0026, "warna": "#4ECDC4"},
    "Li": {"nomor": 3, "nama": "Litium", "massa": 6.94, "warna": "#95E1D3"},
    "Be": {"nomor": 4, "nama": "Berilium", "massa": 9.0122, "warna": "#F38181"},
    "B": {"nomor": 5, "nama": "Boron", "massa": 10.81, "warna": "#FCE38A"},
    "C": {"nomor": 6, "nama": "Karbon", "massa": 12.011, "warna": "#2C3E50"},
    "N": {"nomor": 7, "nama": "Nitrogen", "massa": 14.007, "warna": "#3498DB"},
    "O": {"nomor": 8, "nama": "Oksigen", "massa": 15.999, "warna": "#E74C3C"},
    "F": {"nomor": 9, "nama": "Fluor", "massa": 18.998, "warna": "#1ABC9C"},
    "Ne": {"nomor": 10, "nama": "Neon", "massa": 20.180, "warna": "#9B59B6"},
    "Na": {"nomor": 11, "nama": "Natrium", "massa": 22.990, "warna": "#F39C12"},
    "Mg": {"nomor": 12, "nama": "Magnesium", "massa": 24.305, "warna": "#27AE60"},
    "Al": {"nomor": 13, "nama": "Aluminium", "massa": 26.982, "warna": "#BDC3C7"},
    "Si": {"nomor": 14, "nama": "Silikon", "massa": 28.085, "warna": "#34495E"},
    "P": {"nomor": 15, "nama": "Fosfor", "massa": 30.974, "warna": "#E67E22"},
    "S": {"nomor": 16, "nama": "Belerang", "massa": 32.06, "warna": "#F1C40F"},
    "Cl": {"nomor": 17, "nama": "Klor", "massa": 35.45, "warna": "#2ECC71"},
    "Ar": {"nomor": 18, "nama": "Argon", "massa": 39.948, "warna": "#8E44AD"},
    "K": {"nomor": 19, "nama": "Kalium", "massa": 39.098, "warna": "#16A085"},
    "Ca": {"nomor": 20, "nama": "Kalsium", "massa": 40.078, "warna": "#ECF0F1"},
    "Fe": {"nomor": 26, "nama": "Besi", "massa": 55.845, "warna": "#C0392B"},
    "Cu": {"nomor": 29, "nama": "Tembaga", "massa": 63.546, "warna": "#D35400"},
    "Zn": {"nomor": 30, "nama": "Seng", "massa": 65.38, "warna": "#7F8C8D"},
    "Br": {"nomor": 35, "nama": "Brom", "massa": 79.904, "warna": "#8E44AD"},
    "Ag": {"nomor": 47, "nama": "Perak", "massa": 107.87, "warna": "#BDC3C7"},
    "I": {"nomor": 53, "nama": "Iodium", "massa": 126.90, "warna": "#2C3E50"},
    "Au": {"nomor": 79, "nama": "Emas", "massa": 196.97, "warna": "#FFD700"},
    "Hg": {"nomor": 80, "nama": "Raksa", "massa": 200.59, "warna": "#5D6D7E"},
    "Pb": {"nomor": 82, "nama": "Timbal", "massa": 207.2, "warna": "#34495E"}
}

# ==========================================
# INISIALISASI SESSION STATE
# ==========================================

if 'riwayat' not in st.session_state:
    st.session_state.riwayat = []

# ==========================================
# FUNGSI-FUNGSI LOGIKA
# ==========================================

def simpan_riwayat(data):
    st.session_state.riwayat.insert(0, data)

def hapus_riwayat():
    st.session_state.riwayat = []

def hitung_larutan(mr, volume, molaritas):
    if mr <= 0 or volume <= 0 or molaritas <= 0:
        return None
    massa = molaritas * (volume / 1000) * mr
    return massa

def hitung_v2(m1, v1, m2):
    if m1 <= 0 or v1 <= 0 or m2 <= 0:
        return None
    v2 = (m1 * v1) / m2
    return v2

def hitung_v1(m1, m2, v2):
    if m1 <= 0 or m2 <= 0 or v2 <= 0:
        return None
    v1 = (m2 * v2) / m1
    return v1

def hitung_m2(m1, v1, v2):
    if m1 <= 0 or v1 <= 0 or v2 <= 0:
        return None
    m2 = (m1 * v1) / v2
    return m2

def hitung_m1(v1, m2, v2):
    if v1 <= 0 or m2 <= 0 or v2 <= 0:
        return None
    m1 = (m2 * v2) / v1
    return m1

# ==========================================
# TAMPILAN UTAMA
# ==========================================

# Header dengan Emoji
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <h1 style="font-size: 48px; margin-bottom: 10px;">⚗️ Kalkulator Kimia</h1>
    <p style="font-size: 18px; color: #666;">Aplikasi Pembelajaran Kimia Sederhana</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Tab Menu dengan Ikon
tab_larutan, tab_pengenceran, tab_periodik = st.tabs([
    "🧪 Pembuatan Larutan", 
    "💧 Pengenceran", 
    "📊 Tabel Periodik"
])

# ======================
# TAB 1: PEMBUATAN LARUTAN
# ======================
with tab_larutan:
    st.markdown("""
    <div style="background: white; padding: 20px; border-radius: 15px; margin-bottom: 20px;">
        <h2 style="color: #1e3a5f; margin-top: 0;">🧪 Hitung Massa Zat Terlarut</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Tampilkan Rumus dengan Styling
    with st.expander("📐 Lihat Rumus dan Referensi"):
        st.markdown("""
        **Rumus Pembuatan Larutan:**
        
        ```
        Massa = Molaritas × (Volume ÷ 1000) × Mr
        ```
        
        atau
        
        ```
        Massa (g) = M (mol/L) × V (L) × Mr (g/mol)
        ```
        
        ---
        
        **📚 Sumber Referensi:**
        
        1. Petrucci, R.H. et al. (2017). *General Chemistry: Principles & Modern Applications*. Pearson.
        
        2. Atkin, P. (2020). *Chemical Principles*. Oxford University Press.
        
        3. IUPAC (2024). *Compendium of Chemical Terminology*. https://goldbook.iupac.org/
        """)
    
    # Input dengan Layout Lebih Baik
    cols = st.columns([1, 1, 1])
    with cols[0]:
        st.markdown("**📋 Input Data:**")
        mr = st.number_input("⚛️ Massa Molar (Mr) [g/mol]", min_value=0.0, key="mr_input", help="Massa molar zat yang akan larut")
    with cols[1]:
        volume = st.number_input("🧪 Volume (V) [mL]", min_value=0.0, key="vol_input", help="Volume larutan akhir yang diinginkan")
    with cols[2]:
        molaritas = st.number_input("📈 Konsentrasi (M) [mol/L]", min_value=0.0, key="mol_input", help="Konsentrasi molar larutan")
    
    st.markdown("<br>", unsafe_allow_html=True)
    hitung_btn = st.button("🧮 Hitung Massa", type="primary", use_container_width=True)
    
    if hitung_btn:
        if mr <= 0 or volume <= 0 or molaritas <= 0:
            st.error("⚠️ Semua nilai harus lebih dari 0!")
        else:
            massa = hitung_larutan(mr, volume, molaritas)
            st.markdown("""
            <div class="hasil-box" style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);">
                ⚗️ Massa yang dibutuhkan: {:.4f} gram
            </div>
            """.format(massa), unsafe_allow_html=True)
            simpan_riwayat("Larutan -> Mr=" + str(mr) + "g/mol, V=" + str(volume) + "mL, M=" + str(molaritas) + "M => Massa: {:.4f}g".format(massa))
            st.rerun()

# ======================
# TAB 2: PENGENCERAN
# ======================
with tab_pengenceran:
    st.markdown("""
    <div style="background: white; padding: 20px; border-radius: 15px; margin-bottom: 20px;">
        <h2 style="color: #1e3a5f; margin-top: 0;">💧 Pengenceran Larutan</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Sub-Tab untuk Semua Variabel
    subtab_v2, subtab_v1, subtab_m2, subtab_m1 = st.tabs([
        "📊 Hitung V₂", 
        "📏 Hitung V₁", 
        "📈 Hitung M₂", 
        "📉 Hitung M₁"
    ])
    
    # --- Hitung V2 ---
    with subtab_v2:
        st.markdown("**🔍 Mencari: Volume Akhir (V₂)**")
        with st.expander("📐 Rumus V₂"):
            st.markdown("""
            ```
            V₂ = (M₁ × V₁) ÷ M₂
            ```
            
            **Dari persamaan:** M₁ × V₁ = M₂ × V₂
            
            ---
            📚 *Referensi: Petrucci, R.H. et al. (2017). General Chemistry.*
            """)
        
        cols = st.columns([1, 1, 1])
        with cols[0]:
            m1 = st.number_input("⚛️ M₁ (awal) [M]", min_value=0.0, key="m1_v2")
        with cols[1]:
            v1 = st.number_input("🧪 V₁ (awal) [mL]", min_value=0.0, key="v1_v2")
        with cols[2]:
            m2 = st.number_input("📈 M₂ (akhir) [M]", min_value=0.0, key="m2_v2")
        
        if st.button("🧮 Hitung V₂", key="btn_v2", use_container_width=True):
            if m1 <= 0 or v1 <= 0 or m2 <= 0:
                st.error("⚠️ Semua nilai harus lebih dari 0!")
            else:
                v2 = hitung_v2(m1, v1, m2)
                st.markdown("""
                <div class="hasil-box">
                    💧 V₂ = {:.2f} mL
                </div>
                """.format(v2), unsafe_allow_html=True)
                simpan_riwayat("V2 -> M1=" + str(m1) + ", V1=" + str(v1) + ", M2=" + str(m2) + " => V2={:.2f}mL".format(v2))
                st.rerun()
    
    # --- Hitung V1 ---
    with subtab_v1:
        st.markdown("**🔍 Mencari: Volume Awal (V₁)**")
        with st.expander("📐 Rumus V₁"):
            st.markdown("""
            ```
            V₁ = (M₂ × V₂) ÷ M₁
            ```
            
            **Dari persamaan:** M₁ × V₁ = M₂ × V₂
            """)
        
        cols = st.columns([1, 1, 1])
        with cols[0]:
            m1_v1 = st.number_input("⚛️ M₁ (awal) [M]", min_value=0.0, key="m1_v1")
        with cols[1]:
            m2_v1 = st.number_input("📈 M₂ (akhir) [M]", min_value=0.0, key="m2_v1")
        with cols[2]:
            v2_v1 = st.number_input("🧪 V₂ (akhir) [mL]", min_value=0.0, key="v2_v1")
        
        if st.button("🧮 Hitung V₁", key="btn_v1", use_container_width=True):
            if m1_v1 <= 0 or m2_v1 <= 0 or v2_v1 <= 0:
                st.error("⚠️ Semua nilai harus lebih dari 0!")
            else:
                v1 = hitung_v1(m1_v1, m2_v1, v2_v1)
                st.markdown("""
                <div class="hasil-box">
                    🧪 V₁ = {:.2f} mL
                </div>
                """.format(v1), unsafe_allow_html=True)
                simpan_riwayat("V1 -> M1=" + str(m1_v1) + ", M2=" + str(m2_v1) + ", V2=" + str(v2_v1) + " => V1={:.2f}mL".format(v1))
                st.rerun()
    
    # --- Hit
