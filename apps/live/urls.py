from flask import Blueprint, request
from apps.live import view


live = Blueprint('live', __name__)


# 获取直播设备列表
@live.route('/devices', method=['GET'])
def devices():
    return view.devices()


# 获取直播页面
@live.route('/living', method=['GET'])
def living():
    
    return view.living()

