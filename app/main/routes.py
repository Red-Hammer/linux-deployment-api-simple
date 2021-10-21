from flask import render_template, jsonify
from app.main import bp



@bp.route('/')
@bp.route('/home')
def home():
    return render_template(
        'home.html',
        title='Home',
    )

@bp.route('/api', methods=['GET', 'POST'])
def api():
    response_dict = {'status': 'success', 'message': 'You pinged me!'}

    response = jsonify(response_dict)

    return response