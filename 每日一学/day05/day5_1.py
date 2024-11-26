import requests

if __name__ == '__main__':
    url = 'https://www.baidu.com'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }

    r = requests.get(url, headers=header)
    # print(r.text)
    print(r.status_code)

    #同理 put post
    # r = requests.put(url, data={'name': 'zhangsan'})
    # print(r.text)
