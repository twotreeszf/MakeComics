import pyjion
pyjion.enable()
import sys
from os import path
import os
from multiprocessing import Pool
import multiprocessing
from make_comics import make_comics


def batch_make_comics(root_folder:str):
    pool = Pool(multiprocessing.cpu_count())

    for sub_folder in os.listdir(root_folder):
        folder_path = path.join(root_folder, sub_folder)
        if path.isdir(folder_path):
            pool.apply_async(make_comics, (folder_path, ))

    pool.close()
    pool.join()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        folder = sys.argv[1]
        batch_make_comics(folder)