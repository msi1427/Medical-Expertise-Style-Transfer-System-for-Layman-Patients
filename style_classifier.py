import os
from os.path import join, dirname, realpath

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

from fastai.text.all import *

from blurr.data.all import *
from blurr.modeling.all import *

from werkzeug.utils import secure_filename

def classifier(text):

    # Returns the expertise percentage

    model_path = Path(join(dirname(realpath(__file__)), "trained_models\\" + secure_filename("style-classifier.pkl")))

    learn = load_learner(model_path)

    expertise = learn.blurr_predict(text)[0][2][0][0]

    return expertise
