import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
iris_df = pd.read_csv(url)

st.dataframe(iris_df)
st.write(iris_df)

st.markdown("*.*.*")

## Radio button
status = st.radio("Select status.", ("Active", "Inactive"))
if status == "Active":
 st.success("활성화 되었습니다.")
else:
 st.warning("비활성화 되었습니다.")
 
 ## Select Box
occupation = st.selectbox("직군을 선택하세요.", [
 "Backend Developer",
 "Frontend Developer",
 "ML Engineer",
 "Engineer",
 "Database Administrator",
 "Scientist",
 "Data Analyst",
 "Security Engineer"
])
st.write(" 직군은 ", occupation, " 입니다.")

## MultiSelect
location = st.multiselect("선호하는 유투브 채널을 선택하세요.",
 (
 "운동",
 "IT 기기",
 "브이로그",
 "먹방",
 "반려동물",
 "맛집 리뷰"
 )
)
st.write(len(location), "가지를 선택했습니다.")

## Slider
level = st.slider("레벨을 선택하세요.", 1, 5)

# Text Input
first_name = st.text_input("Enter Your First Name", "Type Here ...")
if st.button("Submit", key='first_name'):
 result = first_name.title()
 st.success(result)
# Text Area
message = st.text_area("메세지를 입력하세요.", "Type Here ...")
if st.button("Submit", key='message'):
 result = message.title()
 st.success(result)

## Date Input
import datetime
today = st.date_input("날짜를 선택하세요.", datetime.datetime.now())
the_time = st.time_input("시간을 입력하세요.", datetime.time())

## Display Raw Code — one line
st.subheader("Display one-line code")
st.code("import numpy as np")
# Display Raw Code — snippet
st.subheader("Display code snippet")
with st.echo():
 # 여기서부터 아래의 코드를 출력합니다.
 df = pd.DataFrame()
## Display JSON
st.subheader("Display JSON")
st.json({"name" : "민수", "gender": "male", "Age": 29})


## Plotting
st.subheader("Matplotlib 으로 차트 그리기")
fig, ax = plt.subplots()
ax = iris_df[iris_df['species']=='virginica']['petal_length'].hist()
st.pyplot(fig)

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
 bytes_data = uploaded_file.read()
 st.write("filename:", uploaded_file.name)
 st.write(bytes_data)