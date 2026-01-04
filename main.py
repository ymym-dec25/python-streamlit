import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ1回答')
expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ2回答')

#text = st.text_input('あなたの趣味を教えて')
#condition = st.slider('あなたの今の調子は？', 0, 100, 50)


#'あなたの趣味：', text, 'です!'
#'コンディション：', condition

#if st.checkbox('Show Image'):
#    img = Image.open('Flower.jpg')
#    st.image(img, caption='お花', use_container_width=True)

