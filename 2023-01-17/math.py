# 다항 함수 그래프 그리기

# 사용할 패키지 불러오기 (매트플롯립, 넘파이)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 그래프에서 사용할 테마 설정 (plt.style.available을 사용하여 사용가능한 테마 확인가능)
mpl.style.use('bmh')
mpl.style.use('seaborn-whitegrid')

# 크기 (10,7)인 그림 생성
fig = plt.figure(figsize=(10,7))
# 그림에 좌표축 생성
ax = fig.add_subplot(1, 1, 1)
# 좌표축에 표시되는 좌표값 숫자 크기 지정
ax.xaxis.set_tick_params(labelsize=18)
ax.yaxis.set_tick_params(labelsize=18)
# 좌표 축 이름 크기 지정
plt.xlabel('$x$', fontsize=25)
plt.ylabel('$y$', fontsize=25)

# 그릴 정의역을 start(시작), stop(끝), num(등간격)순서로 생성
# -3 부터 2까지 10개의 숫자
x = np.linspace(-3, 2, 10)
y = 2*x+4
# 평면에 점을 연속적으로 찍어 그래프를 그리기 (k 옵션은 검은색을 지정)
ax.plot(x, y, 'k')

# 좌표축을 그리기 위해 미리 만들어놓은 arrowed_spines()함수 호출
arrowed_spines(fig, ax)

plt.show()