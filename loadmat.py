from os.path import dirname, join as pjoin
import scipy.io as sio

data_dir = pjoin(dirname(sio.__file__), 'matlab', 'tests', 'data')
mat_fname = 'model/MA2HDQN_model/reward.mat'

mat_contents = sio.loadmat(mat_fname,appendmat=True)
print(type(mat_contents))
print(sorted(mat_contents.keys()))
print(mat_contents['reward'][9500:])
print(mat_contents['reward'].size)

