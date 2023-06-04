class DataProcessor:
    def __init__(self, file, args, test_rate=0.1):
        self.file = file
        self.train_data = []
        self.test_data = []
        self.content = []
        self.test_rate = test_rate
        self.args = args

        self._generate_content_()
        self._generate_train_data_()
        self._generate_test_data_()

    def _generate_content_(self):
        with open(self.file, "r", encoding='utf-8') as f:
            print("---Analyzing File Content---")
            for line in f.readlines():
                line_tuples = []
                words = line.split()
                for word in words:
                    line_tuples.append([word[0], 'n', 'B-char'])
                    if len(word) > 1:
                        for c in word[1:]:
                            line_tuples.append([c, 'n', 'I-char'])
                self.content.append(line_tuples)

    def _generate_train_data_(self):
        print("---Generating Dataset for Training---")
        for line in self.content[:int(len(self.content) * (1 - self.test_rate))]:
            self.train_data.append(line)

    def _generate_test_data_(self):
        print("---Generating Dataset for Testing---")
        for line in self.content[int(len(self.content) * (1 - self.test_rate)) + 1:]:
            self.test_data.append(line)

    def write_train_file(self):
        print(f'---Writing Into Path: {self.args.train_data}---')
        format_list = []
        with open(self.args.train_data, "w", encoding='utf-8') as  f:
            for line in self.train_data:
                for t in line:
                    format_list.append("\t".join(t) + '\n')
                format_list.append("\n")
            f.writelines(format_list)

    def write_test_file(self):
        print(f'---Writing Into Path: {self.args.test_data}---')
        format_list = []
        with open(self.args.test_data, "w", encoding='utf-8') as f:
            for line in self.test_data:
                for t in line:
                    format_list.append("\t".join(t) + '\n')
                format_list.append("\n")
            f.writelines(format_list)
