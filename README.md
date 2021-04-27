# Fraud-Detection
온라인 쇼핑몰에서 발생할 수 있는 결제 사기 및 오작동을 막는 FDS 시스템에 대해 연구하는 자료 입니다. 

### 참고자료
```
1. 캐글 데이터 : https://www.kaggle.com/mlg-ulb/creditcardfraud
2. FDS with ML : https://www.researchgate.net/project/Fraud-detection-with-machine-learning
```

### FDS란?
```
금융기업에서 다양한 금융사기에 대한 사전/사후대응을 지원하는 이상거래 탐지 시스템 - Fraud Detection System

이러한 FDS는 정보수집, 이상거래 분석, 대응으로 구성된다. 
1. 로그 수집 시스템 : 실시간 거래정보를 수집하고 대용량 데이터를 정제하여 이상거래 분석 시스템
2. 이상거래 분석 시스템 : 로그 수집에서 전달받은 데이터와 고객정보, 외부정보를 종합적으로 판단하여 거래이상 여부를 판단
3. 대응 시스템 : 이상거래 분석 시스템이 이상거래라고 판단한 거래에 대해 유형별 대응 시나리오에 따라 사용자 접속차단, 담당자에게 확인 알람 등의 자동화된 시스템 조치를 수행
- 인공지능 탐지 모델은 새로이 발견된 거래 패턴에 대한 내용을 학습하여 성능을 개선하고 이를 이상거래 분석 시스템에 수시로 반영함
```
<img src="https://www.2e.co.kr/news/photo/202012/301050_3752_120.jpg" />

### FDS 분석 방법
```
1. 오용탐지 기법 : 기존 이상거래 또는 사기거래에서 나타나는 주요 특징들을 조건화, 규칙화 하여 새로히 발생하는 금융거래에 다중 조건을 적용하여 필터링하는 방식으로 이상거래 여부를 식별 ex) 특정 고객이 거래하던 월 평균 금액보다 100배 이상 큰 금액이 새벽에 이체가 되고 구매가 속한 경우
2. 이상탐지 기법 : RDBMS에 저장된 고객 기번 정보, 거래 정보 등의 속성 정보를 바탕하여 모델링하여 특이점을 탐지하는 것이다. 또한, 고객이 가지고 있는 정적 변수(Static Variable)와 거래 정보에 따라 변화하는 동적 변수(Dynamic Variable)를 기본적으로 활용하여 분석함. ex) 손해보험사에서는 자동차 고의 사고 보험사기 사례에서 보험금 청구 고객의 고객기본정보(나이, 성별, 면허취득일), 상품정보(상품명, 가입특약, 가입일), 보험금 청구 거래정보(치료병원, 사고장소, 사고일, 청구일, 입원일수, 청구금 등), 외부기관 정보(통신사 정보, 신용평가기관, 의료보험 정보 등)를 종합적으로 분석하여 청구 거래 건이 사기일 가능성을 분석하여 경고를 줌.
```
