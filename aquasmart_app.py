import streamlit as st

# Data rekomendasi parameter lingkungan air untuk tiap jenis ikan
rekomendasi = {
    "Ikan Nila": {
        "pH": (6.5, 8.5),
        "Oksigen Terlarut": (5, 7),
        "Suhu Air": (25, 30),
        "Kedalaman Air": (60, 100)
    },
    "Ikan Lele": {
        "pH": (6.5, 8),
        "Oksigen Terlarut": (3, 6),
        "Suhu Air": (26, 30),
        "Kedalaman Air": (40, 80)
    },
    "Ikan Gurame": {
        "pH": (6.5, 8.5),
        "Oksigen Terlarut": (4, 6),
        "Suhu Air": (27, 30),
        "Kedalaman Air": (60, 150)
    },
    "Ikan Mas": {
        "pH": (6.5, 8),
        "Oksigen Terlarut": (5, 8),
        "Suhu Air": (20, 28),
        "Kedalaman Air": (60, 100)
    },
    "Ikan Mujair": {
        "pH": (6.5, 9),
        "Oksigen Terlarut": (5, 7),
        "Suhu Air": (25, 30),
        "Kedalaman Air": (50, 100)
    },
    "Ikan Patin": {
        "pH": (6, 8),
        "Oksigen Terlarut": (4.5, 6.5),
        "Suhu Air": (26, 30),
        "Kedalaman Air": (100, 150)
    },
    "Ikan Koi": {
        "pH": (6.5, 8),
        "Oksigen Terlarut": (6, 8),
        "Suhu Air": (20, 28),
        "Kedalaman Air": (80, 150)
    },
    "Ikan Gabus": {
        "pH": (6, 7.5),
        "Oksigen Terlarut": (4.2, 5.6),
        "Suhu Air": (25, 30),
        "Kedalaman Air": (50, 100)
    },
    "Ikan Arwana": {
        "pH": (6, 7),
        "Oksigen Terlarut": (5, 7),
        "Suhu Air": (26, 30),
        "Kedalaman Air": (100, 200)
    },
    "Ikan Cupang": {
        "pH": (6.2, 7),
        "Oksigen Terlarut": (3, 5),
        "Suhu Air": (24, 30),
        "Kedalaman Air": (20, 40)
    }
}

# Konversi range ke string friendly
def format_range(r):
    return f"{r[0]} - {r[1]}"

# Setup tampilan
st.set_page_config(page_title="AQUASmart", layout="centered")
st.title("🐟 AQUASmart")
st.markdown("**Sistem Rekomendasi Parameter Lingkungan dan Jenis Ikan**")
st.divider()

# Tabs
tab1, tab2 = st.tabs(["📋 Pilih Jenis Ikan", "🧪 Masukkan Parameter Air"])

# ================== TAB 1 =====================
with tab1:
    st.subheader("Rekomendasi Berdasarkan Jenis Ikan")
    jenis_ikan = st.selectbox("Pilih Jenis Ikan", list(rekomendasi.keys()))

    if jenis_ikan:
        st.markdown("### Rekomendasi Parameter:")
        for param, nilai in rekomendasi[jenis_ikan].items():
            st.write(f"- **{param}**: {format_range(nilai)}")

# ================== TAB 2 =====================
with tab2:
    st.subheader("Rekomendasi Ikan Berdasarkan Kondisi Air")

    ph = st.number_input("Masukkan pH Air", min_value=0.0, max_value=14.0, step=0.1)
    oksigen = st.number_input("Masukkan Oksigen Terlarut (mg/L)", min_value=0.0, max_value=20.0, step=0.1)
    suhu = st.number_input("Masukkan Suhu Air (°C)", min_value=0.0, max_value=40.0, step=0.1)
    kedalaman = st.number_input("Masukkan Kedalaman Air (cm)", min_value=0.0, max_value=300.0, step=1.0)

    if st.button("Cari Rekomendasi Ikan"):
        cocok = []
        for ikan, param in rekomendasi.items():
            if (
                param["pH"][0] <= ph <= param["pH"][1] and
                param["Oksigen Terlarut"][0] <= oksigen <= param["Oksigen Terlarut"][1] and
                param["Suhu Air"][0] <= suhu <= param["Suhu Air"][1] and
                param["Kedalaman Air"][0] <= kedalaman <= param["Kedalaman Air"][1]
            ):
                cocok.append(ikan)

        if cocok:
            st.success("✅ Jenis Ikan yang Cocok:")
            for ikan in cocok:
                st.write(f"- {ikan}")
        else:
            st.warning("⚠️ Tidak ada jenis ikan yang cocok dengan parameter yang dimasukkan.")

# Footer
st.markdown("---")
st.markdown("<center>© 2025 AQUASmart</center>", unsafe_allow_html=True)
