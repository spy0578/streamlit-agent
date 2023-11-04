import streamlit as st
import speech_recognition as sr

# 创建“录音”按钮
if st.button("录音"):
    # 创建识别器对象
    r = sr.Recognizer()
    # 打开系统默认的麦克风
    with sr.Microphone() as source:
        # 提示用户进行讲话
        st.write("请开始说话...")
        # 使用recorognizer对象记录用户的讲话并进行语音识别
        audio = r.listen(source)
        try:
            # 将用户的讲话翻译成文本并输出
            text = r.recognize_google(audio, language='en-US')
            st.write("你刚刚说道：", text)
        except:
            st.write("语音识别失败，请重试")
