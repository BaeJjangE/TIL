# 라이브러리 import 명령어
### 데이터 셋 분리
```python
from sklearn.model_selection import train_test_split
```

---

## 등분산 검정

### 등분산검정(F-test): 모분산

```python
# 두 집단, 정규분포를 따를 때
from scipy.stats import f 
# 두 집단 이상, 정규분포를 따를 때
from scipy.stats import bartlett
# 두 집단 이상, 정규분포를 따르지 않을 때
from scipy.stats import levene 
```

---

## 범주형 -> 연속형

### t-test 검정: 모평균

```python
# 단일표본 t-검정
from scipy.stats import ttest_1samp 
# 대응표본 t-검정
from scipy.stats import ttest_rel
# 독립2표본 t-검정
from scipy.stats import ttest_ind
```

### onewayANOVA: 모평균
```python
# 일원분산분석
from scipy.stats import f_oneway
# ols 모델 생성
from statsmodels.formula.api import ols
# 모델을 넣어 일원분산분석표를 보여줌
from statsmodels.stats.anova import anova_lm
# 귀무가설 기각 시 사후검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
```

### twowayANOVA 

### - onewayANOVA랑 같고 ols에 쓰는 방식만 다름: 모평균

```python
# formula = "종속변수 ~ 독변1 + 독변2 + 독변1:독변2"
from statsmodels.formula.api import ols 
from statsmodels.stats.anova import anova_lm
```

---

## 범주형 -> 범주형

### 카이제곱검정: 범주형, 범주형 -> 독립성검정

```python
# crosstab과 같이 사용
from scipy.stats import chi2_contingency
```

---

## 군집 분석(비지도 학습)

### 계층적 군집 분석

```python
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
# 덴드로그램 그리기위함
from matplotlib import pyplot as plt 
```

### 비계층적 군집 분석
```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
```

---

## 회귀분석(지도학습, 연속형 -> 연속형)

### 단순선형회귀 분석

```python
from statsmodels.formula.api import ols
from sklearn.linear_model import LinearRegression
```

### 다중선형회귀 분석
```python
from statsmodels.formula.api import ols
```
### 다중공선성 검사

```python
from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor as vif # VIF가 10이넘으면 다중공선성 문제가있음
```


### 회귀 검정 :  MAE, MSE, RMSE(MSE**0.5)

```python
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
```

---

## 분류

### 로지스틱회귀분석(지도학습, 연속형 -> 범주형)
```python
from statsmodels.api import Logit
from sklearn.linear_model import LogisticRegression
```

### 분류용 검정

```python
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score # 이진분류만 가능
from sklearn.metrics import recall_score # 이진분류만 가능
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
```

### 분류: 나이브베이즈

```python
from sklearn.naive_bayes import GaussianNB
```

---

### KNN

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
```

---

## 시계열분석

```python
# rolling(), ewm()
import pandas as pd 
# 시계열 분해
from statsmodels.tsa.seasonal import seasonal_decompose
```

---

## 상관분석(연속형 -> 연속형)

```python
import pandas as pd # corr()
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import kendalltau
```

---

## 의사결정나무모델

```python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
```

---

## 추천: 연관성 분석

```python
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
```

---

## 주성분 분석(PCA)

```python
import pandas as pd # cumsum() <- 누적분산
from sklearn.decomposition import PCA
```

---

## 회귀 한번에 다불러오기

```python
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.preprocessing import (OneHotEncoder, LabelEncoder, StandardScaler, 
                                   MinMaxScaler, PowerTransformer, QuantileTransformer)
from sklearn.model_selection import KFold, StratifiedKFold, train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
%matplotlib inline
```

