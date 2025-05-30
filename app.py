import streamlit as st
import google.generativeai as genai

# Gemini API 설정
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# 페이지 설정
st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon="🤖",
    layout="centered"
)

# 제목과 설명
st.title("🤖 Gemini Chatbot")
st.markdown("Powered by Gemini 1.5 Flash & Streamlit")

# 구분선
st.divider()

# 세션 상태 초기화
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 채팅 기록 표시
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 사용자 입력
user_input = st.chat_input("메시지를 입력하세요...")

if user_input:
    # 사용자 메시지 표시
    with st.chat_message("user"):
        st.write(user_input)
    
    # 사용자 메시지 저장
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    try:
        # Gemini 모델에 메시지 전송
        response = model.generate_content(user_input)
        
        # 모델 응답 표시
        with st.chat_message("assistant"):
            st.write(response.text)
        
        # 모델 응답 저장
        st.session_state.chat_history.append({"role": "assistant", "content": response.text})
        
    except Exception as e:
        st.error(f"오류가 발생했습니다: {str(e)}")
