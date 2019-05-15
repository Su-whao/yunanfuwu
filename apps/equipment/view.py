from flask import request, session, jsonify, render_template, url_for, redirect
from models import User, Group, Equipment
from db import db


def getEquipments():
    '''
        设备信息获取
    :return:
    '''
    return redirect('/monitor')


def addEquipment():
    '''
        新增设备
        将新设备添加至数据库
    :return: 数据添加结果
    '''
    name = request.form.get('name')
    user_id = session.get('id')
    if not user_id:
        return jsonify({'msg': 'fail', 'data': 'please to login'})
    user = User.query.filter(User.id == user_id).first()
    try:
        equipment = Equipment(name=name)
        equipment.group.append(user.group)
        while user.parent_id:
            user = user.parent
            equipment.group.append(user.group)
        db.session.add(equipment)
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify({'msg': 'fail', 'data': 'add equipment error when commit database'})
    return jsonify({'msg': 'success', 'data': 'add success'})


def modifyEquipment(eid):
    '''
        获取用户提交要修改的设备信息
        修改设备信息并存储
    :param eid: 用户ID
    :return: 设备信息修改状态
    '''
    key = request.form.get('key')
    value = request.form.get('value')
    if value == '':
        value = None
    try:
        print(key, value)
        equipment = Equipment.query.filter(Equipment.id == eid)
        equipment.update({key: value})
        db.session.commit()
        return jsonify({'msg': 'success', 'data': 'modify equipment success'})
    except Exception as e:
        print(e)
        return jsonify({'msg': 'fail', 'data': 'modify equipment error when select equipments'})


def showEquipments():
    '''
        查询当前用户拥有的设备
        获取设备信息
        设备信息展示
    :return: 设备信息
    '''
    user_id = session.get('id')
    equipments = User.query.filter(User.id == user_id).first().group.equipments
    data = {
        'base':{
            'pageTitle': '设备信息-云安服务',
            'avatarImgUrl': '/static/img/yunan_logo_1.png',
            'pageNow': '设备信息',
            'username': session.get('username'),
            'userid': session.get('id')
        },
        'equipments': [
            {
                'name': e.name,
                'status': e.status,
                'use_department': e.use_department,
                'location': e.location,
                'remark': e.remarks,
                'manufacturer': e.manufacturer,
                'model': e.model,
                'create_time': e.create_time,
                'id': e.id
            }
            for e in equipments
        ]
    }
    return render_template('equipments.html', **data)


def showEditEquipment(eid):
    '''
        通过设备ID查询设备信息
        设备信息修改并存储
    :param eid: 设备ID
    :return:
    '''
    e = Equipment.query.filter(Equipment.id == eid).first()
    data = {
        'base': {
            'pageTitle': '设备信息-云安服务',
            'avatarImgUrl': '/static/img/yunan_logo_1.png',
            'pageNow': '设备信息',
            'username': session.get('username'),
            'userid': session.get('id')
        },
        'equipment': {
                'name': e.name,
                'status': e.status,
                'use_department': e.use_department,
                'location': e.location,
                'remarks': e.remarks,
                'manufacturer': e.manufacturer,
                'model': e.model,
                'create_time': e.create_time,
                'id': e.id,
                'ip': e.ip,
                'gaode_longitude': e.gaode_longitude,
                'gaode_latitude': e.gaode_latitude
            }
    }
    return render_template('editEquipment.html', **data)


def showAddEquipment():
    '''
        新增设备展示
    :return:
    '''
    data = {
        'base':{
            'pageTitle': '添加设备-云安服务',
            'avatarImgUrl': '/static/img/yunan_logo_1.png',
            'pageNow': '添加设备',
            'username': session.get('username'),
            'userid': session.get('id')
        }
    }
    return render_template('addEquipment.html', **data)