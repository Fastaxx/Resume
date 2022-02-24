import streamlit as st
import pages.edu, pages.projets, pages.exp, pages.skills, pages.propos
from PIL import Image
import ressources.ast as ast
hide_menu = """ 
<style>
#MainMenu {
	visibility:hidden;
}

footer {
	visibility:hidden;
}@
</style>
"""
PAGES = {
    "🙋 Introduction": pages.propos,
    "👨‍💻️ Professional experience": pages.exp,
    "✅ Achievements": pages.projets,
    "Skills": pages.skills,
    "🎓 Education" : pages.edu,
}

PAGE_CONFIG = {"page_title" : "Resume Louis Libat",
"page_icon":"https://img.icons8.com/ios/50/000000/resume.png",
"layout":"centered",
"initial_sidebar_state":"expanded",
"menu_items":{
	'Get Help': None,
	'Report a bug':None,
	'About': "Test"
}}

st.set_page_config(**PAGE_CONFIG)


image = Image.open('img/louis.jpeg') 
def main():
	st.markdown(hide_menu,unsafe_allow_html=True)
	selection = st.sidebar.radio("Go to", list(PAGES.keys()))
	page = PAGES[selection]
	with st.spinner(f"Loading {selection} ..."):
		ast.write_page(page)
	st.sidebar.title("Contact")
	st.sidebar.info(
        """
       	If you want to contact me by
        [email](mailto:) or by
        [LinkedIn](https://www.linkedin.com/in/louislibat/)
	""")


if __name__ == "__main__":
    main()