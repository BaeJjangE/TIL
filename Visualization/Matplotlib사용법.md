# Matplotlib

```bash
# import
import matplotlib as mpl
import matplotlib.pyplot as plt

# 스타일 지정
plt.style.use(['seaborn-notebook'])
```



## 라인 플롯

* 플롯(plot)은 그림(figure)와 축(axes)으로 구성

- `plt.Figure`: 축과 그래픽, 텍스트, 레이블을 표시하는 모든 객체를 포함하는 컨테이너

- `plt.Axes`: 눈금과 레이블이 있는 테두리 박스로 시각화를 형성하는 플롯 요소 포함

```python
fig = plt.figure()
ax = plt.axes()
```

```bash
# 예시
x = np.arange(0, 10, 0.01)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x)); # 기본 색 자동 배정
```

### 라인 스타일(Line Style)

```bash
# 'solid' = '-'
# 'dashed' = '--'
# 'dashdot' = '-.'
# 'dotted' = ':'

# 예시
plt.plot(np.random.randn(50), linestyle='solid')
plt.plot(np.random.randn(50), linestyle='--')
plt.plot(np.random.randn(50), linestyle='-.')
plt.plot(np.random.randn(50), linestyle=':');
```





