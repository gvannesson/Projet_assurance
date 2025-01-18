import streamlit as st

# Fonction pour afficher une image en tant que bouton
def clickable_image(image_path, button_key):
    clicked = st.button("", key=button_key)
    st.image(image_path)
    return clicked

# Exemple d'utilisation
image_path = "path/to/your/image.png"

# Afficher l'image comme un bouton
if clickable_image(image_path, button_key="button1"):
    st.write("Le bouton a été cliqué!")

# Utilisez des images supplémentaires avec des clés différentes si nécessaire
