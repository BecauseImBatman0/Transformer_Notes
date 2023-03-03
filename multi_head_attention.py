import numpy as np
import torch.nn as nn
import torch
class Attention1(nn.Module):
    def __init__(self):
        super(Attention1,self).__init__()
        self.softmax=nn.Softmax(dim=1)

    def forward(self,Q,K,V):
        '''
        Q、K、V都是n*dk的矩阵，
        即对应一个n个单词的句子，词embedding维度为dk
        '''
        n,dk=Q.size()
        score=torch.matmul(Q,K.t())/np.sqrt(dk)
        score=self.softmax(score)
        return torch.matmul(score,V)
