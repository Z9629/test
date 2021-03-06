from json_response import JsonResponse
from aip import ocr
import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR"+BASE_DIR)
OUT = "/static/upload"
ABS_OUT = os.path.join(BASE_DIR, OUT[1:])
print(ABS_OUT)

# 定义常量
APP_ID = '9851066'
API_KEY = 'LUGBatgyRGoerR9FZbV4SQYk'
SECRET_KEY = 'fB2MNz1c2UHLTximFlC4laXPg7CVfyjV'

# 初始化AipFace对象
aipOcr = ocr(APP_ID, API_KEY, SECRET_KEY)

def upload_img(request):

    img = request.FILES.get('image')
    if not all(img):
        return JsonResponse({
                    'code':'-1',
                    'msg':'no image'
                })
    abs_path = ''
    try:
        # 存储文件
        file_name = "%s.png" % (time.time() * 1000)
        # web_path = os.path.join(OUT, file_name)
        abs_path = os.path.join(ABS_OUT, file_name)
        with open(abs_path, "wb") as fp:
            for chunk in img.chunks():
                fp.write(chunk)

    except Exception as msg:
        return JsonResponse({
            "code": -3, "msg": "Upload filed! Msg:%s" % msg
        })

    options = {
        'detect_direction': 'true',
        'language_type': 'CHN_ENG',
    }

    # 调用通用文字识别接口
    result = aipOcr.basicGeneral(get_file_content(abs_path), options)
    # print(json.dumps(result).decode("unicode-escape"))
    return JsonResponse(result)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()