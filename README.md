# Newscaster Face Analysis
This initial project is meant as an initial analysis of facial features in American newscasters to determine a connection between their characteristics and their facial features.

## Installation/Setup
This project is based heavily on this [face classification one](https://github.com/wondonghyeon/face-classification). Key requirements to configure this code to run are:
  * [dlib](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)
  * [face_recognition](https://github.com/ageitgey/face_recognition/)
  * NumPy (```pip install numpy```)
  * pandas (`pip install pandas`)
  * scikit-learn (`pip install scikit-learn`)
  
  Once these are installed, what remains is downloading a dataset to train on. For more general work, the LFWA+ dataset can be used. However, any directory can be used for training. In my particular case, I used a custom setup of newscasters' faces, found in the `cropped` folder.

##### Feature Extraction
```bash
python2 feature-extraction.py --data_dir cropped/ --save_feature feature.csv --save_label label.csv
```
  
#### Model Training
```bash
python2 train.py --feature features.csv --label label.csv --save_model face_model.pkl
```

#### Prediction
Classify face attributes in test directory based on the training from above.
```bash
python2 pred.py --img_dir cropped_test/ --model face_model.pkl
```

#### NOTES
NewsID key: WX=1, Anchor=2, Traffic=3

anchor_model_ALL had: Iteration 351, loss = 12.60876782
anchor_model_female had: Iteration 74, loss = 15.21468414
anchor_model_male had: Iteration 64, loss = 19.56094234

