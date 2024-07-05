from os.path import dirname, join as pjoin
import scipy.io as sio
import pandas as pd

data_dir = pjoin(dirname(sio.__file__), 'matlab', 'tests', 'data')
mat_fname = 'model/MA2HDQN_model_learn_rate_adaptive/reward.mat'

mat_contents = sio.loadmat(mat_fname,appendmat=True)
print(type(mat_contents))
print(sorted(mat_contents.keys()))
print(mat_contents['reward'][45000:47000])
print(mat_contents['reward'].size)

# 将数据转换为pandas DataFrame
df = pd.DataFrame(mat_contents['reward'])

# 将DataFrame写入Excel文件
df.to_excel('model/MA2HDQN_model_learn_rate_adaptive.xlsx', encoding='utf-8',  index=False)

