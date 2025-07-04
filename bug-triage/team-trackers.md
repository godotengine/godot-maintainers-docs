## Team Triage Trackers

<!-- TODO: Add basic introduction -->

To search for PRs with requested reviews from a team, add `team-review-requested:` to the search bar, followed by the
team name (see below for each team, the link opens a search on GitHub). Note that this *doesn't* show PRs that have already
been reviewed by that team, any review comments at all, from any member of a specific team, will remove the request,
so this is not always helpful.

Some GitHub labels aren't neatly covered by trackers, below is a list of teams and labels that don't (currently) have trackers:
* 2D Nodes:
  - [godotengine/2d-nodes](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2F2d-nodes)
  - `topic:2d` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3A2d) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3A2d)
* 3D Nodes:
  - [godotengine/3d-nodes](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2F3d-nodes)
  - `topic:3d` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3A3d) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3A3d)
* Documentation:
  - [godotengine/documentation](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fdocumentation)
  - `documentation` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Adocumentation) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Adocumentation)
* Tests:
  - [godotengine/tests](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Ftests)
  - `topic:tests` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Atests) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Atests)

For more information about the different GitHub labels, please see the [labels documentation](https://docs.godotengine.org/en/latest/contributing/workflow/bug_triage_guidelines.html#labels).

<!-- TODO: Consider using a table -->

### Animation

Tracked in:
* [Animation Team Issue Triage](https://github.com/orgs/godotengine/projects/74) (This tracker doesn't follow the pattern of the other ones)

RC channel:
* [#animation](https://chat.godotengine.org/channel/animation)

GitHub team:
* [godotengine/animation](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fanimation)

GitHub label:
* `topic:animation` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aanimation) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aanimation)

### Asset Pipeline

Tracked in:
* [Asset Pipeline Issue Triage](https://github.com/orgs/godotengine/projects/72) (This tracker doesn't follow the pattern of the other ones)

RC channel:
* [asset-pipeline](https://chat.godotengine.org/channel/asset-pipeline)

GitHub team:
* [godotengine/import](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fimport)

GitHub label:
* `topic:import` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aimport) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aimport)

### Audio

Tracked in:
* [Audio Issue Triage](https://github.com/orgs/godotengine/projects/101)

RC channel:
* [#audio](https://chat.godotengine.org/channel/audio)

GitHub team:
* [godotengine/audio](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Faudio)

GitHub label:
* `topic:audio` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aaudio) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aaudio)

### Buildsystem

Tracked in:
* [Buildsystem Issue Triage](https://github.com/orgs/godotengine/projects/53)

RC channel:
* [#buildsystem](https://chat.godotengine.org/channel/buildsystem)

GitHub team:
* [godotengine/buildsystem](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fbuildsystem)

GitHub label:
* `topic:buildsystem` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Abuildsystem) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Abuildsystem)

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

GitHub team:
* [godotengine/core](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fcore)

GitHub labels:
* `topic:core` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Acore) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Acore)
* `topic:input` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Ainput) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Ainput)

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

GitHub teams:
* [godotengine/2d-editor](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2F2d-editor)
* [godotengine/3d-editor](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2F3d-editor)
* [godotengine/debugger](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fdebugger)
* [godotengine/docks](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fdocks)
* [godotengine/script-editor](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fscript-editor)
* [godotengine/usability](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fusability)

GitHub label:
* `topic:editor` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aeditor) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aeditor)
* `topic:export` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aexport) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aexport)
* `topic:i18n` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Ai18n) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Ai18n)
* `topic:plugin` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aplugin) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aplugin)

### GDExtension

Tracked in:
* [GDExtension Issue Triage](https://github.com/orgs/godotengine/projects/81/views/1)

RC Channel:
* [#gdextension](https://chat.godotengine.org/channel/gdextension)

GitHub team:
* [godotengine/gdextension](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fgdextension)

GitHub label:
* `topic:gdextension` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Agdextension) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Agdextension)

### GDScript

Tracked in:
* [GDScript Issue Triage](https://github.com/orgs/godotengine/projects/79)

RC channel:
* [#gdscript](https://chat.godotengine.org/channel/gdscript)

GitHub team:
* [godotengine/gdscript](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fgdscript)

GitHub label:
* `topic:gdscript` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Agdscript) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Agdscript)

