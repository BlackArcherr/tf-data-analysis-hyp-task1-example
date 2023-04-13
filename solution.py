
import pandas as pd
import numpy as np
import statsmodels
chat_id = 474140315 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
    z_score, p_value = statsmodels.stats.proportion.proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='larger')
    return p_value < 0.06
