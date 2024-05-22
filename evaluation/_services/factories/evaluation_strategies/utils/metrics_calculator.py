def calculate_base_values(target_indexes, predicted_indexes):
    tp, fp, tn, fn = 0, 0, 0, 0
    for target_i, pred_i in zip(target_indexes, predicted_indexes):
        if not pred_i and not target_i:
            tn += 1
        elif set(pred_i) == set(target_i):
            tp += 1
        elif set(pred_i).issuperset(set(target_i)):
            fp += 1
        elif set(target_i).difference(set(pred_i)):
            fn += 1
    return tp, fp, tn, fn


def accuracy_score(target_indexes, predicted_indexes):
    tp, fp, tn, fn = calculate_base_values(target_indexes, predicted_indexes)
    return (tp + tn) / (tp + fp + tn + fn) if (tp + fp + tn + fn) > 0 else 0


def precision_score(target_indexes, predicted_indexes, average):
    tp, fp, tn, fn = calculate_base_values(target_indexes, predicted_indexes)
    return tp / (tp + fp) if (tp + fp) > 0 else 0


def recall_score(target_indexes, predicted_indexes, average):
    tp, fp, tn, fn = calculate_base_values(target_indexes, predicted_indexes)
    return tp / (tp + fn) if (tp + fn) > 0 else 0


def f1_score(target_indexes, predicted_indexes, average):
    precision = precision_score(target_indexes, predicted_indexes, 0)
    recall = recall_score(target_indexes, predicted_indexes, 0)
    return (2 * (precision * recall)) / (precision + recall) if (precision + recall) > 0 else 0