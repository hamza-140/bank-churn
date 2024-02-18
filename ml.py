import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import plotly.express as px
# import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from imblearn.over_sampling import SMOTE
import xgboost as xgb
# from xgboost import XGBClassifier
# from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix, plot_confusion_matrix, roc_curve
# from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix, ConfusionMatrixDisplay, roc_curve
# import scikitplot as skplt
import warnings
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
df = pd.read_csv('BankChurnersUNTOUCH.csv')
df = df.iloc[:,1:-2]
df["Attrition_Flag"] = df["Attrition_Flag"].map({"Existing Customer":0, "Attrited Customer":1})
num_cols = list(df.select_dtypes(["int64","float64"]))
cat_cols = list(df.select_dtypes("object"))
# Creating the dummy variables for all the categorical features
for col in cat_cols:
    dummy_cols = pd.get_dummies(df[col], drop_first=True, prefix=col)
    df = pd.concat([df,dummy_cols],axis=1)
    df.drop(columns=col, inplace=True)
# Splitting the data into train and test
y = df.pop("Attrition_Flag")
X = df
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=69)
X_train = pd.DataFrame(X_train)
X_test = pd.DataFrame(X_test)
# Normalizing the data
req_cols = ['Customer_Age', 'Dependent_count', 'Months_on_book', 'Total_Relationship_Count',
            'Months_Inactive_12_mon', 'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
            'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt', 'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1',
            'Avg_Utilization_Ratio']
#print(len(req_cols))
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train[req_cols])
X_test = scaler.transform(X_test[req_cols])
# Applying SMOTE to handle imbalance in target variable

sm = SMOTE(random_state = 69, sampling_strategy = 1.0)

X_train, y_train = sm.fit_resample(X_train, y_train)
# XGBoost model

xgb_model = xgb.XGBClassifier(random_state=69, use_label_encoder=False, n_jobs=-1)

xgb_model.fit(X_train, y_train)
xgb_model.save_model("model_file.bin")

#
#
#
# if int(prediction)==0:
#     print("This is reliable customer.")
# else :
#     print("Untrusted customer.")