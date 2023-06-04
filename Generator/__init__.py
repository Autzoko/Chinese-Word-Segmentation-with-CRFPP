import os


class CrfCaller:
    def __init__(self, args):
        self.test_data = args.test_data
        self.train_data = args.train_data
        self.crf_learn = args.crf_learn
        self.crf_test = args.crf_test
        self.args = args
        self.template = args.template

    def _crf_train_(self):
        command = f'{self.crf_learn} -f {self.args.crf_f} -c {self.args.crf_c} {self.template} {self.train_data} {self.args.crf_model} -t'
        os.system(command)

    def _crf_test_(self, output_file):
        command = f'{self.crf_test} -m {self.args.crf_model} {self.test_data} > {output_file}'
        os.system(command)

    def generate(self, output_file):
        if self.args.train:
            self._crf_train_()
        if self.args.test:
            self._crf_test_(output_file)








