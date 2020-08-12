from app.api import bp

@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    '''
    :param id: id of user
    :return: information about particular user
    '''
    pass

@bp.route('/users', methods=['GET'])
def get_users():
    pass

@bp.route('/users/<int: id>/followers', method=['GET'])
def get_followers(id):
    pass

@bp.route('/users/<int: id>/followed', method=['GET'])
def get_followed(id):
    pass

@bp.route('/users', methods=['POST'])
def create_user():
    pass

@bp.route('/users/<init:id>', methods=['PUT'])
def update_user(id):
    pass

