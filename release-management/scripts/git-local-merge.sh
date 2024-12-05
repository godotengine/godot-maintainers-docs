#!/bin/bash

PR=$1
VIEW=$(gh pr view $PR)
AUTHOR=$(echo "$VIEW" | grep -m 1 "author:" | sed "s/^author:[[:space:]]*//")
TITLE=$(echo "$VIEW" | grep -m 1 "title:" | sed "s/^title:[[:space:]]*//")

BASE_BRANCH=$(git branch --show-current)

gh pr checkout $PR -f

PR_BRANCH=$(git branch --show-current)
MESSAGE_TAG="$AUTHOR/$PR_BRANCH"
if [ "$PR_BRANCH" == "$AUTHOR/$BASE_BRANCH" ]; then # master
  MESSAGE_TAG="$PR_BRANCH"
fi

MESSAGE="Merge pull request #$PR from $MESSAGE_TAG

$TITLE"
echo -e "Merging PR with message:\n$MESSAGE"

git checkout $BASE_BRANCH

git merge --no-ff $PR_BRANCH -m "$MESSAGE"
git branch -d $PR_BRANCH
