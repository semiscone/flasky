from flask import jsonify, request, g, abort, url_for, current_app
from .. import db
from ..models import Order, Permission
from . import api
from .decorators import permission_required
from .errors import forbidden


@api.route('/order/')
def get_orders():
    order = Order.from_json(request.json)
    print(order)
    return jsonify({'status': "success"})


@api.route('/order/', methods=['POST'])
def new_orders():
    print(request.json)
    #post = Order.from_json(request.json)
    #print(post)
    return jsonify({'status': "success"})




@api.route('/order/<int:id>', methods=['PUT'])
@permission_required(Permission.WRITE_ARTICLES)
def edit_orders(id):
    post = Post.query.get_or_404(id)
    if g.current_user != post.author and \
            not g.current_user.can(Permission.ADMINISTER):
        return forbidden('Insufficient permissions')
    post.body = request.json.get('body', post.body)
    db.session.add(post)
    return jsonify(post.to_json())
