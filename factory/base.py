# define the data used for training and we need document (Elementary1.txt)
from ..common import *
from abc import *
import tensorflow as tf
import numpy as np

class BaseModel(object):
    __metaclass__ = ABCMeta

    def __init__(self, sess):
        self.sess = sess
        self.learningRate = None
        self.X = None
        self.Y = None
        self.dropoutRate = tf.placeholder(tf.float32)
        self.isTraining = tf.placeholder(tf.bool)
    
    @abstractmethod
    def build(self):
        pass
    @abstractmethod
    def predict(self):
        pass
    @abstractmethod
    def train(self):
        pass
    @abstractmethod
    def predict(self):
        pass
    
 

class BaseLab(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.numOfEnsemble = 1
        self.modelFilePath = None
        self.sess = None
        self.batchSize = None
        
    @abstractmethod
    def saveModel(self):
        pass
    @abstractmethod
    def loadModel(self):
        pass
    @abstractmethod
    def trainModel(self):
        pass