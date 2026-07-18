"""检查成员学习记录和个人练习的目录命名。"""

import re
import subprocess
import sys


PROJECT_ID_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")
GITHUB_ID_PATTERN = re.compile(
    r"^(?=.{1,39}$)[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?$"
)
WEEK_DIRECTORY_PATTERN = re.compile(r"^week-(?:0[1-9]|[1-9][0-9])$")
WEEK_FILE_PATTERN = re.compile(r"^week-(?:0[1-9]|[1-9][0-9])\.md$")

ALLOWED_ROOT_FILES = {
    "learning-records/README.md",
    "exercises/README.md",
}


def tracked_paths() -> list[str]:
    """读取当前 Git 工作树中已跟踪及未忽略的未跟踪文件路径。"""
    try:
        result = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            check=True,
            stdout=subprocess.PIPE,
        )
    except (OSError, subprocess.CalledProcessError) as error:
        raise RuntimeError(
            "无法读取 Git 文件列表，请确认当前目录是 Git 仓库"
        ) from error

    return [
        raw_path.decode("utf-8") for raw_path in result.stdout.split(b"\0") if raw_path
    ]


def check_project_and_user(project_id: str, github_id: str) -> list[str]:
    """检查项目 ID 和 GitHub 用户名目录。"""
    errors = []
    if not PROJECT_ID_PATTERN.fullmatch(project_id):
        errors.append("项目 ID 必须使用小写英文字母、数字或下划线，且以字母开头")
    if not GITHUB_ID_PATTERN.fullmatch(github_id):
        errors.append("成员目录必须使用 GitHub 用户名，只允许字母、数字和非首尾连字符")
    return errors


def check_learning_record(parts: list[str]) -> list[str]:
    """检查 learning-records 下的文件路径。"""
    expected = "learning-records/<project-id>/<github-id>/week-XX.md"
    if len(parts) != 4:
        return [f"学习记录路径应为 {expected}"]

    errors = check_project_and_user(parts[1], parts[2])
    if not WEEK_FILE_PATTERN.fullmatch(parts[3]):
        errors.append("学习记录文件名应为 week-01.md 到 week-99.md")
    return errors


def check_exercise(parts: list[str]) -> list[str]:
    """检查 exercises 下的文件路径。"""
    expected = "exercises/<project-id>/<github-id>/week-XX/<文件>"
    if len(parts) < 5:
        return [f"个人练习路径应为 {expected}"]

    errors = check_project_and_user(parts[1], parts[2])
    if not WEEK_DIRECTORY_PATTERN.fullmatch(parts[3]):
        errors.append("个人练习周次目录应为 week-01 到 week-99")
    return errors


def check_path(path: str) -> list[str]:
    """检查一个仓库相对路径，不处理规则范围外的文件。"""
    normalized = path.replace("\\", "/").removeprefix("./")
    if normalized in ALLOWED_ROOT_FILES:
        return []

    parts = normalized.split("/")
    if parts[0] == "learning-records":
        return check_learning_record(parts)
    if parts[0] == "exercises":
        return check_exercise(parts)
    return []


def main(arguments: list[str]) -> int:
    """检查指定路径；未指定时检查当前 Git 文件列表。"""
    try:
        paths = arguments or tracked_paths()
    except RuntimeError as error:
        print(f"命名规范检查无法运行：{error}", file=sys.stderr)
        return 2

    managed_paths = [
        path
        for path in paths
        if path.replace("\\", "/").startswith(("learning-records/", "exercises/"))
    ]
    failures = [(path, error) for path in managed_paths for error in check_path(path)]

    if failures:
        print("命名规范检查失败：", file=sys.stderr)
        for path, error in failures:
            print(f"- {path}\n  {error}", file=sys.stderr)
        return 1

    print(f"命名规范检查通过：已检查 {len(managed_paths)} 个受管文件。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
