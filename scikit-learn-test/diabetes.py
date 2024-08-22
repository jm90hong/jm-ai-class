import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. 데이터 생성
# 랜덤 데이터 생성 (y = 3X + 5 + 잡음)
np.random.seed(42)
X = np.random.rand(100, 1)
print(X)
y = 3 * X + 5 + np.random.randn(100, 1)

print(y)
# 2. 데이터 분할 (학습 데이터와 테스트 데이터)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 선형 회귀 모델 생성 및 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 4. 예측
y_pred = model.predict(X_test)

# 5. 결과 출력
print(f"회귀 계수 (기울기): {model.coef_[0][0]}")
print(f"절편: {model.intercept_[0]}")
print(f"평균 제곱 오차 (MSE): {mean_squared_error(y_test, y_pred)}")
print(f"결정 계수 (R^2): {r2_score(y_test, y_pred)}")

# 6. 시각화
plt.scatter(X_test, y_test, color='black', label="실제 값")
plt.plot(X_test, y_pred, color='blue', linewidth=3, label="예측 값")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()
