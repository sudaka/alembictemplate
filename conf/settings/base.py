'''Loading settings to project'''
from src.libsettings import Jsettings

# dev settings
mysettings = Jsettings(settingsfname='conf/settings/settings.json',
                       schemafname='conf/settings/schema.json')
mysettings.load_settings()
