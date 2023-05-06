# bazel-python-coverage

## Requirements

- Bazel or Bazelisk
- genhtml
- Invoke (Python library)

## Coverage

```
$ inv coverage
```

## Invoke task list for development

```
$ invoke --list                                                                                                                   [aws:ads][k8s:ads-prd/ads-api]
Available tasks:

  clean            Clean the project
  coverage         Run coverage
  coverage-boto3   Run coverage for boto3
  run              Run the project
  setup            Setup the project
  test             Run tests
  test-boto3       Run tests for boto3
```
