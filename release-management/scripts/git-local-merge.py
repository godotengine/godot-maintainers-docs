#!/usr/bin/env python3
from __future__ import annotations

if __name__ != "__main__":
    raise ImportError(f"{__name__} should not be used as a module.")

import argparse
import json
import os
import shutil
import signal
import subprocess
import sys
from typing import NoReturn


class PullRequestInfo:
    id: int
    title: str = ""
    branch: str = ""

    def __init__(self, id: int) -> None:
        self.id = id
        out = subprocess.run(
            ["gh", "pr", "view", str(self.id), "--json", "author,title,headRefName"],
            capture_output=True,
            encoding="utf-8",
        )
        if out.returncode:
            return

        data = json.loads(out.stdout)
        self.title = data["title"]
        self.branch = f"{data['author']['login']}/{data['headRefName']}"

    def message(self) -> str:
        TEMPLATE = """\
Merge pull request #{id} from {branch}

{title}"""

        return TEMPLATE.format(id=self.id, branch=self.branch, title=self.title)


def main() -> NoReturn:
    parser = argparse.ArgumentParser(prog="git-local-merge", description="Locally merge multiple GitHub PRs.")
    parser.add_argument("ids", nargs="*", help="PR ids to merge.", type=int)
    parser.add_argument(
        "-f",
        "--file",
        help="Path to a file containing PR ids.",
        type=argparse.FileType(encoding="utf-8"),
    )
    args = parser.parse_args()

    ids: set[int] = set(args.ids)
    if args.file:
        try:
            ids.update(int(id) for id in args.file.read().split())
        except ValueError:
            parser.error("File contained invalid int values.")
    if not ids:
        parser.error("No ids provided.")

    if subprocess.run(["git", "checkout"], stdout=subprocess.PIPE).returncode != 0:
        sys.exit(1)

    BASE_BRANCH = subprocess.run(
        ["git", "branch", "--show-current"], capture_output=True, encoding="utf-8"
    ).stdout.strip()

    if not shutil.which("gh"):
        print(
            "GitHub CLI not detected! Download the CLI tool to use this script:\n"
            + "https://github.com/cli/cli#installation",
            file=sys.stderr,
        )
        sys.exit(1)

    # GitHub CLI relies on a default remote repository being set.
    out = subprocess.run(["gh", "repo", "set-default", "--view"], capture_output=True)
    if out.stderr:
        subprocess.run(["gh", "repo", "set-default"])
        out = subprocess.run(["gh", "repo", "set-default", "--view"], capture_output=True)
        if out.stderr:
            print("Failed to setup default remote repository!", file=sys.stderr)
            sys.exit(1)

    failed: set[int] = set()
    prs: list[PullRequestInfo] = []

    for id in ids:
        pr = PullRequestInfo(id)
        if pr.title:
            prs.append(pr)
        else:
            print(f"id #{id} does not correspond to a PR!", file=sys.stderr)
            failed.add(id)

    for pr in prs:
        subprocess.run(["gh", "pr", "checkout", str(pr.id), "--branch", pr.branch, "--force"])
    subprocess.run(["git", "checkout", BASE_BRANCH])

    for pr in prs:
        out = subprocess.run(["git", "merge", "--no-ff", pr.branch, "-m", pr.message()])
        if out.returncode != 0:
            subprocess.run(["git", "merge", "--abort"])
            failed.add(pr.id)
        subprocess.run(["git", "branch", "--delete", "--force", pr.branch])

    if len(failed):
        print(f"Failed to merge: {failed}.")
    sys.exit(len(failed))


try:
    main()
except KeyboardInterrupt:
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    os.kill(os.getpid(), signal.SIGINT)
