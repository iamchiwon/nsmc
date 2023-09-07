#! /usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import os

def partition(target):
    dat = pd.read_csv(f'../ratings_{target}.txt', sep='\t')

    os.makedirs(f'../ratings/{target}', exist_ok=True)
    os.makedirs(f'../ratings/{target}/positive', exist_ok=True)
    os.makedirs(f'../ratings/{target}/negative', exist_ok=True)

    for row in range(0, len(dat)):
        label = dat['label'][row]
        document = dat['document'][row]
        filename = dat['id'][row]

        if type(document) != str:
            continue

        if label == 0:
            with open(f'../ratings/{target}/negative/{filename}.txt', 'w') as f:
                f.write(document)

        if label == 1:
            with open(f'../ratings/{target}/positive/{filename}.txt', 'w') as f:
                f.write(document)

partition('train')
partition('test')
