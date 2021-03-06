# -*- coding: utf-8 -*-
import pickle
from PCV.imagesearch import vocabulary
from PCV.tools.imtools import get_imlist
from PCV.localdescriptors import sift

###创建词汇

# 获取图像列表
imlist = get_imlist('./test/')
nbr_images = len(imlist)
# 获取特征列表
featlist = [imlist[i][:-3] + 'sift' for i in range(nbr_images)]

# 提取文件夹下图像的sift特征
for i in range(nbr_images):
    sift.process_image(imlist[i], featlist[i])

# 生成词汇
voc = vocabulary.Vocabulary('ukbenchtest')  # 创建词汇类
voc.train(featlist, 1000, 10)  # 单词数为1000，进行k-means训练

# 保存词汇
with open('./test/vocabulary.pkl', 'wb') as f:
    pickle.dump(voc, f)
print('vocabulary is:', voc.name, voc.nbr_words)