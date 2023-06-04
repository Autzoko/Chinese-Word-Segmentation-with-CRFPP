from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


class Evaluator:
    def __init__(self, outfile):
        self.outfile = outfile
        self.y_pred = []
        self.y_true = []

        self.precision_B = None
        self.recall_B = None
        self.f1_B = None

        self.precision_I = None
        self.recall_I = None
        self.f1_I = None

        self._get_data_()

    def _get_data_(self):
        with open(self.outfile, "r", encoding='utf-8') as f:
            labels = ['B-char', 'I-char']
            for line in f.readlines():
                items = line.strip().split('\t')
                if len(items) > 1:
                    if items[-1] in labels and items[-2] in labels:
                        self.y_pred.append(items[-1])
                        self.y_true.append(items[-2])

    def _cal_precision(self):
        self.precision_B = precision_score(y_true=self.y_true, y_pred=self.y_pred, pos_label='B-char')
        self.precision_I = precision_score(y_true=self.y_true, y_pred=self.y_pred, pos_label='I-char')

    def _cal_recall_(self):
        self.recall_B = recall_score(y_true=self.y_true, y_pred=self.y_pred, pos_label='B-char')
        self.recall_I = precision_score(y_true=self.y_true, y_pred=self.y_pred, pos_label='I-char')

    def _cal_f1_(self):
        self.f1_B = f1_score(y_true=self.y_true, y_pred=self.y_pred, pos_label='B-char')
        self.f1_I = precision_score(y_true=self.y_true, y_pred=self.y_pred, pos_label='I-char')

    def get_precision(self):
        self._cal_precision()
        return self.precision_B, self.precision_I

    def get_recall(self):
        self._cal_recall_()
        return self.recall_B, self.recall_I

    def get_f1(self):
        self._cal_f1_()
        return self.f1_B, self.recall_I
