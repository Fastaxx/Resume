import streamlit as st
from PIL import Image


image = Image.open('img/louis.jpeg') 

def write():
	st.title("Introduction")
	st.markdown("""
		### Who am I ?
Engineering student in the thermal and energy field,
passionate about the world of Data Science and current environmental issues.
I am motivated, autonomous and curious.

**Louis Libat**\n
**Energy Engineering | Project Management | Data Science**\n
[**LinkedIn**](https://www.linkedin.com/in/louislibat/) | [**Email**](mailto:)

		""")