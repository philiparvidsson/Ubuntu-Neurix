What is Neurix?
###############
.. image:: img/screenshot0.png

Neurix is a Linux configuration script for Ubuntu GNOME 16.10.  It configures the system for optimal performance, installs some software and removes some bundled software.  It also sets up a beautiful theme, convenient keyboard shortcuts and more.

The installation is configurable to a great extent; you decide what parts of Neurix you want to install (for example, whether you want to use Google Chrome instead of Mozilla Firefox) and set up. You can easily modify the installation by deleting any nx-files associated with the components you want to exclude.

Installation
============
1. Clone this repository.
2. Chdir into the Neurix directory.
3. Type :code:`./install` to install.

Alternatively, you can copy and paste the following line of text into a terminal to automatically clone the repository and run the installation:

:code:`cd ~ && sudo apt install git -qqy && git clone https://github.com/philiparvidsson/Ubuntu-Neurix.git && cd Ubuntu-Neurix && ./install`

*NOTE: You should not run the installation script with sudo—the script will automatically ask for sudo permissions and let you enter your password when required.*

Configuration
=======

Neurix is configurable to a great extent. Below are lists of software etc., configured by Neurix during installation.  You can, of course, easily change the installation by modifying the relevant nx-files.  If you want to remove a feature from the installation, simply delete the associated nx-files.

Other than what is listed below, Neurix also installs and sets up a theme for you, providing a coherent and elegant look.  Also, certain services are disabled or reconfigured for a more optimized experience.

Software
--------
Neurix installs the following software:

+---------------------------+----------+
| Name                      | Optional |
+===========================+==========+
| Emacs                     | X        |
+---------------------------+----------+
| GIMP                      | X        |
+---------------------------+----------+
| Google Chrome             | X        |
+---------------------------+----------+
| Plex Media Server         | X        |
+---------------------------+----------+
| Python                    |          |
+---------------------------+----------+
| Slack                     | X        |
+---------------------------+----------+
| TeX Live                  | X        |
+---------------------------+----------+
| Telegram                  | X        |
+---------------------------+----------+
| Transmission              | X        |
+---------------------------+----------+
| git                       |          |
+---------------------------+----------+
| make                      |          |
+---------------------------+----------+
| redshift                  | X        |
+---------------------------+----------+
| tlp                       |          |
+---------------------------+----------+
| ttf-mscorefonts-installer |          |
+---------------------------+----------+
| unrar                     |          |
+---------------------------+----------+

Neurix *removes* the following software:

+---------------------------+----------+
| Name                      | Optional |
+===========================+==========+
| Bundled games             |          |
+---------------------------+----------+
| Firefox                   | X        |
+---------------------------+----------+
| LibreOffice               | X        |
+---------------------------+----------+

Keyboard shortcuts
------------------
Neurix provides the following keyboard shortcuts:

+------------------------------+---------------+
| Shortcut                     | Command       |
+==============================+===============+
| <Primary>odiaeresis (ctrl+ö) | Show terminal |
+------------------------------+---------------+
| <Super>e (win+e)             | Open Nautilus |
+------------------------------+---------------+

Aliases
-------
Neurix provides the following aliases/commands:

+-------------------------+----------------------------------------+
| Alias                   | Command                                |
+=========================+========================================+
| :code:`e.`              | Open Nautilus in current directory     |
+-------------------------+----------------------------------------+
| :code:`plex-add-media`  | Add media to Plex Media Server library |
+-------------------------+----------------------------------------+
| :code:`plex-start`      | Start Plex Media Server                |
+-------------------------+----------------------------------------+
| :code:`plex-stop`       | Stop Plex Media Server                 |
+-------------------------+----------------------------------------+
| :code:`sloc`            | Counts source lines of code            |
+-------------------------+----------------------------------------+
| :code:`stt`             | Set terminal title                     |
+-------------------------+----------------------------------------+
| :code:`sysupd`          | Upgrade system                         |
+-------------------------+----------------------------------------+

Details
-----------

Neurix is carefully configured to provide a pleasant and coherent experience. Below is information on certain intricacies of the configuration.

**Google Chrome**

Google Chrome automatically installs three extensions upon first start: `LastPass <https://chrome.google.com/webstore/detail/lastpass-free-password-ma/hdokiejnpimakedhajhdlcegeplioahd>`_, `uBlock Origin <https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm>`_ and `Vimium <https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb>`_.

**redshift**

If installed, redshift is set up to use geolocation to get your GPS coordinates for accurate tinting of the screen. It uses 3400K color temp. during day and 2700K during night.

**Transmission**

If Transmission is installed, it is set up to automatically add and start torrents from the Downloads directory.  When a download is completed, and if Plex Media Server is installed, the torrent (movie or TV show) is automatically extracted and copied to the Plex Media Server library at :code:`/var/lib/plexmediaserver/Library`.
