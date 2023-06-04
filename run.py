import argparse
from Generator import CrfCaller
from DataProcessor import DataProcessor
from Evaluator import Evaluator


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--crf_f", type=int, default=8)
    parser.add_argument("--crf_c", type=int, default=4)
    parser.add_argument("--train_data", type=str, default='.\\data\\processed\\train.txt')
    parser.add_argument("--test_data", type=str, default='.\\data\\processed\\test.txt')
    parser.add_argument("--template", type=str, default='.\\docs\\template')
    parser.add_argument("--crf_model", type=str, default='.\\docs\\model')
    parser.add_argument("--crf_learn", type=str, default='.\\CRF_Tool\\crf_learn')
    parser.add_argument("--crf_test", type=str, default='.\\CRF_Tool\\crf_test')
    parser.add_argument("--train", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    args = parser.parse_args()

    processor = DataProcessor(file='.\\data\\pku_training.utf8', args=args)
    processor.write_train_file()
    processor.write_test_file()

    caller = CrfCaller(args)
    caller.generate('.\\docs\\crf_pred.txt')

    evaluator = Evaluator(".\\docs\\crf_pred.txt")
    b_precision, i_precision = evaluator.get_precision()
    b_recall, i_recall = evaluator.get_recall()
    b_f1, i_f1 = evaluator.get_f1()

    print("PRF Score When B-char is the Positive Label")
    print(f'Precision: {b_precision}')
    print(f'Recall: {b_recall}')
    print(f'F-1: {b_f1}')

    print("\nPRF Score When I-char is the Positive Label")
    print(f'Precision: {i_precision}')
    print(f'Recall: {i_recall}')
    print(f'F-1: {i_f1}')


if __name__ == '__main__':
    run()
