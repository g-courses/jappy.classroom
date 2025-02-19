{
    "dockerComposeFile": "docker-compose.yml",
    "service": "jappy",
    "remoteUser": "devuser",
    
    // Permite sobrescribir el ENTRYPOINT
    "overrideCommand": false, 
    "command":"/usr/bin/supervisord -c /etc/supervisord.conf",
  
    "workspaceMount": "source=${localWorkspaceFolder},target=/home/devuser/workspace/${localWorkspaceFolderBasename},type=bind,consistency=consistent",
    "workspaceFolder": "/home/devuser/workspace",

    // Features to add to the dev container. More info: https://containers.dev/features.
    // "features": {},

    // Use 'forwardPorts' to make a list of ports inside the container available locally.
    "forwardPorts": [8888],
    "portsAttributes": {
        "8888": {
          "label": "Jupyter server"
        }
    },
    
    "customizations": {
        "vscode": {
            "settings": {
                "files.exclude": {
                    "**/.ipy*": true,
                    "**/.Trash*": true,
                    "**/.DS_*": true
                },
                "extensions.ignoreRecommendations": true,
                //"editor.inlineSuggest.enabled": false,
                //"editor.inlineSuggest.showToolbar": "never",
                //"editor.quickSuggestions": {
                //  "other": "off"
                //},
                //"editor.suggest.selectionMode": "never",
                //"editor.suggest.showClasses": false,
                //"editor.suggest.showColors": false,
                //"editor.suggest.showConstants": false,
                //"editor.suggest.showConstructors": false,
                //"editor.suggest.showCustomcolors": false,
                //"editor.suggest.showEnumMembers": false,
                //"editor.suggest.showEnums": false,
                //"editor.suggest.showEvents": false,
                //"editor.suggest.showFields": false,
                //"editor.suggest.showIcons": false,
                //"editor.suggest.showInlineDetails": false,
                //"editor.suggest.showInterfaces": false,
                //"editor.suggest.showIssues": false,
                //"editor.suggest.showKeywords": false,
                //"editor.suggest.showUnits": false,
                //"editor.suggest.showTypeParameters": false,
                //"editor.suggest.showUsers": false,
                //"editor.suggest.showValues": false,
                //"editor.suggest.showVariables": false,
                //"editor.suggest.showWords": false,
                "editor.tabSize": 4,
                "editor.insertSpaces": true,
                "problems.visibility": false,
                "doxygen_runner.view_after_generate": false
            },
            "extensions": [
                // Incluidas en la imagen                    
                "ms-python.python",
                "ms-python.vscode-pylance",
                "ms-python.debugpy",
                "ms-toolsai.jupyter",
                "ms-toolsai.vscode-jupyter-cell-tags",
                "ms-toolsai.vscode-jupyter-slideshow",
                "ms-toolsai.jupyter-keymap",
                "ms-toolsai.jupyter-renderers",
                "ms-vscode.cpptools-extension-pack",
                "lfm.vscode-makefile-term",
                "ms-vscode.makefile-tools",
                "ms-vscode.cpptools",
                "ms-vscode.cpptools-themes",
                "ms-vscode.cmake-tools",
                "twxs.cmake",
                "redhat.java",
                "ms-toolsai.datawrangler",
                "bbenoist.Doxygen",
                "cschlosser.doxdocgen",
                "betwo.vscode-doxygen-runner",
                "hediet.vscode-drawio",
                "bierner.markdown-mermaid",
                "bpruitt-goddard.mermaid-markdown-syntax-highlighting",
                "tomoyukim.vscode-mermaid-editor",
                "jebbs.plantuml"
                // Incluya las extensiones sus extensiones a continuacion
            ]
        }
    }
}

