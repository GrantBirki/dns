import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parent))

from update_deploy_msg import write_deploy_message


class WriteDeployMessageTest(unittest.TestCase):
    def test_writes_results_without_preprocessing_template_syntax(self):
        with TemporaryDirectory() as tmpdir:
            github_env = Path(tmpdir) / 'github-env'
            write_deploy_message(
                github_env,
                '{{ value }}\n{% if changed %}\n{# note #}',
                delimiter_factory=lambda _length: '0' * 32,
            )

            self.assertEqual(
                github_env.read_text(encoding='utf-8'),
                'DEPLOY_MESSAGE<<branch_deploy_00000000000000000000000000000000\n'
                '{{ value }}\n{% if changed %}\n{# note #}\n'
                'branch_deploy_00000000000000000000000000000000\n',
            )

    def test_retries_when_delimiter_collides_with_result_line(self):
        delimiters = iter(['a' * 32, 'b' * 32])
        with TemporaryDirectory() as tmpdir:
            github_env = Path(tmpdir) / 'github-env'
            write_deploy_message(
                github_env,
                'branch_deploy_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                delimiter_factory=lambda _length: next(delimiters),
            )

            self.assertIn(
                'DEPLOY_MESSAGE<<branch_deploy_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb',
                github_env.read_text(encoding='utf-8'),
            )


if __name__ == '__main__':
    unittest.main()
