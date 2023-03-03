# Transformer_Notes
学习Transfomer的笔记

## 1.Self-Attention

![图片](https://user-images.githubusercontent.com/126166790/222720335-bbcf8ce3-01cf-4ddc-9756-3d749c1aaa07.png)

输入Q、K、V来计算自注意力，Q是query，K是key，V是value。对于一个句子（比如“因为我是蝙蝠侠”），这个句子由许多个字组成（‘因’、‘为’、‘我’......）,而对于每个单词/字，需要用一个向量来表示（embedding），比如‘因’可以表示成[1,2,3,4]，‘为’可以表示为[5,6,7,8]。每个字对应的向量有一个维度，这里给的例子中，维度是4。因此这个有7个字的句子可以表示为一个7x4的矩阵。
