import streamlit as st

# Configuration de la page
st.set_page_config(page_title="PromptMaster Pro", page_icon="🚀")

st.title("🚀 PromptMaster : Créez des contenus viraux")
st.subheader("Générez des instructions parfaites pour ChatGPT en 3 clics.")

# Formulaire utilisateur
with st.container():
    topic = st.text_input("Quel est le sujet de votre contenu ?", placeholder="Ex: Les bienfaits du café, Investir en bourse...")
    platform = st.selectbox("Pour quelle plateforme ?", ["Instagram (Post)", "TikTok (Script)", "LinkedIn (Article)", "YouTube (Description)"])
    tone = st.select_slider("Quel ton souhaitez-vous ?", options=["Humoristique", "Inspirant", "Professionnel", "Provocateur"])

# Logique de génération de prompt
if st.button("Générer mon Prompt 🔥"):
    if topic:
        final_prompt = f"""
        AGIS EN TANT QU'EXPERT EN CRÉATION DE CONTENU SUR {platform.upper()}.
        TA MISSION : Rédiger un contenu captivant sur le sujet suivant : '{topic}'.
        TON : {tone}.
        STRUCTURE : Commence par une accroche (Hook) forte, développe 3 points clés, et termine par un appel à l'action (CTA) engageant.
        FORMAT : Utilise des émojis et des retours à la ligne pour la lisibilité.
        """
        
        st.success("Voici votre prompt à copier-coller dans ChatGPT :")
        st.code(final_prompt, language="markdown")
        st.info("💡 Conseil : Ajoutez ce site à vos favoris pour gagner du temps !")
    else:
        st.error("Veuillez entrer un sujet pour continuer.")

# Section Monétisation (Lien de don ou Affiliation gratuite)
st.sidebar.markdown("---")
st.sidebar.write("☕ **Soutenir le projet**")
st.sidebar.write("Si cet outil vous aide, vous pouvez m'offrir un café !")
# Ici vous mettrez votre lien PayPal.me ou Revolut (gratuit à créer)
st.sidebar.button("Faire un don (Lien fictif)")
