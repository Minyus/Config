# Set up an efficient scripting environment using Xonsh, Vim, VS Code, Pycharm

## Xonsh

- Install by `pip install xonsh` (or `apt` for Linux, `brew` for macOS)
- Auto-suggestions (similar to fish): `<right-arrow>` or `<Ctrl + e>` for macOS & Windows
- Tab-completion
- Automatic cd (enabled by `$AUTO_CD = True` in `.xonshrc`)
- Easy to customize prompt
- Add aliases (e.g. `aliases["dd"] = "cd .."`)
- Put https://github.com/Minyus/Config/blob/master/cpu_ml_spark_1907_py368/.xonshrc in ~ directory

## Vim plugin for VSCode

- `.vimrc` config support (since v1.12.0 (2019-12-01))
- Clarify the mode by chainging cursor to `|` in insert mode.
- Put https://github.com/Minyus/Config/blob/master/cpu_ml_spark_1907_py368/.vimrc in ~ directory

## Selected Vim commands

- Switch to insert mode:
  - `<i>`
  - `<Cmd + i>`: Move cursor to beginning of the line
  - `<Cmd + a>`: Move cursor to end of the line
- Switch to normal mode
  - `<Escape>`
- Cut
  - `<dd>`: delete the line
- Copy
  - `<yy>`: yank the line
- Paste
  - `<p>`
- Undo
  - `<u>`

## Other plugins for VSCode

- `Remote Development` (https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) for remote Python debugging through SSH
- `GitLens` (https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
- `Git Graph` (https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
- `Bracket Pair Colorizer 2` (https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2)
- `File Util` (https://marketplace.visualstudio.com/items?itemName=sleistner.vscode-fileutils)
  - "fileutils.delete.useTrash": true
- `YAML` (https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)

## Pycharm

- Git

## DroidVim

- Vim for Android
- https://play.google.com/store/apps/details?id=com.droidvim&hl=en_SG

<p align="center">
<img src="img/DroidVim_Screenshot.png">
</p>
