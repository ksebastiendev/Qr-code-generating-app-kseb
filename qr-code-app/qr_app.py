import streamlit as st
import qrcode
from PIL import Image

st.title("Générateur de QR Code Simple")
st.write("Entrez un texte ou un lien pour générer un QR Code personnalisé.")

# Input utilisateur
data = st.text_input("Entrez votre texte ou lien ici", "https://clcoding.com")

# Choix des couleurs
col1, col2 = st.columns(2)
with col1:
    fill_color = st.color_picker("Couleur du QR Code", "#000000")
with col2:
    back_color = st.color_picker("Couleur de fond", "#FFFF00")

if st.button("Générer le QR Code"):
    qr = qrcode.QRCode(
        version=3,
        box_size=8,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
img = img.convert("RGB")  # 🔧 Correction obligatoire

st.image(img, caption="Votre QR Code")

    # Télécharger le QR Code
    img.save("qr_code.png")
    with open("qr_code.png", "rb") as file:
        st.download_button(
            label="Télécharger l'image",
            data=file,
            file_name="qr_code.png",
            mime="image/png"
        )

