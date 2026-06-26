import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from update_deploy_msg import render_deploy_message


class RenderDeployMessageTest(unittest.TestCase):
    def test_renders_results_without_consuming_branch_deploy_template(self):
        template_path = Path(__file__).resolve().parents[2] / '.github' / 'deployment_message.md'
        rendered = render_deploy_message(
            template_path.read_text(encoding='utf-8'),
            'planned changes',
        )

        self.assertNotIn('{% raw %}', rendered)
        self.assertNotIn('{% endraw %}', rendered)
        self.assertNotIn('[[ results ]]', rendered)
        self.assertIn('planned changes', rendered)
        self.assertIn('{{ actor }}', rendered)
        self.assertIn('{{ ref }}', rendered)
        self.assertIn('{{ environment }}', rendered)

    def test_escapes_nunjucks_opening_delimiters_in_results(self):
        rendered = render_deploy_message(
            '[[ results ]]',
            '{{ value }}\n{% if changed %}\n{# note #}',
        )

        self.assertIn('{ { value }}', rendered)
        self.assertIn('{ % if changed %}', rendered)
        self.assertIn('{ # note #}', rendered)
        self.assertNotIn('{{ value }}', rendered)
        self.assertNotIn('{% if changed %}', rendered)
        self.assertNotIn('{# note #}', rendered)


if __name__ == '__main__':
    unittest.main()
