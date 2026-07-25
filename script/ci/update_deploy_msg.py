import os
import secrets
from pathlib import Path

DEFAULT_RESULTS = 'No deployment results were captured.'


def write_deploy_message(github_env, results, delimiter_factory=secrets.token_hex):
    results = str(results or DEFAULT_RESULTS)
    result_lines = set(results.splitlines())

    while True:
        delimiter = f'branch_deploy_{delimiter_factory(16)}'
        if delimiter not in result_lines:
            break

    with Path(github_env).open('a', encoding='utf-8') as env_file:
        env_file.write(f'DEPLOY_MESSAGE<<{delimiter}\n')
        env_file.write(results)
        if not results.endswith('\n'):
            env_file.write('\n')
        env_file.write(f'{delimiter}\n')


def main():
    results = os.environ.get('MSG', DEFAULT_RESULTS)
    github_env = os.environ.get('GITHUB_ENV')

    if not github_env:
        raise RuntimeError('GITHUB_ENV is required')

    write_deploy_message(github_env, results)


if __name__ == '__main__':
    main()
