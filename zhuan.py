import json
import glob
import shutil

path = 'E:/sift_bow/test1/'
json_list_path = glob.glob(path + '*.jpg')
new_docu_path = 'E:/sift_bow/test/'

json_new = []
for json_path in json_list_path:
    # with open(json_path) as f:
    #     ann = json.load(f)
    #     if(len(ann) != 0):
    shutil.copy(json_path, new_docu_path)
