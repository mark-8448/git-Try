import decimal
with decimal.localcontext() as ctx:
    ctx.prec = 3  # знаки после запятой
    print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
# 0.333
