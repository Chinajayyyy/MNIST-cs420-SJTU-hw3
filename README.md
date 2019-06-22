#机器学习homework3
***

**姓名：范哲栋**
**学号：516030910449**

***

##文件夹结构

<kbd>README.md</kbd>
<kbd>README.pdf</kbd>是<kbd>README.md</kbd>导出的pdf文件，如何有需要可以直接看<kbd>README.pdf</kbd>
<kbd>report.pdf</kbd>

> SVM&NN
>> DataA
>>> breast_cancer.py
>>> draw_iris.py
>>> iris.py
>>> iris.csv

>> DataB
>>> draw_cnn.py
>>> draw_svm.py
>>> first_cnn.py
>>> input_data.py
>>> SVM.py
>>> CNN实验数据.xlsx
>>> SVM实验数据.xlsx
>>> MNIST_data
>>>> datafiles  
  
***
## DataA文件夹
<kbd>breast_cancer.py</kbd>和<kbd>iris.py</kbd>这两个python文件是针对数据集训练模型并测试模型得分的数据，以<kbd>iris.py</kbd>文件为例，如果需要改变数据集大小或PCA降维的维数，需要手动修改<kbd>iris.py</kbd>第27行test_size参数和第31行n_components参数。而<kbd>breast_cancer.py</kbd>文件中的算法与<kbd>iris.py</kbd>大体相同，最终获得的结果体现爱数据集的差距上，因此在report中主要以iris为数据集结果。

<kbd>iris.csv</kbd>文件是手动收集的不同状态下整个模型的分类效果的csv文件。

<kbd>draw.py</kbd>文件是通过<kbd>iris.csv</kbd>中收集的数据将整个数据可视化出来。

***
## DataB文件夹
<kbd>CNN实验数据.xlsx</kbd>和<kbd>SVM实验数据.xlsx</kbd>两个文件中记录了使用数据集操作数据后的一系列结果。

<kbd>first_cnn.py</kbd>文件中是CNN网络的结构以及生成model并且测试的内容。如果需要修改CNN迭代的次数，只需要修改文件中第102行的数字即可，实验数据是1000~20000。

<kbd>SVM.py</kbd>文件内容是SVM的model生成和测试。如果要修改数据集使用的大小来测试生成的不同的model，只需要修改35，36，39行的数字，实验数据是从10000～55000。

<kbd>draw_cnn.py</kbd>和<kbd>draw_svm.py</kbd>文件是将xlsx文件中的数据可视化。

<kbd>input_data.py</kbd>文件是导入数据到<kbd>first_cnn.py</kbd>和<kbd>SVM.py</kbd>一个脚本。所有测试用的数据保存在<kbd>MNIST_data</kbd>文件夹


***
> Casual
>> wiki4HE.csv
>> wiki.tet

***
## wiki4HE.csv
<kbd>wiki4HE.csv</kbd>文件中存放了这次实验所用的所有数据，对于缺失的数据采用<kbd>?</kbd>来代替

## wiki.tet
<kbd>wiki.tet</kbd>文件存放了通过FCI算法应用于<kbd>wiki4HE.csv</kbd>文件后生成的模型文件，这个文件需要通过<kbd>Tetrad</kbd>软件来打开。
