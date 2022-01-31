import streamlit as st
import pages.edu, pages.projets, pages.exp, pages.skills, pages.propos
from PIL import Image
import ressources.ast as ast

PAGES = {
    "Introduction": pages.propos,
    "Professional experience": pages.exp,
    "Achievements": pages.projets,
    "Skills": pages.skills,
    "Education" : pages.edu,
}

image = Image.open('img/louis.jpeg') 
def main():
	st.sidebar.title("Navigation")
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