from flask import url_for, request, redirect, session
from flask_views.base import TemplateView

from app import app, instagram


class MainPage(TemplateView):
    template_name = "MainPage.html"

    def get(self):
        # TODO: add redirect after sign up implementation
        # if current_user.is_authenticated:
        #     return redirect()

        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)

        # logic will be added later

        return context

app.add_url_rule('/', view_func=MainPage.as_view('main_page'))


class ProfilePage(TemplateView):
    template_name = "ProfilePage.html"

    def get(self):
        if not get_inst_token():
            return redirect('/sign-in')

        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(ProfilePage, self).get_context_data(**kwargs)
        context.update({'session': session})

        # logic will be added later

        return context

app.add_url_rule('/profile', view_func=ProfilePage.as_view('profile'))


@app.route('/sign-in')
def login():
    return instagram.authorize(callback=url_for('oauth_authorized', _external=True, next='/profile'))


@app.route('/oauth-authorized')
@instagram.authorized_handler
def oauth_authorized(resp):
    next_url = request.args.get('next') or url_for('profile')
    if resp is None:
        return redirect('sign-in')

    session['instagram_token'] = resp['access_token']
    session['user'] = resp['user']

    return redirect(next_url)


@instagram.tokengetter
def get_inst_token():
    return session.get('instagram_token')

