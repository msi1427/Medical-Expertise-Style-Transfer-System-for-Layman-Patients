import os
from os.path import join, dirname, realpath

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

from fastai.text.all import *

from blurr.data.all import *
from blurr.modeling.all import *

from werkzeug.utils import secure_filename

def masking_expert_terms(text):

    # Masks the experts terms

    model_path = Path(join(dirname(realpath(__file__)), "trained_models\\" + secure_filename("style-classifier.pkl")))

    learn = load_learner(model_path)

    init_expertise = learn.blurr_predict(text)[0][2][0][0]
    split_text = text.split() 
    mask_x = text.split()
    
    for i in range(len(mask_x)):
        mask_x[i] = '[MASK]'
        temp_masked_str = ""
    
        for j in range(len(mask_x)):
            temp_masked_str += mask_x[j]
            if j != len(mask_x)-1 : temp_masked_str += " "
    
        curr_expertise = learn.blurr_predict(temp_masked_str)[0][2][0][0]
        if curr_expertise < .50 : break
        if init_expertise - curr_expertise >= .30 : continue # change initial_expertise
        mask_x[i]=split_text[i]
    
    masked_str = ""
    for j in range(len(mask_x)):
        masked_str += mask_x[j]
        if j != len(mask_x)-1 : masked_str += " "
    
    return masked_str


def transfer_to_layman(text):

    # Transfers an expert style text to layman style text

    masked_text = masking_expert_terms(text)

    model_path = Path(join(dirname(realpath(__file__)), "trained_models\\" + secure_filename("maskedlm-model.pkl")))

    learn = load_learner(model_path)

    layman = learn.blurr_generate(masked_text)[0]

    return layman