# Bug Triage Overview

## Triage Workflow

The first step of triage is to confirm that the issue is valid and filled in properly. This means that:
* It is a bug report, for the engine, and not a:
  - Feature proposal, belonging in [Godot Proposals](https://github.com/godotengine/godot-proposals)
  - Online documentation issue, belonging in [Godot Docs](https://github.com/godotengine/godot-docs) (this should generally be transferred)
  - A support question, these should be directed to other [community channels](https://godotengine.org/community/)
* Has all the required information:
  - The engine version tested with (with a specific version hash if not using an official release)
  - System information in most cases
  - Clear and detailed reproduction steps
  - A valid MRP if the steps are not trivial, or if the issue depends on scene setup or requires data, such as animations, meshes, etc., where getting
    the required setup to test are not trivial.

If the report is missing this information, ask for this information before proceeding. If the issue lacks critical information, or is written in a way that makes it
difficult to classify the issue, it should be tagged with “needs work”. Otherwise you can proceed and add some basic tags to the issue and add the “needs testing” tag.

Once the basic details of the issue have been verified the issue should be tagged with the appropriate tags.
See [bug triage guidelines](https://docs.godotengine.org/en/latest/contributing/workflow/bug_triage_guidelines.html) for details on these tags.

If the bug is reported on the current development version (i.e. the `master` branch, and any pre-releases such as `4.4.beta1`) it is important to verify if it also occurs
on a past stable release. If this information is missing from the report (i.e. the author only reports having tested development versions) please either ask the author to
test with a stable version or test the bug yourself. If it *doesn't* occur on a past release it is considered a regression and should be tagged with the “regression” label,
and should also be added to the “4.x Release Blockers” project. See [below](#release-blocker-tracking) for details.

For pre-release versions, it's critical to identify what change caused a specific bug. **All** such regressions should be bisected.
You can ask the issue author to follow the instructions in the
[Bisecting regressions](https://docs.godotengine.org/en/latest/contributing/workflow/bisecting_regressions.html) documentation.
If they are not able to (or the issue is critical and should be fixed as quickly as possible), then you can look into bisecting the issue yourself.

Once identified correctly it should be put on the relevant triage project(s) if appropriate. [See below](#team-triage-trackers) for a list of triage projects.
Functional enhancements shouldn't generally be put on the trackers (i.e. new features, not enhancements to documentation). Some teams have dedicated trackers for enhancements,
but they aren't detailed here.

Try to tag an issue as specifically as possible, adding “needs testing” and “needs work” if necessary. Don't worry about misidentifying issues,
for example classifying something as a “bug” when it's actually an issue in the documentation or a missing feature.
Maintainers for each area will double checks reports when investigating, and will change tags as necessary.
It's more important to get an issue tagged correctly than getting it right from the start.

### Testing an MRP

A valid MRP is a *minimal* project that reproduces a bug. This means that it is no larger than it needs to be, it also has to be a project, not an exported executable.
Do _not_ run executable projects added to a bug report, they are not valid MRPs as an MRP needs to be something that can be evaluated in detail, and be tweaked if needed,
and more importantly they are untrusted files.

Some bugs can be hard to verify when testing different versions (for example when bisecting) due to generated data. In this case, you might need to delete the `.godot` folder
or any user data related to the project. See [data paths](https://docs.godotengine.org/en/latest/tutorials/io/data_paths.html) for details on where these files are stored.

<!-- TODO? -->

If you are unable to reproduce the bug, and the author reports using a different operating system, or using different hardware 
(for example a different GPU manufacturer or family), please drop it in the [#bugsquad](https://chat.godotengine.org/channel/bugsquad) channel and ask for someone to test it.

## Team Workflow

When issues arrive in the triage projects they will have the “For Team Assessment” status. These issues should be treated as being unverified, and should be verified before
moving the issue to another status. This can be done as part of regular team meetings, or be handled by individual maintainers processing these, as long as the assessment made
by triagers is verified.

As part of this verification, other information should be updated if needed. For example, if the issue was added to multiple trackers because it was unclear what area it
belongs to, it should be removed from the unrelated tracker(s). This is also a good time to verify any regression severity or assign one if it is unassessed.

If the report is missing information, please ask the author for more details. If the task of handling testing updated information can be handled by the bugsquad, this task
can be handed over to them for verification: for example, testing an updated MRP provided by the author.

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

### Editor

Tracked in:
* [Editor Issue Triage](https://github.com/orgs/godotengine/projects/111)

RC channel:
* [#editor](https://chat.godotengine.org/channel/editor)

Categories:
* Docks:
  Editor docks (Inspector, Scene etc.) and dock layout
* 2D Editor:
  2D editor and related features, including GUI
* 3D Editor:
  3D editor and related features, including gizmos
* Shader Editor:
  Includes visual shaders
* Script Editor:
  Text editing (Scripts, TextFiles)
* Animation:
  `AnimationPlayer`, `AnimationTree` and animation-related systems
* Tiles:
  `TileMapLayer` and `TileSet` editors
* Project Export:
  Export dialog, export process and related features
* Project Manager:
  Project Manager and its components
* Plugins:
  Related to editor plugins, both user (e.g. `EditorInterface`) and native (any plugin not covered by other categories)
* Game View:
  Issues relating to the embedded game view
* AssetLib:
  AssetLib integration with the editor
* Debugger:
  Related to editor/runtime interactions
* Systems:
  Misc editor systems not covered by other categories
* Usability:
  User experience, editor visuals (themes etc.)
* File System:
  Related to `EditorFileSystem`, cache, UIDs, previews
* Asset Pipeline:
  Asset import, models and materials, imported animations

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
* [.NET Issue Triage](https://github.com/orgs/godotengine/projects/83) (Internal tracker)

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
