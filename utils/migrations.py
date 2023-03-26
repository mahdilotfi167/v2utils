from django.db import migrations


class AddExtraSetting(migrations.RunPython):
    def __init__(self, name, type, *, value=None, description=None):
        def insert_entry(apps, schema_editor):
            Setting = apps.get_model('extra_settings', 'Setting')
            try:
                entry = Setting(name=name, value_type=type)
                if value is not None:
                    entry.value = value
                if description is not None:
                    entry.description = description
                entry.save()
            except Exception as e:
                raise RuntimeError('Cannot insert entry with name %s' % name) from e

        super().__init__(insert_entry)
