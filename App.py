import streamlit as st

# Configuration de la page
st.set_page_config(page_title="PromptMaster Pro", page_icon="🚀")

# Titre et interface
st.title("🚀 PromptMaster : Créez des contenus viraux")
st.subheader("Générez des instructions parfaites pour ChatGPT en 3 clics.")

# Formulaire utilisateur
topic = st.text_input("Quel est le sujet de votre contenu ?", placeholder="Ex: Les bienfaits du sport...")
platform = st.selectbox("Pour quelle plateforme ?", ["Instagram (Post)", "TikTok (Script)", "LinkedIn"])
tone = st.select_slider("Quel ton ?", options=["Humoristique", "Inspirant", "Professionnel"])

# Logique de génération
if st.button("Générer mon Prompt 🔥"):
    if topic:
        final_prompt = f"Agis en tant qu'expert {platform}. Sujet: {topic}. Ton: {tone}. Rédige un contenu viral avec une accroche forte."
        st.success("Copiez ce prompt dans ChatGPT :")
        st.code(final_prompt, language="markdown")
    else:
        st.error("Entrez un sujet !")

# --- SECTION PAIEMENT (BARRE LATERALE) ---
st.sidebar.markdown("---")
st.sidebar.write("☕ **Soutenir le projet**")
st.sidebar.markdown(f'''
<a href="https://www.buymeacoffee.com/prolyesboug" target="_blank">
    <button style="background-color: #FFDD00; color: black; font-weight: bold; border-radius: 5px; width: 100%; height: 45px; border: none; cursor: pointer;">
        ☕ Offrir un café (5€)
    </button>
</a>
''', unsafe_allow_html=True)
