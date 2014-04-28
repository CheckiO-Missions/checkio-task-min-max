prepare = """
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

TESTS = {
    "1. Basics": [
        {
            "test_code": {
                "python-3": prepare + run_test.format(simple_max),
                "python-27": prepare + run_test.format(simple_max)
            },
            "show": {"python-3": simple_max, "python-27": simple_max},
            "answer": 3
        },
        {
            "test_code": {
                "python-3": prepare + run_test.format(simple_min),
                "python-27": prepare + run_test.format(simple_min)
            },
            "show": {"python-3": simple_min, "python-27": simple_min},
            "answer": 2
        },
        {
            "test_code": {
                "python-3": prepare + run_test.format(max_range),
                "python-27": prepare + run_test.format(max_range)
            },
            "show": {"python-3": max_range, "python-27": max_range},
            "answer": 2
        },
        {
            "test_code": {
                "python-3": prepare + run_test.format(min_hello),
                "python-27": prepare + run_test.format(min_hello)
            },
            "show": {"python-3": min_hello, "python-27": min_hello},
            "answer": 2
        },
        {
            "test_code": {
                "python-3": prepare + run_test.format(two_max_items),
                "python-27": prepare + run_test.format(two_max_items)
            },
            "show": {"python-3": two_max_items, "python-27": two_max_items},
            "answer": 2
        },
        {
            "test_code": {
                "python-3": prepare + run_test.format(lambda_key),
                "python-27": prepare + run_test.format(lambda_key)
            },
            "show": {"python-3": two_max_items, "python-27": lambda_key},
            "answer": 2
        },


    ],
    # "Extra": [
    #     {
    #         "input": [6, 3],
    #         "answer": 9,
    #         "explanation": "6+3=?"
    #     },
    #     {
    #         "input": [6, 7],
    #         "answer": 13,
    #         "explanation": "6+7=?"
    #     }
    # ]
}
