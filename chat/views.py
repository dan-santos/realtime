from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
import json

class IndexView(TemplateView):
    template_name = 'chat/index.html'


class SalaView(TemplateView):
    template_name = 'chat/sala.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nome_sala_json'] = mark_safe(
            # gerando json com o nome da sala
            json.dumps(self.kwargs['nome_sala'])
        )
        return context 