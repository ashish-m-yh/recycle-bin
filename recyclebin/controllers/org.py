from recyclebin import models

from flask import Blueprint, make_response, jsonify

org = Blueprint('org', __name__)


@org.route('/org/<int:org_id>', methods=['GET'])
def get_org(org_id):
    org_info = models.org.get_by_id(org_id)
    return jsonify({'org_info': org_info})


@org.route('/org', methods=['POST'])
def create_org(info):
    info = request.json

    org_info = models.org.save(info)
    #return jsonify({'org_id': })


@org.route('/org', methods=['PUT'])
def update_org(org_id):
    info = request.json
    org_info = models.org.get_by_id(org_id)
    return jsonify({'org_info': org_info})
