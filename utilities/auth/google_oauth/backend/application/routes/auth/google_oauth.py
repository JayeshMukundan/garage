from application.routes.auth import auth_fazade
from application.addons.auth import AuthAddon
from application.models import User
from application.constants import auth_constants
from flask import session, jsonify
from flask import url_for
from flask import redirect
from flask import flash
from flask import request
from flask_jwt_extended import create_access_token


google = AuthAddon.oauth.remote_app(
    'google',
    consumer_key=auth_constants.GOOGLE_CLIENT_ID,
    consumer_secret=auth_constants.GOOGLE_CLIENT_SECRET,
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)


@google.tokengetter
@staticmethod
def get_google_oauth_token():
    return session.get('google_token')


def register_google_oauth_routes(app):

    @app.route('/api/login/google')
    def login_google():
        return google.authorize(callback=url_for('authorized_google', _external=True))


    @app.route('/api/login/google/authorized')
    def authorized_google():
        response = google.authorized_response()
        if response is None or response.get('access_token') is None:
            flash('Access denied: reason={} error={}'.format(
                request.args['error_reason'],
                request.args['error_description']
            ), 'danger')
            return redirect(url_for('login'))

        google_user_info = google.get('userinfo', token=(response['access_token'], ''))
        email = google_user_info.data.get('email')

        user = User.query.filter_by(email=email).first()
        if not user:
            # Create a new user account if the email doesn't exist
            user = User(email=email, username=email)
            auth_fazade.register(user)
        else:
            auth_fazade.login(user)

        access_token = create_access_token(identity=user.id, additional_claims={'jti': user.id})
        redirect_url = f'/google-redirect?access_token={access_token}'

        flash('Logged in via Google successfully!', 'success')
        # Redirect the browser
        return redirect(redirect_url)