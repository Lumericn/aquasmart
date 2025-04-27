import streamlit as st
import json

# Fungsi untuk memuat data dari JSON

def load_rules():
    try:
        with open("rules.json", "r") as f:
            rules = json.load(f)
        return rules
    except Exception as e:
        st.error(f"Gagal memuat data: {e}")
        return []

# Fungsi format rentang

def format_range(min_val, max_val):
    return f"{min_val} - {max_val}"

# Fungsi utama Streamlit

def main():
    st.set_page_config(page_title="AQUASmart", layout="centered")
    st.title("🐟 AQUASmart - Sistem Pakar Rekomendasi Ikan Budidaya")
    st.markdown("Sistem pakar untuk membantu memilih jenis ikan yang sesuai berdasarkan kondisi lingkungan, atau menampilkan kebutuhan lingkungan berdasarkan jenis ikan.")

    rules = load_rules()
    if not rules:
        return

    tab1, tab2 = st.tabs(["🔎 Masukkan Parameter Air", "🔁 Pilih Jenis Ikan"])

    # --- Forward Chaining ---
    with tab1:
        st.subheader("🔎 Rekomendasi Ikan")

        ph = st.number_input("Masukkan pH", min_value=0.0, step=0.1)
        oksigen = st.number_input("Masukkan Oksigen Terlarut (mg/L)", min_value=0.0, step=0.1)
        suhu = st.number_input("Masukkan Suhu Air (°C)", min_value=0.0, step=0.1)
        kedalaman = st.number_input("Masukkan Kedalaman Air (cm)", min_value=0.0, step=1.0)

        if st.button("Cek Rekomendasi"):
            cocok = []
            for rule in rules:
                cond = rule["IF"]
                if (
                    cond["pH"][0] <= ph <= cond["pH"][1] and
                    cond["Oksigen"][0] <= oksigen <= cond["Oksigen"][1] and
                    cond["Suhu"][0] <= suhu <= cond["Suhu"][1] and
                    cond["Kedalaman"][0] <= kedalaman <= cond["Kedalaman"][1]
                ):
                    cocok.append(rule["THEN"])

            st.markdown("### 🌟 Hasil Rekomendasi")
            if cocok:
                for ikan in cocok:
                    st.write(f"- {ikan}")
            else:
                st.warning("Tidak ada jenis ikan yang cocok dengan parameter yang dimasukkan.")

    # --- Backward Chaining ---
    with tab2:
        st.subheader("🔁 Parameter dari Jenis Ikan")

        ikan_list = list(set(rule["THEN"] for rule in rules))
        selected_fish = st.selectbox("Pilih jenis ikan:", ikan_list)

        if selected_fish:
            rule = next((r for r in rules if r["THEN"] == selected_fish), None)
            if rule:
                cond = rule["IF"]
                st.markdown(f"### 📋 Rekomendasi Parameter untuk **{selected_fish}**")
                st.write(f"- **pH:** {format_range(cond['pH'][0], cond['pH'][1])}")
                st.write(f"- **Oksigen Terlarut:** {format_range(cond['Oksigen'][0], cond['Oksigen'][1])} mg/L")
                st.write(f"- **Suhu Air:** {format_range(cond['Suhu'][0], cond['Suhu'][1])} °C")
                st.write(f"- **Kedalaman Air:** {format_range(cond['Kedalaman'][0], cond['Kedalaman'][1])} cm")

if __name__ == "__main__":
    main()

# Footer
st.markdown("---")
st.markdown("<center>© 2025 AQUASmart</center>", unsafe_allow_html=True)