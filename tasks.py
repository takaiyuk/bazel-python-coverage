from pathlib import Path

from invoke import task


def project_root(ctx):
    """Util function to change directory to the project root

    Args:
        ctx:
    """
    return ctx.cd(Path(__file__).parent.parent)

@task
def setup(ctx):
    """Setup the project

    Args:
        ctx:
    """
    with project_root(ctx):
        ctx.run(
            """
            pip install -r python/requirements.txt
            pip freeze > python/requirements_lock.txt
            """
        )

# @task
# def coverage(ctx):
#     """Run coverage
    
#     Args:
#         ctx:
#     """
#     with project_root(ctx):
#         ctx.run(
#             """
#             coverage run -m pytest python/tests
#             coverage report -m
#             coverage html
#             """
#         )

@task
def run(ctx):
    """Run the project
    
    Args:
        ctx:
    """
    with project_root(ctx):
        ctx.run(
            """
            bazelisk run //python:binary
            """
        )

@task
def test(ctx):
    """Run tests
    
    Args:
        ctx:
    """
    with project_root(ctx):
        ctx.run(
            """
            bazelisk test //python:test
            """
        )

@task
def coverage(ctx):
    """Run coverage

    Args:
        ctx:
    """
    with project_root(ctx):
        ctx.run(
            """
            bazelisk coverage //python:test --combined_report=lcov
            genhtml --output bazel-coverage bazel-out/_coverage/_coverage_report.dat
            """
        )

@task
def test_boto3(ctx):
    """Run tests for boto3
    
    Args:
        ctx:
    """
    with project_root(ctx):
        ctx.run(
            """
            bazelisk test //python:test_boto3
            """
        )

@task
def coverage_boto3(ctx):
    """Run coverage for boto3

    Args:
        ctx:
    """
    with project_root(ctx):
        ctx.run(
            """
            bazelisk coverage //python:test_boto3 --combined_report=lcov
            genhtml --output bazel-coverage bazel-out/_coverage/_coverage_report.dat
            """
        )

@task
def clean(ctx):
    """Clean the project
    
    Args:
        ctx:
    """
    with project_root(ctx):
        ctx.run(
            """
            rm -rf .pytest_cache/
            rm -rf .coverage htmlcov/ bazel-coverage/
            """
        )
