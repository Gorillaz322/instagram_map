from flask.ext.login import current_user
from flask_views.base import TemplateView

from app import app


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
