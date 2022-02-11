import pandas as pd
from sklearn.model_selection import train_test_split

def models():
  mdls = {
        # TODO: select models
    }

  return mdls

def model_build(features,truth,tag,test_size,**params):
  
 X_train, X_test, y_train, y_test = train_test_split(features, truth, test_size=test_size)
  
 if tag == 'packet_loss_ratio':
   # mdl = neighbors.KNeighborsRegressor(**params) # TODO: select models
 elif tag == 'latency':
   # mdl = linear_model.BayesianRidge(**params) # TODO: select models
    
 mdl.fit(X_train, y_train)
 preds = mdl.predict(X_test)
 dict1 = {'preds': preds, 'truth': y_test}
 out = pd.DataFrame(dict1)
 
  
 return out #returns a pandas df
