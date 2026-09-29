from decimal import Decimal, ROUND_HALF_UP


def some_expression_with_rounding(a, b):
    denominator = 1 + a ** (2 ** b)
    result = (12 * a + 25 * b) / denominator
    return float(Decimal(str(result)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
