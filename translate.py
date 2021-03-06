
import sys
from workflow import Workflow, ICON_WEB, web

API_KEY = 'trnsl.1.1.20150814T095541Z.7d37d9cfc8192d15.daf236523ceddc759bbd2bf347426ec656e73391'

def main(wf):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    # RU
    params = dict(key=API_KEY, lang='ru', text=wf.args[0])
    r = web.get(url, params)

    r.raise_for_status()

    result = r.json()

    value = result['text'][0]
    wf.add_item(title=value, arg=value, subtitle='-> RU', valid=True)

    # EN
    params = dict(key=API_KEY, lang='en', text=wf.args[0])
    r = web.get(url, params)

    r.raise_for_status()

    result = r.json()

    value = result['text'][0]
    wf.add_item(title=value, arg=value, subtitle='-> EN', valid=True)

    wf.send_feedback()

if __name__ == u"__main__":
    update_settings = {
        'github_slug': 'Pr0Ger/alfred_yandex.translate',
    }
    wf = Workflow(update_settings = update_settings)
    sys.exit(wf.run(main))
