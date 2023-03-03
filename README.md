# Transformer_Notes
学习Transfomer的笔记

## 1.Self-Attention

![图片](https://user-images.githubusercontent.com/126166790/222720335-bbcf8ce3-01cf-4ddc-9756-3d749c1aaa07.png)

输入Q、K、V来计算自注意力，Q是query，K是key，V是value。对于一个句子（比如“因为我是蝙蝠侠”），这个句子由许多个字组成（‘因’、‘为’、‘我’......）,而对于每个单词/字，需要用一个向量来表示（embedding），比如‘因’可以表示成[1,2,3,4]，‘为’可以表示为[5,6,7,8]。每个字对应的向量有一个维度，这里给的例子中，维度是4。因此这个有7个字的句子可以表示为一个7x4的矩阵。

由于事实上的实现是多头的（下面会讲），这里先通过一个简单的例子来理解self-attention。
![图片](https://user-images.githubusercontent.com/126166790/222725393-9a1f4fec-7831-4e70-ab16-6603f5d48265.png)
为了简单，我们假设Q、K、V都是n行dk列的矩阵，即对应一个有n个单词，且表示每个单词的向量的长度为dk，至于K和V，这里先不讲具体含义（因为我也还没全弄懂），只需要知道它们是key-value对就行。
这个自注意力的计算其实就是通过计算Q和K的相似程度，然后和V得到最后的值。注意到还有一个Mask（opt.）没讲，但是你先别急。
