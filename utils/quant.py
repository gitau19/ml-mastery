# use in other files from utils.stats import expected_value, max_drawdown
def slope_intercept(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b

def expected_value(win_prob, win_amount, lose_amount):
    lose_prob = 1 - win_prob
    return (win_prob * win_amount) + (lose_prob * lose_amount)

def win_rate(trades):
    wins = sum(1 for t in trades if t > 0)
    return wins / len(trades) * 100

def max_drawdown(balances):
    peak = balances[0]
    max_drop = 0
    for b in balances:
        if b > peak:
            peak = b
        drop = peak - b
        if drop > max_drop:
            max_drop = drop
    return max_drop, max_drop / peak * 100