#!/usr/bin/env python3
from __future__ import annotations

if __name__ != "__main__":
    raise ImportError(f"{__name__} should not be used as a module.")

import argparse
import json
import shutil
import subprocess
import sys
from typing import NoReturn


class PullRequestInfo:
    id: int
    title: str = ""
    branch: str = ""
    commits: list[str] = []

    def __init__(self, id: int) -> None:
        self.id = id
        out = subprocess.run(
            ["gh", "pr", "view", str(self.id), "--json", "author,title,headRefName,commits"],
            capture_output=True,
            encoding="utf-8",
        )
        if out.returncode:
            return

        data = json.loads(out.stdout)
        self.title = data["title"]
        self.branch = f"{data['author']['login']}/{data['headRefName']}"
        self.commits = [commit["oid"] for commit in data["commits"]]

    def message(self) -> str:
        TEMPLATE = """\
Merge pull request #{id} from {branch}

{title}"""

        return TEMPLATE.format(id=self.id, branch=self.branch, title=self.title)


def main() -> NoReturn:
    parser = argparse.ArgumentParser(prog="git-local-merge", description="Locally merge multiple GitHub PRs.")
    parser.add_argument("ids", nargs="*", help="PR ids to merge.", type=int)
    parser.add_argument("-f", "--file", help="Path to a file containing newline-separated PR ids.")
    parser.add_argument("-c", "--cherry-pick", action="store_true", help="Perform cherry-picks instead of merges.")
    args = parser.parse_args()

    ids: list[int] = []
    for id in args.ids:
        if id in ids:
            parser.error(f'Duplicate id passed in command line: "{id}".')
        ids.append(id)
    if args.file:
        with open(args.file, encoding="utf-8", newline="\n") as file:
            for line in file:
                if not line:
                    continue
                try:
                    id = int(line)
                except ValueError:
                    parser.error(f'Invalid int passed in file: "{line}"')
                if id in ids:
                    parser.error(f'Duplicate id passed in file: "{id}".')
                ids.append(id)
    if not ids:
        parser.error("No ids provided.")

    if subprocess.run(["git", "checkout"], stdout=subprocess.PIPE).returncode != 0:
        sys.exit(1)

    BASE_BRANCH = subprocess.run(
        ["git", "branch", "--show-current"], capture_output=True, encoding="utf-8"
    ).stdout.strip()
    BASE_SHA = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, encoding="utf-8").stdout.strip()

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

    failed: list[int] = []
    prs: list[PullRequestInfo] = []

    for id in ids:
        pr = PullRequestInfo(id)
        if pr.title:
            prs.append(pr)
        else:
            print(f"id #{id} does not correspond to a PR!", file=sys.stderr)
            failed.append(id)

    if args.cherry_pick:
        for idx, pr in enumerate(prs, 1):
            print()
            print(f"[{idx:3d}/{len(prs):3d}] {pr.id}: {pr.title}")
            out = subprocess.run(["git", "cherry-pick", "-x", *pr.commits], capture_output=True, encoding="utf-8")
            loop = True
            while loop:
                if out.returncode == 0:  # Success.
                    print("Success!")
                    loop = False
                elif out.returncode == 1:  # Merge conflicts.
                    choice = input("Merge conflicts detected. Either resolve manually then continue (y) or skip (n): ").lower()
                    if choice in ['y', 'yes']:  # Attempt to resolve.
                        subprocess.run(["git", "add", "."], capture_output=True)
                        out = subprocess.run(
                            ["git", "cherry-pick", "--continue"], capture_output=True, encoding="utf-8"
                        )
                    elif choice in ['n', 'no']:  # Abort early.
                        loop = False
                        print("Aborting...")
                        subprocess.run(["git", "cherry-pick", "--abort"], capture_output=True)
                        failed.append(pr.id)
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
                else:  # Unrelated error.
                    loop = False
                    print(f"Cherry-pick failed from unrelated error: {out.stderr.strip()}")
                    subprocess.run(["git", "cherry-pick", "--abort"], capture_output=True)
                    failed.append(pr.id)

        if len(failed):
            print()
            print(f"Failed to cherry-pick: {failed}.")

        if not shutil.which("prek"):
            print()
            print("prek not detected! Skipping post-run validation...", file=sys.stderr)
        else:
            print()
            CURRENT_SHA = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, encoding="utf-8").stdout.strip()
            out = subprocess.run(["prek", "run", "--from-ref", BASE_SHA, "--to-ref", CURRENT_SHA, "--color=always"])
            if out.returncode != 0:
                sys.exit(out.returncode)

        sys.exit(len(failed))

    for pr in prs:
        print()
        subprocess.run(["gh", "pr", "checkout", str(pr.id), "--branch", pr.branch, "--force"])
    print()
    subprocess.run(["git", "checkout", BASE_BRANCH])

    for pr in prs:
        print()
        out = subprocess.run(["git", "merge", "--no-ff", pr.branch, "-m", pr.message()])
        if out.returncode != 0:
            subprocess.run(["git", "merge", "--abort"])
            failed.append(pr.id)
        subprocess.run(["git", "branch", "--delete", "--force", pr.branch])

    if len(failed):
        print()
        print(f"Failed to merge: {failed}.")

    if not shutil.which("prek"):
        print()
        print("prek not detected! Skipping post-run validation...", file=sys.stderr)
    else:
        print()
        CURRENT_SHA = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, encoding="utf-8").stdout.strip()
        out = subprocess.run(["prek", "run", "--from-ref", BASE_SHA, "--to-ref", CURRENT_SHA, "--color=always"])
        if out.returncode != 0:
            sys.exit(out.returncode)

    sys.exit(len(failed))


try:
    main()
except KeyboardInterrupt:
    import os
    import signal

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    os.kill(os.getpid(), signal.SIGINT)
