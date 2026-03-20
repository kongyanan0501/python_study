"""
函数  类型注解
"""

# ### 案例2: 订单总金额计算
# 定义一个用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额的函数。

# ## 具体规则
# 1. **优惠券**：需要商品金额满 5000 才可以使用，且优惠券金额不能超过商品总价。
# 2. **积分抵扣**：需要商品总金额满 5000 才可以使用，100 积分抵扣 1 元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。


# 定义函数-----# (鼠标，100，2)，（键盘199，1），200,2000,9.9
def order_cal(*args: tuple[str, float, int], coupon=0, score=0, delivery=0):

    # 计算商品总额
    order_total = sum(good[1] * good[2] for good in args)

    # 扣减优惠券
    if order_total >= 5000 and coupon < order_total:
        order_total -= coupon

    # 扣减积分
    if order_total >= 5000 and score // 100 < order_total:
        order_total -= score // 100

    # 添加运费
    order_total += delivery
    return order_total


total = order_cal(
    ("鼠标", 288, 2),
    ("键盘", 388, 1),
    ("手机", 6999, 1),
    coupon=10,
    score=4000,
    delivery=9.9,
)
print(total)


# 如果没有优惠券和积分，调用函数不输入这两个参数时会报错。因为函数必须调用全部参数。所以需要把优惠券积分参数设置为默认参数。
