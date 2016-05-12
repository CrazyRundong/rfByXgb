# -*- coding: utf-8 -*-
# Rundong Li, UESTC
import xgb2rf
from pandas import DataFrame
import pandas as pd

# testDF1 = DataFrame([[1,2,'1'],[3,4,'cc'],[1,3,'1']], columns=['num_0','num_1','cate_0'])
# testDF2 = DataFrame([[1,2,'1'],[8,4,'cc'],[15,3,'1']], columns=['num_0','num_1','cate_0'])
# label2 = DataFrame([True, True, False], columns=['label'])
#
# paraDic = {'n_estimators':5, 'max_depth':5, 'max_features':6, 'bootstrap':False, 'bootStrapEqu':False}
# testLearner = xgb2rf.Learner(paraDic)
# testLearner.fit(testDF2, label2)
# prediction1 = testLearner.predict(testDF1)
# print prediction1

# large data test...
param = {'silent': 1, 'eval_metric': 'auc', 'nthread': 4, 'eta': 0.2, 'objective': 'binary:logistic', 'max_depth': 6,
         'bootstrap': True}
dataPath = '../mojin/data/PPD-First-Round-Data-Update/Training Set/PPD_Training_Master_GBK_3_1_Training_Set.csv'
dataRaw = pd.read_csv(dataPath, index_col=u'Idx', parse_dates=[u'ListingInfo'], na_values=['不详', -1, 'NULL', ' '],
                      nrows=20)
dataLabel = pd.DataFrame(dataRaw.iloc[:, -2], columns=['label'])
dataDate = dataRaw.iloc[:, -1]
dataCook = dataRaw.drop([u'target', u'ListingInfo'], axis=1)
testLearner = xgb2rf.Learner(param)
testLearner.fit(X=dataCook, y=dataLabel)
