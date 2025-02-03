# Bug Triage Overview

## Basic Steps

Make sure the issue report is in the right place and that it is filled in properly. Any issue with complex steps, or that requires specific data such as a mesh,
should always have a minimal project attached to help testing.

If a bug is reported on the current development version (for example 4.4.beta1) as well as being reported as working in a past pre-release of the same version (for example 4.4.dev6),
or working on the latest stable version (for example 4.3.stable) it is a regression and should be tagged with the “regression tag”, it should also be added to the “4.x Release Blockers” project.
If the author of the report only reports it as happening in a pre-release it is important to check if it is a regression or not, by testing on previous versions.

Try to tag an issue as specifically as possible, adding “needs testing” and “needs work” if necessary. Don't worry about misidentifying issues,
for example classifying something as a “bug” when it's actually an issue in the documentation or a missing feature.
Maintainers for each area will double checks reports when investigating, and will change tags as necessary.
It's more important to get an issue tagged correctly than getting it right from the start.

For pre-release versions it's critical to identify what change caused a specific bug, all such regressions should be bisected.

Once identified correctly (and preferably once an issue has been confirmed, if possible, if the bug requires specific hardware, operating system, etc. that you don't have,
please drop it in the “bugsquad” channel and ask for someone to test it) it should be put on the relevant triage project(s) if appropriate. See below for a list of triage projects.
Functional enhancements shouldn't generally be put on the trackers (i.e. new features, not enhancements to documentation), some teams have dedicated trackers for enhancements,
but they aren't detailed here.

For some of the trackers there are additional details, like category, these should usually be filled in if possible, see below for details for each tracker (including the release blocker tracker).
If unsure what to assign leave it to the team to do. Only the fields specified below should be filled in by non-maintainers, and the status of the issue should be left in “For Team Assessment”.

New issues in the tracker should then be evaluated by maintainers (this can be done during meetings for example) and moved from “For Team Assessment”, and any details should be verified,
any incorrect information specified by the bugsquad should be fixed at this time.

## Relase Blocker Tracking

Release blockers have their own project, [`4.x Relase Blockers`](https://github.com/orgs/godotengine/projects/61). This tracks issues that need to be fixed before the next release.
These should be assigned a severity:
* *Not Critical*: For issues that do not have to be fixed before the next release, but would be good if we can to reduce newly introduced issues.
* *Bad*: For issues that should be fixed before the next release, but are less critical.
* *Very bad*: Like *Bad* but worse.
* *Release Blocker*: For issues that we absolutely need to fix before releasing. These include issues that severely hurt engine usability, breaks existing functionality, or are new features that
  don't work.
* *Immediate Blocker*: For issues that should be solved as soon as possible, rather than before release. This includes issues that make the engine completely unusable, breaks the buildsystem,
  or are dangerous or damaging (such as security issues or privacy issues).

## Team Triage Trackers

TBA
