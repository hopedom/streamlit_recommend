# 딥러닝 기반 추천시스템 구축 프로젝트
___


- [배포된 streamlit](https://apprecommend-nmhn3yf5gy86no8fued8kc.streamlit.app/)

- 저장소 구조

streamlit_recommend (Repository Root)
│  autoint.py                         # AutoInt 모델 구현 코드
│  autointp.py                        # AutoInt+ 모델 구현 코드 (streamlit 배포 버전)
│  show_st.py                         # Streamlit 메인 실행 파일 (AutoInt 모델)
│  show_st+.py                        # Streamlit 메인 실행 파일 (AutoInt+ 모델)
│  requirements.txt                   # 필수 패키지 목록 (최종 간소화된 버전)
│  README.md                          # 저장소 설명 파일
│
├─data
│  │  field_dims.npy                  # 모델 입력 차원 정보
│  │  autoIntMLP_label_encoders.pkl   # 인코더 객체 (AutoInt+ 모델)
│  │  label_encoders.pkl              # 인코더 객체 (AutoInt 모델)
│  │
│  └─ml-1m
│        ratings_prepro.csv           # 사용자/영화 평점 데이터
│        movies_prepro.csv            # 영화 정보 데이터
│        users_prepro.csv             # 사용자 정보 데이터
│
└─model
      autoInt_model_weights.weights.h5 # 가중치 저장 파일 (AutoInt 모델)
      autoIntMLP+_model_weights.h5     # 가중치 저장 파일 (AutoInt+ 모델)
