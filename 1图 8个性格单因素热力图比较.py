import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 定义数据
data = {
    '': ['8', '35', '70', 'Masculine', 'Feminine', 'Androgynous', 'Modest', 'Stylish', 'Luxury', 'Black', 'White', 'Yellow', 'Asian', 'Caucasian', 'African', 'Good-looking', 'Standard-looking', 'Unpleasant-looking', 'Disabled', 'Non-disabled'],
    'Conscientiousness': [0, 12, 38, 0, 0, 50, 50, 0, 0, 0, 0, 0, 7, 3, 3, 0, 50, 0, 50, 0],
    'Agreeableness': [50, 0, 0, 0, 45, 0, 50, 0, 0, 30, 17, 0, 9, 11, 29, 50, 0, 0, 50, 0],
    'Neuroticism': [12, 38, 0, 0, 0, 50, 50, 0, 0, 0, 0, 0, 4, 0, 2, 2, 48, 0, 50, 0],
    'Openness': [1, 49, 0, 0, 0, 50, 50, 0, 0, 10, 0, 0, 45, 0, 0, 10, 21, 19, 50, 0],
    'Extraversion': [0, 50, 0, 0, 0, 50, 50, 0, 0, 49, 0, 0, 42, 0, 0, 50, 0, 0, 50, 0],
    'Narcissism': [0, 50, 0, 0, 0, 50, 0, 50, 0, 1, 4, 0, 18, 3, 4, 50, 0, 0, 0, 50],
    'Psychopathy': [37, 13, 0, 0, 0, 34, 50, 0, 0, 0, 0, 0, 13, 0, 1, 29, 10, 11, 1, 49],
    'Machiavellianism': [0, 0, 0, 0, 0, 36, 0, 50, 0, 7, 9, 0, 7, 4, 20, 50, 0, 0, 0, 50],
}

# 转换为DataFrame
df = pd.DataFrame(data)

# 设置特征为索引
df.set_index('',inplace=True)

# 绘制热力图
plt.figure(figsize=(10, 8))
ax = sns.heatmap(df, annot=True, cmap='YlGnBu', fmt='d', linewidths=.5)
plt.xticks(rotation=30,ha='right',fontsize = 15,fontweight = 'bold')
plt.yticks(fontsize = 15,fontweight = 'bold')

# 添加分组分隔线
separator_positions = [3, 6, 9, 12, 15, 18]  # 每组结束位置
for pos in separator_positions:
    ax.hlines(pos, 0, len(df.columns), 
              colors='gray', linestyles='dashed', linewidth=1.5)


# plt.title('Model Performance Comparison')
# plt.xlabel('Models')
# plt.ylabel('Features')
plt.show()


