import os


def segment(sentence, args):
    with open(".\\docs\\cache\\predict.data", "w", encoding='utf-8') as f:
        for c in sentence:
            f.write(f"{c}\tn\tB-char\n")
    os.system(f'{args.crf_test} -m {args.crf_model} .\\docs\\cache\\predict.data > .\\docs\\cache\\new.txt')

    predict_tags = []
    with open(".\\docs\\cache\\new.txt", "r", encoding='utf-8') as f:
        for line in f.readlines():
            predict_tags.append(line.strip().split('\t')[-1])

    words = []
    for i in range(len(predict_tags)):
        word = ""
        if predict_tags[i] == "B-char":
            word += sentence[i]
            j = i + 1
            while j < len(sentence) and predict_tags[j] == "I-char":
                word += sentence[j]
                j += 1
        if word:
            words.append(word)

    result = " ".join(words)
    os.remove(".\\docs\\cache\\predict.data")
    os.remove(".\\docs\\cache\\new.txt")
    return result
