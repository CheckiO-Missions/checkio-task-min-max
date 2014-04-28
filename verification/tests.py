init_code = """
if not "min" in USER_GLOBAL:
    raise NotImplementedError("Where is 'min'?")
if not "max" in USER_GLOBAL:
    raise NotImplementedError("Where is 'max'?")

min = USER_GLOBAL['min']
max = USER_GLOBAL['max']
"""

run_test = """RET['code_result'] = {}
"""

###Basic

simple_max = "max(3, 2)"
simple_min = "min(3, 2)"
max_range = "max([1, 2, 0, 3, 4])"
min_hello = "min('hello')"
two_max_items = "max(2.2, 5.6, 5.9, key=int)"
lambda_key = "min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1])"


def prepare_test(test, answer):
    return {
            "test_code": {"python-3": init_code + run_test.format(test), "python-27": init_code + run_test.format(test)},
            "show": {"python-3": test, "python-27": test},
            "answer": answer}


TESTS = {
    "1. Basics": [
        prepare_test("max(3, 2)", 3),
        prepare_test("min(3, 2)", 2),
        prepare_test("max([1, 2, 0, 3, 4])", 4),
        prepare_test("min('hello')", "e"),
        prepare_test("max(2.2, 5.6, 5.9, key=int)", 5.6),
        prepare_test("min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1])", [9, 0])
    ],
    "Extra": [
        prepare_test("max([0])", 0),
        prepare_test("min((9,))", 9),
        prepare_test("max(range(6))", 5),
        prepare_test("min({1, 2, 3, 4, -10})", -10),
        prepare_test("max(set('djsaljldsklfjzx'))", "z"),
        prepare_test("min(set('djsaljldsklfjzx'))", "a"),
        prepare_test("max([1, 2, 3], [5, 6], [7], [0, 0, 0, 1])", [7]),
        prepare_test("min([1, 2, 3], [5, 6], [7], [0, 0, 0, 10], key=sum)", [1, 2, 3]),
        prepare_test("max(True, False, -1, key=lambda x: not x)", False),
        prepare_test("min(True, False, -1)", -1),
    ]
}
