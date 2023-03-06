"Forms"
from django.forms import ModelForm
from backoffice.models import MuseumTopic

class TopicForm(ModelForm):
    class Meta:
        model = MuseumTopic
        fields = '__all__'
        # fields = ['Titel','Manufacturer','Factual_text','Description',
        #          'Long_Description', 'Picture1_path','Picture2_path','Picture3_path']
