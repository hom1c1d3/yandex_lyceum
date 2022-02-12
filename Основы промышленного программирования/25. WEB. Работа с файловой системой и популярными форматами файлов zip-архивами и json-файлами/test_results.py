import json
import sys


def get_scores_by_tests(file_name):
    with open(file_name, 'r', encoding='utf8') as fd:
        scoring = json.load(fd)['scoring']
    scores_by_tests = {}
    for block in scoring:
        points = block['points']
        tests = block['required_tests']
        single_test_points = points / len(tests)
        block_scores = {tst: single_test_points for tst in tests}
        scores_by_tests.update(block_scores)
    return scores_by_tests


def main():
    scores_by_test = get_scores_by_tests('scoring.json')
    test_results = sys.stdin.read().splitlines()
    res_score = 0
    for test_num, test_res in enumerate(test_results, 1):
        if test_res != 'ok':
            continue
        test_score = scores_by_test.get(test_num, 0)
        res_score += test_score
    print(int(res_score))


if __name__ == '__main__':
    main()