from flask import Blueprint, request
import apps.gov.view as view

gov = Blueprint('gov', __name__)


@gov.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return view.login()
	else:
		return view.loginPage()

@gov.route('/regist', methods=['POST'])
def regist():
	return view.regist()

@gov.route('/monitor')
def monitor():
	return view.monitor()