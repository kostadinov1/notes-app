from django import forms

from notes_app_exam.core.models import Note, Profile


class BootstrapFieldMixin():
    fields = {}

    def _init_readonly_field(self):
        for _, field in self.fields.items():

            if hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})

                if 'readonly' not in field.widget.attrs:
                    field.widget.attrs['disabled'] = True
                    field.widget.attrs['readonly'] += 'readonly'


class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class NoteEditForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class NoteDeleteForm(forms.ModelForm, BootstrapFieldMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_readonly_field()

    class Meta:
        model = Note
        fields = '__all__'

    def save(self, commit=True):
        self.instance.delte()
        return self.instance


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(forms.ModelForm, BootstrapFieldMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_readonly_field()
    class Meta:
        model = Profile
        fields = '__all__'
