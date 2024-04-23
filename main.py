import streamlit as st
import google.generativeai as genai

class GeminiAPIManager:
        def check_gemini_api_key(self, gemini_api_key: str) -> None:
                ''' 
                Function to check whether the API key was really exist in Google. 
                This function especially made for `gemini_api_input()` below
                '''
                if len(gemini_api_key) != 0:
                        try:
                                genai.configure(api_key=gemini_api_key)
                                model = genai.GenerativeModel('gemini-pro-vision')
                                response = model.generate_content("Hello")
                        except Exception as e:
                                st.warning(e)                        
        def gemini_api_input(self) -> None:
                ''' Function to input and manage Gemini-AI api key'''
                # Input API key for Gemini API
                input_gemini_api = st.text_input(
                        label='Gemini-AI API key',
                        placeholder='Input your own Gemini-AI API key',
                        type='password',
                        help='required to use this application'
                )
                st.markdown('''
                Or if you don't have one, get your own Gemini-AI API key here:  
                [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
                ''')
                api_key_valid = True
                try:
                        self.check_gemini_api_key(input_gemini_api)
                except Exception:
                        api_key_valid = False
                if api_key_valid and 'gemini_api_key' not in st.session_state:
                        st.session_state.gemini_api_key = input_gemini_api

def main():
        st.title('Text Generation using Gemini-AI')
        with st.container(border=True): GeminiAPIManager().gemini_api_input()
        input_text = st.text_area('Input text you want answer')
        if len(input_text) > 0:
                genai.configure(api_key=st.session_state.gemini_api_key)
                # gemini_version = 'models/gemini-1.5-pro-latest'
                gemini_version = 'models/gemini-pro'
                model = genai.GenerativeModel(gemini_version)
                response = model.generate_content(input_text)
                st.markdown(response.text)

main()
        
