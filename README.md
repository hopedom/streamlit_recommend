# 딥러닝 기반 추천시스템 구축 프로젝트
___

📌 개요

본 프로젝트는 영화 데이터셋 `MovieLens 1M`을 활용하여 AutoInt+ (AutoInt MLP Model) 딥러닝 추천 시스템을 구축하고, 하이퍼파라미터 튜닝을 통해 모델의 성능을 최적화하는 과정을 담고 있습니다.   
최종적으로 Streamlit을 사용하여 구현된 추천 시스템을 시각화하고 배포했습니다.

- [배포된 streamlit](https://apprecommend-nmhn3yf5gy86no8fued8kc.streamlit.app/)

## 🚀 모델 학습 결과 및 평가 Metric

### 1. 기본 모델 (최종 제출 모델)

*이 모델의 가중치가 Streamlit 배포에 활용되었습니다.*

| 지표 | 훈련/검증 결과 | 추천 지표 (@10) | 비고 |
|:---|:---|:---|:---|
| **Batch Size** | 2048 | 2048 | 안정적인 학습 조건 |
| **Loss (Val)** | 0.577 (0.592) | N/A | 이진 분류 성능 |
| **NDCG** | N/A | **0.654** | 추천 순위 정확도 |
| **Hit Rate** | N/A | **0.625** | 추천 성공률 |

### 2. 튜닝 시도 모델 (성능 하락)

| 지표 | 훈련/검증 결과 | 추천 지표 (@10) | 비고 |
|:---|:---|:---|:---|
| **Batch Size** | 32 (불안정 조건 하) | 32 | **성능 하락 원인** |
| **Val AUC** | 0.770 | N/A | 튜닝 목표 Metric (분류 성능) |
| **NDCG** | N/A | 0.558 | **약 9.6%p 하락** |

🚀 모델 학습 기록

1. `batch_size` = 2048
   - `binary_crossentropy`: 0.577 - `loss`: 0.577 - `val_binary_crossentropy`: 0.592 - `val_loss`: 0.592
   - `ndcg` :  0.654, `hitrate` :  0.625
2. `batch_size` = 32 튜닝 후 best_model 기록
   - `batch_size` 수정 후 `keras.tuner`를 활용하여 `임베딩 크기`, `Dropout 비율` 그리고 `학습률`에 대한 파라미터 튜닝을 수행
   - 튜닝 시 `metric`은 `AUC`를 활용하였고, 평가 지표인 `NDCG` 그리고 `hitrate`를 활용하여 비교 분석을 수행
   - 그 결과, 기존 모델의 성능 대비 약 9.6%p의 성능 하락을 보임
   - `val_AUC Score` = 0.770, `ndcg` :  0.558, `hitrate` :  0.572
<img width="562" height="848" alt="image" src="https://github.com/user-attachments/assets/516a365b-5875-4739-927d-3714e7dd7480" />
<img width="663" height="556" alt="image" src="https://github.com/user-attachments/assets/482e6c54-1cbc-4015-be5c-316c77236749" />

___
📂 저장소 구조

```text
streamlit_recommend (Repository Root)
│  autoint.py                         # AutoInt 모델 구현 코드
│  autointp.py                        # AutoInt+ 모델 구현 코드
│  model_training.ipynb               # AutoInt+ 모델 학습 및 튜닝 코드 
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

