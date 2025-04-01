# AEM Instance Manager #

I've created to streamline Adobe Experience Manager (AEM) project management. This tool is designed to simplify the management of different AEM instances, providing a user-friendly interface for handling various projects effortlessly.

In this tool, you can add your projects once, and whenever required, you can start and stop the author and publish instances. Additionally, it starts instances in the background to avoid cluttering your workspace with tons of terminal windows.

I created this tool for my personal use because I was facing a lot of issues maintaining and checking instances when working on multiple projects simultaneously. It also eliminates the need to navigate through folder structures to start old projects. Now, with just a few clicks, you can efficiently manage and monitor your AEM projects.

### Features ###

* Add new AEM projects with project name, author port, publish port, and folder path.
* Start and stop AEM project instances.
* Remove AEM projects from the manager.
* Display project details, including project name, author port, publish port, and status.

### Requirements ###

* Python 3.6 or higher
* Tkinter
* pandas - External
* subprocess
* os
* socket
* time

### Usage ###

1. Clone the repository:

```git clone https://github.com/yourusername/aem-projects-instance-manager.git```

2. Navigate to the project directory:

```cd aem-projects-instance-manager```

3. Install all the external dependencies:

```pip3 install pandas```

4. Run the application:

```python main.py``

### Instructions ###

1. Adding a Project:
	* Enter the project details (Project Name, Author Port, Publish Port, Folder Path).
	* Click the "Save" button to add the project.
2. Starting a Project:
	* Select a project from the dropdown menu.
	* Click the "Start" button to start the AEM project instance.
3. Stopping a Project:

### Who do I talk to? ###

	- Mayur Satav
	- www.mayursatav.in
