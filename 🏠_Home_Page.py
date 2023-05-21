import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="🏠",
)

st.write("# DIPR430685_22_2_10! 🏠")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Họ và tên: Nguyễn Phạm Ngọc Duy \n
    MSSV: 20133031 \n
    Đây là Project cho môn học DIPR430685_22_2_10 📸. Project được xây dựng bằng Python trên Streamlit.
    ### My Include
    - Phát hiện khuông mặt 🕵️‍♀️
    - Nhận diện khuông mặt 🙎‍♂️
    - Xử lý ảnh số 🖥
    ### Contact
    - Email: (kazr1582@gmail.com)
    - Github: (https://github.com/crytalwing/DIPR430685_22_2_10)
"""
)
