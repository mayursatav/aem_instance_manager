# AEM Instance Manager

**AEM Instance Manager** is a Python-based CLI tool to help developers manage local Adobe Experience Manager (AEM) instances more easily. It allows you to start, stop, and monitor multiple AEM author/publish instances from a simple interface.

---

## 📦 Installation

First, clone the repository and navigate to the project directory:

```bash
pip3 install aem-instance-manager
```
## 📋 Dependencies
```
pandas
tkinter for GUI (usually comes with Python)
```

## 📂 Required AEM Project Structure
```
└── project1
    ├── author
    │   └── aem-author-p4502.jar
    ├── publish
    │   └── aem-publish-p4502.jar
    └── src
```

## Required Inputs

To function properly, aem-instance-manager needs the following input details:

| Input | Info |
| ------ | ------ |
| Project Name | You project name (e.g Project 1) |
| Author Port | any author port number (e.g 4502) |
| Publish Port |  any publish port number (e.g 4503) |
| Folder Path | project folder path (e.g. /Users/mayur/Desktop/aem/project1) |

## 🚀 Usage

In Mac

Setup for macOS Terminal
```
export PATH="$HOME/Library/Python/3.13/bin:$PATH"
export PATH="/Library/Frameworks/Python.framework/Versions/3.13/bin:$PATH"
```
Then apply the changes:
```
source ~/.zshrc
```
Once installed, you can launch the CLI tool with:
```
aem-instance-manager
```
Or directly using Python:
```
python3 -m aem_instance_manager.run
```

![aem-instance-manager gui window screenshot](https://raw.githubusercontent.com/mayursatav/aem_instance_manager/refs/heads/main/aem-instance-manager-screenshot.png)

## 🧠 Features
- 🧾 Manage multiple AEM instances (Author / Publish)
- ✅ Start/Stop/Restart selected instances
- 📊 Track status using pandas DataFrames
- 🖥️ Simple terminal interface (with optional GUI using tkinter)

## 📝 License
```
MIT License
```

## Created By
Mayur Satav
[www.mayursatav.in](https://www.mayursatav.in/) 
