from flask import Blueprint, render_template, request, jsonify
from app.utils.rcviz import visualize

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        func_def = request.form.get('function_definition')
        func_call = request.form.get('function_call')
        try:
            dot_graph = visualize(func_def, func_call)
            return jsonify({'status': 'success', 'dot_graph': dot_graph})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})
    return render_template('index.html')