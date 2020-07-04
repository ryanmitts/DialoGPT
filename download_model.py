import os
import sys
import logging
from functools import partial

from demo_utils import download_model_folder
import argparse
import subprocess as sp

download_model = partial(download_model_folder, DATA_FOLDER='models')

# model size:  could be one of 'small' (GPT2 with 117M), 'medium'(345M) or 'large' (1542M)
# dataset: one of 'multiref' or 'dstc'
# from_scratch: True : load model trained from scratch or False: load model trained from fine-tuning the GPT-2
target_folder = download_model(model_size='medium', dataset='multiref', from_scratch=False)