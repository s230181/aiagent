# 분류 모델 웹앱 만들기

import streamlit as st

# 1.기계학습 모델 파일 로드
import joblib
model = joblib.load('이용시간에따른감정변화')

# 2.모델 설명
st.title('소셜미디어 사용 시간과 정서적 웰빙')
col1, col2,col3 = st.columns( 3 )      # 몇 개의 컬럼으로 나눌까?
with col1:
      st.subheader('모델 설명 ')
      st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
      st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
      st.write(' - 훈련    데이터 : 1000건')
      st.write(' - 테스트 데이터 : 103건')
      st.write(' - 모델 정확도 : 0.4')
      st.write(' - SNS 이용시간에 따른 청소년의 우울 및 충동성 차이에 관한 논문에 따르면 청소년의 우울 및 충동성 수준은 SNS 이용 시간 하위집단보다 SNS 이용 시간 상위집단에서 더 높게 나왔다.')
# 3.데이터시각화
with col2:
      st.subheader('데이터시각화1')
      st.image('나이에따른감정.png' )   # 이미지 불러오기
with col3:
      st.subheader('데이터시각화2')
      st.image('사용시간에따른감정1.png')    # 이미지 불러오기

# 4. 모델 활용
st.subheader('모델 활용')
st.write('**** 소셜미디어 하루 사용 시간이 얼마나 되나요? 인공지능이 당신의 기분을 예측해드립니다!!')

a = st.number_input(' 나이를 입력하세요. ', value=0)
b = st.number_input(' 소셜미디어 하루 사용 시간을 입력하세요. ', value=0)   # 사용자 입력

if st.button('나의 감정 확인하기'):              # 사용자가 '합불분류' 버튼을 누르면
        input_data = [[ a,b ]]          # 사용자가 입력한 a,b,c 를 input_data에 저장하고
        p = model.LogisticRegression(input_data)      # model이 분류한 값을 p에 저장한다
        if p[0] == 1 :
              st.success('인공지능 분류 결과는 Anger입니다')
        elif p[0] == 2:
            st.success('인공지능 분류 결과는 Sadness입니다')
        elif p[0] == 3:
            st.success('인공지능 분류 결과는 Anxiety입니다')
        elif p[0] == 4:
            st.success('인공지능 분류 결과는 Neutral입니다')
        elif p[0] == 5:
            st.success('인공지능 분류 결과는 Boredom입니다')
        else:
              st.success('인공지능 분류 결과를 Happiness입니다')


              
