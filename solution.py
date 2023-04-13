
import pandas as pd
import numpy as np

chat_id = 474140315 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    conv_x = x_success/x_cnt
    conv_y = y_success/y_cnt
    p = (x_success + y_success) / (x_cnt + y_cnt)
    z = (conv_x - conv_y) / math.sqrt(p*(1-p)*(1/x_cnt + 1/y_cnt))
    critical_value = norm.ppf(0.03)  

return abs(z) > critical_value
