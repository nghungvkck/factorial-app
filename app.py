import streamlit as st
from factorial import fact
import os

def load_user():
    # Đọc danh sách user từ file user.txt
    try:
        if os.path.exists("user.txt"):
            with open("user.txt", "r", encoding="utf-8") as f:
                users = [line.strip() for line in f.readlines() if line.strip()]
            return users
        else:
            st.error("File user.txt không tồn tại!")
            return []

    except Exception as e:
        st.error(f"Lỗi khi đọc file user.txt: {e}")
        return []

def login_page():
    """Trang dang nhap"""
    st.title("Dang nhap")

    "Input username"
    username = st.text_input("Nhap ten nguoi dung")
    if st.button("Dang nhap"):
        if username:
            users = load_user()
            if username in users:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                "Neu user ko hop le, hien thi trang chao hoi"
                st.session_state.show_greeting = True
                st.session_state.logged_in = username
                st.rerun()
        else:
            st.warning("VUi long dang nhap ten nguoi dung ")

def facctorial_calculation():
    st.title("Facctorial Calculation")

    st.write(f"XIn chao, {st.session_state.username}")

    "Nut dang xuat"
    if st.button("Nut dang xuat"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    st.divider()

    # Chuc nang tinh giai thua
    number = st.number_input("Nhap vao 1 so: ",
                             min_value=1,
                             max_value=800)
    if st.button("Tinh gian thua"):
        result = fact(number)
        st.write(f"giai thua cua  {number} la {result}")

def greeting_pape():
    st.title("Xin chao")
    st.write(f"XIn chao {st.session_state.username}")
    st.write(f"Ban ko co quyen truy cap chuc nang tinh giai thua")

    if st.button("QUay lai dang nhap"):
        st.session_state.show_greeting = False
        st.session_state.username = ""
        st.rerun()

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = ""
    if 'show_greeting' not in st.session_state:
        st.session_state.show_greeting = False

    if st.session_state.logged_in:
        facctorial_calculation()
    elif st.session_state.show_greeting:
        greeting_pape()
    else:
        login_page()

if __name__ == '__main__':
    main()