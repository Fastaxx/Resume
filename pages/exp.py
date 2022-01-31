import streamlit as st
from PIL import Image

elecmap = Image.open('img/elecmap.png') 
def write():
	st.title("Professional experience")
	col1, col2 =st.columns(2)
	with col1:
		st.markdown(
		""" ### [electricitymap](https://electricitymap.org/) Contributor

**Open-source electricity CO2 data**
- Power Grid Data, Carbon intensity estimation
- Real-time data, Live visualization
- Python, Heroku, SQL

###

### Civilian Service : Project Manager | 2021 
**Context**
- Project Management (Financing Plan, grants,...)
- Deployment of cycling infrastructures - Coordination of public, private and associative actors
- Website redesign and Hosting
- Bike Mechanics - Repair Workshop

###

### Burgundy heritage restoration project | 2019
**Rempart**
- Construction and restoration of heritage

""")
	with col2:
		st.subheader("")
		st.image(elecmap)
	

