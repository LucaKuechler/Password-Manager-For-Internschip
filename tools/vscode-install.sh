#!/bin/bash
code --install-extension aaron-bond.better-comments             # colered syntax for comments
code --install-extension ms-python.python                       # python
code --install-extension Equinusocio.vsc-material-theme-icons   # file icon theme
code --install-extension miguelsolorio.fluent-icons             # activity bar icon theme
code --install-extension njqdev.vscode-python-typehint          # python type hints for auto completion
code --install-extension wholroyd.jinja                         # jinja langserver
code --install-extension samuelcolvin.jinjaht                   # jinja better syntax highlighting
code --install-extension tabnine.tabnine-vscode                 # auto completion based on ai
code --install-extension cstrap.flask-snippets                  # flask code snippets
code --install-extension esbenp.prettier-vscode                 # prettier for web formatting
code --install-extension zhuangtongfa.material-theme            # color theme

if [ "$OSTYPE" == "msys" ] || [ "$OSTYPE" == "cygwin" ]; then 
    code --install-extension ms-vscode-remote.remote-wsl        # wls2 support
fi
