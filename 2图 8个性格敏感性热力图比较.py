import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 常量定义
CATEGORY_DICT = {
    'Age': [0, 1, 2],
    'Gender': [3, 4, 5],
    'Dressing': [6, 7, 8],
    'Color': [9, 10, 11],
    'Race': [12, 13, 14],
    'Look': [15, 16, 17],
    'Healthy': [18, 19]
}

MODELS = [
    'Conscientiousness', 'Agreeableness', 'Neuroticism',
    'Openness', 'Extraversion', 'Narcissism',
    'Psychopathy', 'Machiavellianism'
]

PLOT_STYLE = {
    'figsize': (12, 7),
    'cmap': "YlGnBu",
    'annot': True,
    'fmt': ".2f",
    'xtick_params': {'rotation': 30, 'ha': 'right', 'fontsize': 12, 'fontweight': 'bold'},
    'ytick_params': {'rotation': 0, 'fontsize': 12, 'fontweight': 'bold'}
}

def calculate_similarity_matrix(data: np.ndarray) -> np.ndarray:
    """计算类别相似性矩阵"""
    num_categories = len(CATEGORY_DICT)
    similarity_matrix = np.zeros((num_categories, num_categories))
    categories = list(CATEGORY_DICT.items())
    
    # 使用向量化操作替代嵌套循环
    for i, (_, x_indices) in enumerate(categories):
        for j, (_, y_indices) in enumerate(categories):
            sub_matrix = data[np.ix_(x_indices, y_indices)]
            similarity_matrix[i, j] = 1 - np.sum(sub_matrix) / 50
            
    return (np.sum(similarity_matrix, axis=0) - 1) / 6

def prepare_heatmap_data(*datasets: np.ndarray) -> np.ndarray:
    """准备热力图数据"""
    return np.vstack([calculate_similarity_matrix(d).reshape(1, -1) for d in datasets]).T

def visualize_personality_traits(heatmap_data: np.ndarray) -> None:
    """可视化人格特质热力图"""
    plt.figure(figsize=PLOT_STYLE['figsize'])
    ax = sns.heatmap(
        heatmap_data,
        cmap=PLOT_STYLE['cmap'],
        annot=PLOT_STYLE['annot'],
        fmt=PLOT_STYLE['fmt']
    )
    
    # 设置坐标轴标签
    ax.set_xticklabels(MODELS, **PLOT_STYLE['xtick_params'])
    ax.set_yticklabels(CATEGORY_DICT.keys(), **PLOT_STYLE['ytick_params'])
    
    plt.tight_layout()
    plt.show()

# 使用
if __name__ == "__main__":
    # 有预定义的array数据data
    input_datasets = [data_1, data_2, data_3, data_4, 
                    data_5, data_6, data_7, data_8]
    
    # 数据处理流水线
    heatmap_matrix = prepare_heatmap_data(*input_datasets)
    visualize_personality_traits(heatmap_matrix)
