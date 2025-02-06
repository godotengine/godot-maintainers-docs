# Bug Triage Overview

## Basic Steps

Make sure the issue report is in the right place and that it is filled in properly. Any issue with complex steps, or that requires specific data such as a mesh,
should always have a minimal project attached to help testing.

If a bug is reported on the current development version (for example 4.4.beta1) as well as being reported as working in a past pre-release of the same version (for example 4.4.dev6),
or working on the latest stable version (for example 4.3.stable) it is a regression and should be tagged with the “regression tag”,
it should also be added to the “4.x Release Blockers” project.
If the author of the report only reports it as happening in a pre-release it is important to check if it is a regression or not, by testing on previous versions.

Try to tag an issue as specifically as possible, adding “needs testing” and “needs work” if necessary. Don't worry about misidentifying issues,
for example classifying something as a “bug” when it's actually an issue in the documentation or a missing feature.
Maintainers for each area will double checks reports when investigating, and will change tags as necessary.
It's more important to get an issue tagged correctly than getting it right from the start.

For pre-release versions it's critical to identify what change caused a specific bug, all such regressions should be bisected.

Once identified correctly it should be put on the relevant triage project(s) if appropriate. [See below](#team-triage-trackers) for a list of triage projects.
Functional enhancements shouldn't generally be put on the trackers (i.e. new features, not enhancements to documentation), some teams have dedicated trackers for enhancements,
but they aren't detailed here.

Try to always confirm issues while triaging. If the bug requires specific hardware, operating system, etc., that you don't have,
please drop it in the [#bugsquad](https://chat.godotengine.org/channel/bugsquad) channel and ask for someone to test it.

For some of the trackers there are additional details, like category, these should usually be filled in if possible, see below for details for each tracker (including the release blocker tracker).
If unsure what to assign leave it to the team to do. Only the fields specified below should be filled in by non-maintainers, and the status of the issue should be left in “For Team Assessment”.

New issues in the tracker should then be evaluated by maintainers (this can be done during meetings for example) and moved from “For Team Assessment”, and any details should be verified,
any incorrect information specified by the bugsquad should be fixed at this time.

## Release Blocker Tracking

Release blockers have their own project, [4.x Release Blockers](https://github.com/orgs/godotengine/projects/61). This tracks issues that need to be fixed before the next release.
These should be assigned a severity:
* *Not Critical*: For issues that do not have to be fixed before the next release, but would be good if we can to reduce newly introduced issues.
* *Bad*: For issues that should be fixed before the next release, but are less critical.
* *Very bad*: Like *Bad* but worse.
* *Release Blocker*: For issues that we absolutely need to fix before releasing. These include issues that severely hurt engine usability, breaks existing functionality, or are new features that
  don't work. In some cases less critical bugs can be considered a release blocker if it involves new API and delaying fixing the problem means restricting the solution due to
  compatibility issues.
* *Immediate Blocker*: For issues that should be solved as soon as possible, rather than before release. This includes issues that make the engine completely unusable, breaks the buildsystem,
  or are dangerous or damaging (such as security issues or privacy issues).

## Team Triage Trackers

### Animation

Tracked in:
* [Animation Team Issue Triage](https://github.com/orgs/godotengine/projects/74) (This tracker doesn't follow the pattern of the other ones)

RC channel:
* [#animation](https://chat.godotengine.org/channel/animation)

### Asset Pipeline

Tracked in:
* [Asset Pipeline Issue Triage](https://github.com/orgs/godotengine/projects/72) (This tracker doesn't follow the pattern of the other ones)

RC channel:
* [asset-pipeline](https://chat.godotengine.org/channel/asset-pipeline)

### Audio

Tracked in:
* [Audio Issue Triage](https://github.com/orgs/godotengine/projects/101)

RC channel:
* [#audio](https://chat.godotengine.org/channel/audio)

### Buildsystem

Tracked in:
* [Buildsystem Issue Triage](https://github.com/orgs/godotengine/projects/53)

RC channel:
* [#buildsystem](https://chat.godotengine.org/channel/buildsystem)

### Core

Tracked in:
* [Core Issue Triage](https://github.com/orgs/godotengine/projects/95)

RC channel:
* [#core](https://chat.godotengine.org/channel/core)

Categories:
* Threads
* Math
* String
* Input
* Resource
* Templates
* Debugger
* Variant
* Main
* Viewport
* IO
* Object/ClassDB

These categories largely match the specific folders the classes are in.

### GDExtension

Tracked in:
* [GDExtension Issue Triage](https://github.com/orgs/godotengine/projects/81/views/1)

RC Channel:
* [#gdextension](https://chat.godotengine.org/channel/gdextension)

### GDScript

Tracked in:
* [GDScript Issue Triage](https://github.com/orgs/godotengine/projects/79)

RC channel:
* [#gdscript](https://chat.godotengine.org/channel/gdscript)

### GUI

Tracked in:
* [GUI Issue Triage](https://github.com/orgs/godotengine/projects/100)

RC channel:
* [#gui](https://chat.godotengine.org/channel/gui)

### Navigation

Tracked in:
* [Navigation Issue Triage](https://github.com/orgs/godotengine/projects/103)

RC channel:
* [#navigation](https://chat.godotengine.org/channel/navigation)

### .NET / Mono

Tracked in:
* [.NET Issue Triage](https://github.com/orgs/godotengine/projects/83)

RC channel:
* [#dotnet](https://chat.godotengine.org/channel/dotnet)

### Network

Tracked in:
* [Network Issue Triage](https://github.com/orgs/godotengine/projects/96)

RC channel:
* [#networking](https://chat.godotengine.org/channel/networking)

### Physics

Tracked in:
* [Physics Issue Triage](https://github.com/orgs/godotengine/projects/102)

RC channel:
* [#physics](https://chat.godotengine.org/channel/physics)

### Platforms

Tracked in:
* [Platforms Issue Triage](https://github.com/orgs/godotengine/projects/84)

RC channel:
* [#platforms](https://chat.godotengine.org/channel/platforms)

Has a "Platform" field for each platform type to fill in.

### Rendering

Tracked in:
* [Rendering Issue Triage](https://github.com/orgs/godotengine/projects/78)

RC channel:
* [#rendering](https://chat.godotengine.org/channel/rendering)

### XR

Tracked in:
* [XR Issue Triage](https://github.com/orgs/godotengine/projects/104)

RC channel:
* [#xr](https://chat.godotengine.org/channel/xr)
