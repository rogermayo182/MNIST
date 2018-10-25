# MNIST
Train the MNIST model and use the model to evaluate the image

本项目在python 2.7环境下测试

1，打开mnist_deep.py,设置circle_step（总训练周期），batch_size（每个周期使用的训练图片数目）；

2，运行mnist_deep.py文件，运行结束后，将在当前目录下生成models目录，训练好的模型文件全部在此文件夹下；

3，运行eval.py文件，将对当前目录下的1.jpg文件进行评估，并输出评估结果；

4，可以将自己的数字图片文件名替换eval.py中的‘1.jpg'进行评估；

5，玩的开心；

1，open the mnist_deep.py,set the value of circle_step(total circle number of the train),batch_size(the image number for each 
circle)

2,run the mnist_deep.py,after the run terminate,the trained model files created in models dirctory

3,ruan eval.py to evaluate the '1.jpg' image files under the current dirctory

4,you can replace the '1.jpg' in eval.py with you own image file name to evaluate it yourself.

5,enjoy yourself
