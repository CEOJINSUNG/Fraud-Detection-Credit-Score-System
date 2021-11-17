from django.shortcuts import render
from django.http import HttpResponse, Http404

# rest_framework setting
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Fraud Detection System
import boto3
from backend.settings import MY_AWS_ACCESS_KEY_ID, MY_AWS_SECRET_ACCESS_KEY
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_agg import FigureCanvasAgg
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.metrics import average_precision_score

class VisualizaitonInPerson(APIView):
    def get_object(self, request, pk=None):
        s3 = boto3.resource(
            "s3",
            aws_access_key_id = MY_AWS_ACCESS_KEY_ID,
            aws_secret_access_key = MY_AWS_SECRET_ACCESS_KEY
        )
        bucket = s3.Object("jinsung-fraud-detection", "s3://jinsung-fraud-detection/transaction/dt={}/transaction.parquet".format(request))
        df = pd.read_parquet("{}".format(bucket))
        return 0

    def get(self, request, pk=None): 
        data = self.get_object(request)
        if data is not None:
            sns.set_style("whitegrid")
            sns_plot = sns.countplot(x="COD_GENDER", data=data)
            image = sns_plot.savefig("output.png")
            return image
        raise Http404

# Create your views here.
# class Visualization(APIView):
#     def get(self, request, format=None):
#         df = read_file("/Users/kimjinsung/desktop/Github/Fraud-Detection/data/PS_20174392719_1491204439457_log.csv")
#         df = df.rename(
#             columns = {
#                 "oldbalanceOrg" : "oldBalanceOrig",
#                 "newbalanceOrig" : "newBalanceOrig",
#                 "oldbalanceDest" : "oldBalanceDest",
#                 "newbalanceDest" : "newBalanceDest",
#             }
#         )

#         X = df.loc[(df.type == "TRANSFER") | (df.type == "CASH_OUT")]

#         randomState = 5
#         np.random.seed(randomState)

#         Y = X["isFraud"]
#         del X["isFraud"]

#         # Eliminate things 
#         X = X.drop(["nameOrig", "nameDest", "isFlaggedFraud"], axis = 1)

#         X.loc[X.type == "TRANSFER", "type"] = 0
#         X.loc[X.type == "CASH_OUT", "type"] = 1
#         X.type = X.type.astype(int)

#         # Fill the blank table
#         X.loc[(X.oldBalanceDest == 0) & (X.newBalanceDest == 0) & (X.amount != 0), ["oldBalanceDest", "newBalanceDest"]] = -1
#         X.loc[(X.oldBalanceOrig == 0) & (X.newBalanceOrig == 0) & (X.amount != 0), ["oldBalanceOrig", "newBalanceOrig"]] = np.nan

#         # Feature Engineering
#         X["errorBalanceOrig"] = X.newBalanceOrig + X.amount - X.oldBalanceOrig
#         X["errorBalanceDest"] = X.oldBalanceDest + X.amount - X.newBalanceDest

#         # Data Visualization
#         limit = len(X)
#         ax = plotStrip(Y[:limit], X.step[:limit], X.type[:limit])
#         ax.set_ylabel("time [hour]", size = 16)
#         ax.set_title("Striped vs. homogenous fingeerprints of genuine and fraudulent transactions over time", size = 20)

#         canvas = FigureCanvasAgg(ax)
#         response = HttpResponse(mimetype="image/png")
#         canvas.savefig(response, format="png")

#         return 0


# def plotStrip(x, y, hue, figsize = (14, 9)):
#     fig = plt.figure(figsize = figsize)
#     colours = plt.cm.tab10(np.linspace(0, 1, 9))
#     with sns.axes_style("ticks"):
#         ax = sns.stripplot(
#             x, y, hue=hue, jitter=0.4, marker=".", size=4, palette=colours
#         )
#         ax.set_xlabel("")
#         ax.set_xticklabels([
#             "genuine", "fradulent"
#         ], size = 16)
#         for axis in ["top", "bottom", "left", "right"]:
#             ax.spines[axis].set_linewidth(2)
        
#         handles, labels = ax.get_legend_handles_labels()
#         plt.legend(handles, ["Transfer", "Cash out"], bbox_to_anchor=(1, 1),
#             loc=2,
#             borderaxespad=0, 
#             fontsize=16
#         )

#     return ax

# def read_file(filename):

#     """Read file with **kwargs; files supported: xls, xlsx, csv, csv.gz, pkl"""

#     read_map = {'xls': pd.read_excel, 'xlsx': pd.read_excel, 'csv': pd.read_csv,
#                 'gz': pd.read_csv, 'pkl': pd.read_pickle}

#     ext = os.path.splitext(filename)[1].lower()[1:]
#     assert ext in read_map, "Input file not in correct format, must be xls, xlsx, csv, csv.gz, pkl; current format '{0}'".format(ext)
#     assert os.path.isfile(filename), "File Not Found Exception '{0}'.".format(filename)

#     return read_map[ext](filename)

