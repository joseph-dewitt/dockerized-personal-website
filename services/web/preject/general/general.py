from flask import Blueprint, render_template


general_bp = Blueprint(
    'general_bp',
    __name__,
    template_folder = 'templates',
    static_folder = 'static',
    static_url_path = 'static'
)

@general_bp.route("/")
def index():
    return render_template('general/index.html')


@general_bp.route("/bad")
def bad():
    return render_template('general/bad.html')
