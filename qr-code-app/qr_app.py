import streamlit as st
import qrcode
from PIL import Image

# Configuration de la page
st.set_page_config(
    page_title="QR Code Generator",
    page_icon="🔗",
    layout="centered"
)

# Style personnalisé pour le bouton
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 0.75em 1.5em;
        border-radius: 8px;
        font-size: 1em;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Logo principal
st.image("qr-code-app/mon_logo1.png", width=120)

# Image illustrative du scan
st.image("qr-code-app/scan_illustration.jpg", use_container_width=True)

# Titre principal
st.title("🔗 Générateur de QR Code Simple")
st.write("Créez vos QR codes en quelques clics avec vos couleurs préférées !")

# Centrage du formulaire avec des colonnes
col_center = st.columns([1,2,1])[1]

with col_center:
    data = st.text_input("Entrez votre texte ou lien ici", placeholder="Ex : hello young dev group")

    fill_color = st.color_picker("Couleur du QR Code", "#000000")
    back_color = st.color_picker("Couleur de fond", "#FFFFFF")

    if st.button("Générer le QR Code"):

        with st.spinner("Génération du QR Code..."):

            qr = qrcode.QRCode(
                version=3,
                box_size=8,
                border=4
            )
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill_color=fill_color, back_color=back_color)
            img = img.convert("RGB")

            st.image(img, caption="Voici votre QR Code", use_container_width=True)

            img.save("qr_code.png")
            with open("qr_code.png", "rb") as file:
                st.download_button(
                    label="📥 Télécharger le QR Code",
                    data=file,
                    file_name="qr_code.png",
                    mime="image/png"
                )

# Footer discret
st.markdown("<hr style='margin-top: 40px; margin-bottom: 10px;'>", unsafe_allow_html=True)
st.caption("Made with ❤️ by ksebastiendev")