### GUI

Tracked in:
* [GUI Issue Triage](https://github.com/orgs/godotengine/projects/100)

RC channel:
* [#gui](https://chat.godotengine.org/channel/gui)

GitHub team:
* [godotengine/gui-nodes](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fgui-nodes)

GitHub label:
* `topic:gui` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Agui) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Agui)

### Navigation

Tracked in:
* [Navigation Issue Triage](https://github.com/orgs/godotengine/projects/103)

RC channel:
* [#navigation](https://chat.godotengine.org/channel/navigation)

GitHub team:
* [godotengine/navigation](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fnavigation)

GitHub label:
* `topic:navigation` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Anavigation) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Anavigation)

### .NET / Mono

Tracked in:
* [.NET Issue Triage](https://github.com/orgs/godotengine/projects/83) (Internal tracker)

RC channel:
* [#dotnet](https://chat.godotengine.org/channel/dotnet)

GitHub team:
* [godotengine/dotnet](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fdotnet)

GitHub label:
* `topic:dotnet` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Adotnet) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Adotnet)

### Network

Tracked in:
* [Network Issue Triage](https://github.com/orgs/godotengine/projects/96)

RC channel:
* [#networking](https://chat.godotengine.org/channel/networking)

GitHub team:
* [godotengine/network](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fnetwork)

GitHub labels:
* `topic:multiplayer` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Amultiplayer) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Amultiplayer)
* `topic:network` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Anetwork) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Anetwork)

### Particles

Tracked in:
* [Particles Issue Triage](https://github.com/orgs/godotengine/projects/115)

RC channel:
* [#vfx-tech-art](https://chat.godotengine.org/channel/vfx-tech-art)

GitHub team:
* No dedicated team (currently)

GitHub label:
* `topic:particles` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aparticles) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aparticles)

### Physics

Tracked in:
* [Physics Issue Triage](https://github.com/orgs/godotengine/projects/102)

RC channel:
* [#physics](https://chat.godotengine.org/channel/physics)

GitHub team:
* [godotengine/physics](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fphysics)

GitHub label:
* `topic:physics` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aphysics) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aphysics)

### Platforms

Tracked in:
* [Platforms Issue Triage](https://github.com/orgs/godotengine/projects/84)

RC channel:
* [#platforms](https://chat.godotengine.org/channel/platforms)

Has a "Platform" field for each platform type to fill in.

GitHub teams:
* [godotengine/android](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fandroid)
* [godotengine/ios](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fios)
* [godotengine/linux-bsd](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Flinux-bsd)
* [godotengine/macos](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fmacos)
* [godotengine/uwp](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fuwp)
* [godotengine/web](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fweb)
* [godotengine/windows](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fwindows)

GitHub labels:
* `topic:porting` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Aporting) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Aporting)
* `platform:android` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Aandroid) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Aandroid)
* `platform:ios` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Aios) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Aios)
* `platform:linuxbsd` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Alinuxbsd) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Alinuxbsd)
* `platform:macos` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Amacos) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Amacos)
* `platform:uwp` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Auwp) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Auwp)
* `platform:web` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Aweb) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Aweb)
* `platform:windows` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Aplatform%3Awindows) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Aplatform%3Awindows)

### Rendering

Tracked in:
* [Rendering Issue Triage](https://github.com/orgs/godotengine/projects/78)

RC channel:
* [#rendering](https://chat.godotengine.org/channel/rendering)

GitHub teams:
* [godotengine/rendering](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Frendering)
* [godotengine/shaders](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fshaders)

GitHub labels:
* `topic:rendering` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Arendering) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Arendering)
* `topic:shaders` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Ashaders) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Ashaders)

### XR

Tracked in:
* [XR Issue Triage](https://github.com/orgs/godotengine/projects/104)

RC channel:
* [#xr](https://chat.godotengine.org/channel/xr)

GitHub team:
* [godotengine/xr](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+team-review-requested%3Agodotengine%2Fxr)

GitHub label:
* `topic:xr` [issues](https://github.com/godotengine/godot/issues?q=is%3Aissue%20state%3Aopen%20label%3Atopic%3Axr) [PRs](https://github.com/godotengine/godot/pulls?q=is%3Apr+is%3Aopen+label%3Atopic%3Axr)
