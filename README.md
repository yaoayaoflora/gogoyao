# Knowledge

## Machine Learning

### Linear Regression
### Logistic Regression
【机器学习】逻辑回归（非常详细） - 阿泽的文章 - 知乎
https://zhuanlan.zhihu.com/p/74874291
### SVM
### Decision Tree
### Ensemble Methods
https://scikit-learn.org/stable/modules/ensemble.html#

#### Gradient Boosting Decision Tree (GBDT)

##### LightGBM
https://github.com/Microsoft/LightGBM
###### Notes
GBDT is an ensemble model of decision trees, which are trained in sequence. In each iteration, GBDT learns the decision trees by fitting the negative gradients (also known as residual errors).

The main cost in GBDT lies in learning the decision trees, and the most time-consuming part in learning a decision tree is to find the best split points. One of the most popular algorithms to find split points is the **pre-sorted algorithm**, which enumerates all possible split points on the pre-sorted feature values. This algorithm is simple and can find the optimal split points, however, it is inefficient in both training speed and memory consumption. Another popular algorithm is the **histogram-based algorithm**. Instead of finding the split points on the sorted feature values, histogram-based algorithm buckets continuous feature values into discrete bins and uses these bins to construct feature histograms during training, which is more efficient in both memory consumption and training speed.

There have been quite a few implememtation of GBDT in the literature, including XGBoost, pGBRT, scikit-learn, and gbm in R. Scikit-learn and gbm in R implements the pre-sorted algorithm, and pGBRT implements the histogram-based algorithm. XGBoost supports both the pre-sorted algorithm and histogram-based algorithm.

###### Questions

##### XGBoost

##### Random Forest
