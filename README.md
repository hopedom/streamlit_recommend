# 딥러닝 기반 추천시스템 구축 프로젝트
___


- [배포된 streamlit](https://apprecommend-nmhn3yf5gy86no8fued8kc.streamlit.app/)

- 저장소 구조

```text
streamlit_recommend (Repository Root)
│  autoint.py                         # AutoInt 모델 구현 코드
│  autointp.py                        # AutoInt+ 모델 구현 코드 
│  show_st.py                         # Streamlit 메인 실행 파일 (AutoInt 모델)
│  show_st+.py                        # Streamlit 메인 실행 파일 (AutoInt+ 모델) *streamlit 배포 버전
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
```

- 학습기록
1. batch_size = 2048
   - binary_crossentropy: 0.5770 - loss: 0.5770 - val_binary_crossentropy: 0.5921 - val_loss: 0.5921
   - mymodel ndcg :  0.65402, mymodel hitrate :  0.62511
2. batch_size = 32 튜닝 후 best_model 기록
   - val_AUC Score = 0.770468, mymodel ndcg :  0.55787, mymodel hitrate :  0.572
<img width="562" height="848" alt="image" src="https://github.com/user-attachments/assets/516a365b-5875-4739-927d-3714e7dd7480" />
<img width="663" height="556" alt="image" src="https://github.com/user-attachments/assets/482e6c54-1cbc-4015-be5c-316c77236749" />

