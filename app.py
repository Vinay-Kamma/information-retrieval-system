import streamlit as st

import time


def main():
    st.set_page_config("Information Retrieval")
    st.header("Information Retrival System")
    
    
    
    with st.sidebar:
        st.title('menu')
        pdf_docs=st.file_uploader("upload your PDF files and click the submit & process Button",accept_multiple_files=True)
        if st.button('Submit & Process'):
            with st.spinner('processing....'):



                st.success('Done')
if __name__=='__main__':
    main()
