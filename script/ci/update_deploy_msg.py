import os
from pathlib import Path

TEMPLATE_FILE = Path('.github/deployment_message.md')
RAW_START = '{% raw %}'
RAW_END = '{% endraw %}'
RESULTS_PLACEHOLDER = '[[ results ]]'


def render_deploy_message(template_text, results):
    return (
        template_text
        .replace(RAW_START, '')
        .replace(RAW_END, '')
        .replace(RESULTS_PLACEHOLDER, str(results))
    )


def main():
    results = os.environ.get('MSG', False)
    rendered_template = render_deploy_message(
        TEMPLATE_FILE.read_text(encoding='utf-8'),
        results,
    )

    print(rendered_template)

    if os.environ.get('GITHUB_ACTIONS', False):
        TEMPLATE_FILE.write_text(rendered_template, encoding='utf-8')


if __name__ == '__main__':
    main()
