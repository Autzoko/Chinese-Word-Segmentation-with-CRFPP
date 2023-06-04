# Chinese Word Segmentation with CRF++
This program accomplished the task of **Chinese Word Segmentation**
by utilizing *CRF++* toolkit. The corpus I used is Renmin Daily Corpus published
by Peking University.

**On account of the version of CRF++ that I use is only for Windows platform, 
if you want to run this program on Linux or MacOS, please substitute the CRF_Tool
with the according version and modify relevant codes.**

## Run
Use command
```shell
python run.py --train
```
to train the model, the model file is saved in ./docs.

Use command
```shell
python run.py --test
```
to test the model with the test dataset, the result is saved
in ./docs.

Use command
```shell
python run.py --sentence=这句话将要被分词
```
to segment the input sentence.

## Program Structure
- CRF_Tool: The CRF++ dependencies.
- data: The directory that saves datasets.
  - processed: The processed data will be saved here.
- DataProcessor: Class for processing raw data to the format that can be handled by CRF++.
- docs: Auxiliary files will be saved here.
- Evaluator: Class for evaluating the prediction results by PRF.
- Generator: Class for generating CRF++ model and prediction results.

