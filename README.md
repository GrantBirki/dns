# dns 🌐

[![deploy](https://github.com/GrantBirki/dns/actions/workflows/deploy.yml/badge.svg)](https://github.com/GrantBirki/dns/actions/workflows/deploy.yml)
[![test](https://github.com/GrantBirki/dns/actions/workflows/test.yml/badge.svg)](https://github.com/GrantBirki/dns/actions/workflows/test.yml)
[![json-yaml-validate](https://github.com/GrantBirki/dns/actions/workflows/json-yaml-validate.yml/badge.svg)](https://github.com/GrantBirki/dns/actions/workflows/json-yaml-validate.yml)
[![Unlock On Merge](https://github.com/GrantBirki/dns/actions/workflows/unlock-on-merge.yml/badge.svg)](https://github.com/GrantBirki/dns/actions/workflows/unlock-on-merge.yml)

DNS management through [octodns](https://github.com/octodns/octodns).

![octopus](docs/assets/octopus.png)

## About 💡

This repository is used to manage DNS records for various domains. `octodns` is used to manage all DNS records through Infrastructure as Code (IaC) principles. The [github/branch-deploy](https://github.com/github/branch-deploy) is responsible for deploying changes to production.

## Development Workflow 🧰

This repository uses the "scripts to rule them all" pattern. Use the repo-owned `script/*` entrypoints instead of invoking `uv` or `octodns` commands directly.

Python is pinned in [`.python-version`](.python-version), and this repo expects a shim-based version manager such as `pyenv` to provide that exact interpreter:

```bash
pyenv install $(cat .python-version)
```

Once the pinned Python is installed, the standard workflows are:

```bash
script/bootstrap
script/test
script/plan
script/deploy
```

- `script/bootstrap` installs the pinned bootstrap tooling and project dependencies from the committed wheel cache.
- `script/test` verifies that `octodns` is installed correctly.
- `script/plan` runs a non-destructive `octodns-sync` plan against `production.yaml`.
- `script/deploy` runs `octodns-sync --doit` against `production.yaml`.

Dependency updates are intentionally explicit. Refresh the lockfiles and vendored wheels with:

```bash
script/vendor
```

The `vendor/cache` directory is committed to the repository so the project can bootstrap and run without contacting package indexes during normal development or CI.

## Deployment Process 🚀

This repository uses IssueOps via the [github/branch-deploy](https://github.com/github/branch-deploy) action to deploy changes to production. This ensure that all changes safely follow the [branch deploy model](https://blog.birki.io/posts/branch-deploy/).

Here is a trimmed down summary of the deployment process:

1. 🧪 Run a noop deployment with `.noop` as a comment on your PR
2. 👀 Observe the CI and `noop` output on your pull request to ensure it is passing and doing what it is supposed to do
3. ✔️ Obtain an approval/review on your pull request
4. 🚀 Branch deploy your pull request to production with `.deploy`

    > If anything goes wrong, rollback with `.deploy main`

5. 🎉 Merge!

> Note: you can use `.deploy | FORCE=true` to force deploy changes.

## License

The MIT license attached to this repository covers all code and documentation. Please see the [LICENSE](LICENSE) file for more information. It should be noted that the MIT license does not cover the DNS records themselves (or the associated domains), only the code, CI workflows, and documentation in this repository.
