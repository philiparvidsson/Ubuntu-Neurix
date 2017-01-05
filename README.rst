What is Neurix?
###############

.. image:: img/screenshot0.png

Neurix is a Linux configuration script for Ubuntu GNOME 16.10.  It configures the system for optimal performance, installs some software and removes some bundled software.  It also sets up a beautiful theme, convenient keyboard shortcuts and more.

The installation is configurable to a great extent; you decide what parts of Neurix you want to install (for example, whether you want to use Google Chrome instead of Mozilla Firefox) and set up. You can easily modify the installation by deleting any nx-files associated with the components you want to exclude.

Installation
============

1. Clone this repository.
2. Chdir into the neurix directory.
3. Type :code:`./install` to install.

Alternatively, you can copy and paste the following line of text into a terminal to automatically clone the repository and run the installation:

:code:`cd ~ && sudo apt install git -qqy && git clone https://github.com/philiparvidsson/neurix.git && cd neurix && ./install`

*NOTE: You should not run the installation script with sudo—the script will automatically ask for sudo permissions and let you enter your password when requierd.*
