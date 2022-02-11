import sys
import os
import json

sys.path.insert(0, 'src')

import pandas as pd
import numpy as np

from etl import load_data
from features import apply_features
from model import model_build

def main():
  """
  Runs all the src code in one script. The main method in our project that runs our project
  
  `main` runs the targets in order of data=>analysis=>model.
  """
  datalist = [] # TODO: input dataset filenames
  
  data = load_data(datalist)
  data = apply_features(data)
  
  with open('config/model-params.json') as fh:
    data_cfg = json.load(fh)
  
  # TODO: update X
  X = data[['1->2Bytes', '2->1Bytes', '1->2Pkts', '2->1Pkts', 'max_packet_size', 
               'range_packet_size', 'avg_packet_size', 'longest_packet_dur', 'total_packet_dir',
               'total_packets', 'total_bytes', 'interaction_length', 'bytes_time_ratio', 'packets_time_ratio']]
  y = data.packet_loss_ratio
  y1 = data.latency
  
  #Packet Loss Predictions
  packet_loss_out = model_build(X, y, 'packet_loss_ratio', 0.33, **data_cfg['knn_regressor']) # TODO: change models
  
  #Latency Predictions
  latency_out = model_build(X, y1, 'latency', 0.33, **data_cfg['ridge_regressor']) # TODO: change models
  
  packet_loss_out.to_csv('data/out/preds_packet_loss.csv')
  latency_out.to_csv('data/out/preds_latency.csv')
  
  return
  
if __name__ == '__main__':
    main()
