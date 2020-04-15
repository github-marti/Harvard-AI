def max_value(s):
    if terminal(s):
        return utility(s)
    v = float("-inf")
    for action in actions(s):
        v = max(v, min_value(result(s, a)))
    return v

def min_value(s):
    if terminal(s):
        return utility(s)
    v = float("inf")
    for action in actions(s):
        v = min(v, max_value(result(s, a)))
    return v


