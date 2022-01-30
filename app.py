import streamlit as st
import pages.edu, pages.projets, pages.exp, pages.skills, pages.propos

import ressources.ast as ast

PAGES = {
    "Présentation": pages.propos,
    "Expérience": pages.exp,
    "Réalisations": pages.projets,
    "Compétences": pages.skills,
    "Formation" : pages.edu,
}

def main():
	st.sidebar.title("Navigation")
	selection = st.sidebar.radio("Allez à", list(PAGES.keys()))
	page = PAGES[selection]
	with st.spinner(f"Loading {selection} ..."):
		ast.write_page(page)
	st.sidebar.title("Contact")
	st.sidebar.info(
        """
        Si vous souhaitez me contacter via
        [email](mailto:l.libat2001@gmail.com) ou via
        [LinkedIn](https://www.linkedin.com/in/louislibat/)
	""")


if __name__ == "__main__":
    main()