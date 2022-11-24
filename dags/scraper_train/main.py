import os
import pathlib
from utils.predict_model import predict
from utils.train_model import train_model
from utils.preprocess_model import preprocess

os.chdir(pathlib.Path(os.path.dirname(__file__)))
