import streamlit as st
import time

st.title('streamlit超入門')
st.write('プログレスバーの表示')
'start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('→カラム')

expander1 = st.expander('問い合わせ内容1')
expander1.write('問い合わせ内容を各')
expander2 = st.expander('問い合わせ内容1')
expander2.write('問い合わせ内容を各')
expander3 = st.expander('問い合わせ内容1')
expander3.write('問い合わせ内容を各')


# option = st.text_input('あなたの趣味入力')
# condition = st.slider('あなたの今の調子は？',0,100,50)
# 'あなたの趣味は',option,'です'

# if condition <=50:
#     x = '不調'
# else:
#     x = '好調'

# 'コンディション',x

# if st.checkbox('show Image'):
#     img = Image.open("C:/Users/tatsuya.ishikawa/OneDrive - AGC/Resized/A96炉ｻｰﾓﾋﾞｭﾜｰ開口部.jpg")
#     st.image(img, caption = 'kohei', use_column_width=True)
# #テキストを追加
