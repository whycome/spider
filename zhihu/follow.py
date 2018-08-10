# coding:utf-8

"""爬取知乎专栏关注人数, 并且写入excel"""

import requests
import json
import pandas as pd

url = 'https://www.zhihu.com/api/v4/columns/donglaoshi/followers'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'referer': 'https://zhuanlan.zhihu.com/donglaoshi'
}
params = {
    'include': 'data[*].follower_count,gender,is_followed,is_following',
    'limit': 10,
    'offset': 0
}

result_list = []
def main():
    for i in range(0, 30):
        params.update({'offset': i * 10})
        print(params)
        r = requests.get(url, params, headers=headers)
        res = r.json()
        result_list.extend(res.get('data', []))

    df = pd.DataFrame(result_list)
    df.to_excel('/Users/wan/Desktop/zhi_3.xlsx')


if __name__ == '__main__':
    main()