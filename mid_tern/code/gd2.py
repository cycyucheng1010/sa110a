
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation
# 學習率
learning_rate = 0.1

# 初始位置
start_position = 5
old_position =0
new_position =0
#x介於-6到6,y=x^2
x = np.arange(-6, 6.1, 0.1)
y = x**2


plt.xlabel('position')
plt.ylabel('value')
plt.title('f(x)=x^2')
plt.grid(True)
for i in range(1, 11):
    if i == 1:
        old_position = start_position
    else:
        old_position = new_position
    
    #f(x) = x^2 微分後: f'(x) =2x
    new_position = old_position - learning_rate * (2*old_position)
    plt.plot(x, y)
    plt.grid(True)
    plt.plot((old_position, new_position), (old_position**2, new_position**2), 'ro-')
    title_name = 'f(x)=x^2, error='+str(abs(new_position**2)) +',learning rate='+str(learning_rate)
    plt.title(title_name)
    #plt.title('f(x)=x^2, error=' + '{:.2f}'.format(abs(new_position**2)) +',learning rate='+'{:2.f}'.format(learning_rate))
    plt.show()


