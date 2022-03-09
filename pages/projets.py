import streamlit as st
import streamlit.components.v1 as components

def write():
	st.title("Projects")
	st.markdown(
		""" ### Study and sizing of a building heating system attached to a hydroelectric power station | 2022

**Elements**
- Hydroelectric plant renovation study
- DHW and heating sizing: Energy recovery, solar thermal
****
### HVAC study and sizing of a wine cellar | 2021 
**Elements**
- ASHRAE method
- Aeraulics and fluid mechanics

****
### Modeling and numerical simulation of an airborne energy generator (Kite) | 2021
**End of studies' project**
- Dynamic Numerical Simulation
- Python Programming
- Experimental build
""")
	col1, col2 = st.columns(2)
	with col1:
		st.subheader("Slide")
		components.iframe("https://drive.google.com/file/d/15C56Hgy9gis-2bkC-Ap2k9SFn0jURLpQ/preview", width=None, height=260)

	with col2:
		st.subheader("Report")
		components.iframe("https://drive.google.com/file/d/1__zu_nTjj3RF18cdGnkVR2cEHf3gS1_1/preview", width=None, height=260)
