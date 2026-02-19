import streamlit as st
from factorial import fact

def main():
    st.title("tinh toan giai thua cua 1 so")
    number  = st.number_input("Nhap so can tinh",
                              min_value=1,
                              max_value=900)
    if st.button("Calculate"):
        result = fact(number)
        st.write(f"Ket qua duoc hien thi la", {result})

if __name__ == "__main__":
    main()