#!/bin/python3

import os
import sys
import subprocess

icon_root = '/usr/share/icons'
icon_folders = {'Faenza', 'Faenza-Dark', 'Faenza-Darker', 'Faenza-Darkest'}
icon_res = {'16', '22', '24', '32', '48', '64', '96', 'scalable'}
dry_run = False

mapping = {
	'apps/XXX/org.xfce.about': 'actions/XXX/help-about',
	'apps/XXX/org.xfce.appfinder': 'actions/XXX/edit-find',
	'apps/XXX/org.xfce.catfish': 'apps/XXX/catfish',
	'apps/XXX/org.xfce.Dictionary': 'apps/XXX/xfce4-dict',
	'apps/XXX/org.xfce.filemanager': 'apps/XXX/system-file-manager',
	'apps/XXX/org.xfce.genmon': 'apps/XXX/utilities-system-monitor',
	'apps/XXX/org.xfce.gigolo': 'places/XXX/gtk-network',
	'apps/XXX/org.xfce.mailreader': 'emblems/XXX/emblem-mail',
	'apps/XXX/org.xfce.mousepad': 'apps/XXX/accessories-text-editor',
	'apps/XXX/org.xfce.notification': 'status/XXX/xfce4-notifyd',
	'apps/XXX/org.xfce.panel.actions': 'actions/XXX/system-log-out',
	'apps/XXX/org.xfce.panel.applicationsmenu': 'places/XXX/start-here',
	'apps/XXX/org.xfce.panel.clock': 'apps/XXX/x-office-calendar',
	'apps/XXX/org.xfce.panel.directorymenu': 'places/XXX/folder',
	'apps/XXX/org.xfce.panel.launcher': 'mimetypes/XXX/application-x-executable',
	'apps/XXX/org.xfce.panel.pager': 'apps/XXX/xfce4-workspaces',
	'apps/XXX/org.xfce.panel.separator': 'actions/XXX/list-remove-symbolic',
	'apps/XXX/org.xfce.panel.showdesktop': 'places/XXX/user-desktop',
	'apps/XXX/org.xfce.panel.tasklist': 'apps/XXX/preferences-system-windows',
	'apps/XXX/org.xfce.panel.windowmenu': 'apps/XXX/preferences-system-windows',
	'apps/XXX/org.xfce.panel': 'apps/XXX/xfce4-panel',
	'apps/XXX/org.xfce.parole': 'apps/XXX/parole',
	'apps/XXX/org.xfce.powermanager': 'apps/XXX/gnome-power-manager',
	'apps/XXX/org.xfce.ristretto': 'apps/XXX/ristretto',
	'apps/XXX/org.xfce.ScreenSaver': 'apps/XXX/preferences-desktop-screensaver',
	'apps/XXX/org.xfce.screenshooter': 'apps/XXX/applets-screenshooter',
	'apps/XXX/org.xfce.session': 'apps/XXX/xfce4-session',
	'apps/XXX/org.xfce.settings.accessibility': 'apps/XXX/preferences-desktop-accessibility',
	'apps/XXX/org.xfce.settings.appearance': 'apps/XXX/preferences-desktop-theme',
	'apps/XXX/org.xfce.settings.color': 'apps/XXX/preferences-color',
	'apps/XXX/org.xfce.settings.default-applications': 'apps/XXX/preferences-desktop-default-applications',
	'apps/XXX/org.xfce.settings.display': 'devices/XXX/video-display',
	'apps/XXX/org.xfce.settings.editor': 'categories/XXX/preferences-system',
	'apps/XXX/org.xfce.settings.keyboard': 'apps/XXX/preferences-desktop-keyboard',
	'apps/XXX/org.xfce.settings.manager': 'categories/XXX/preferences-desktop',
	'apps/XXX/org.xfce.settings.mouse': 'apps/XXX/preferences-desktop-peripherals',
	'apps/XXX/org.xfce.taskmanager': 'apps/XXX/utilities-system-monitor',
	'apps/XXX/org.xfce.terminal-settings': 'apps/XXX/utilities-terminal',
	'apps/XXX/org.xfce.terminal': 'uapps/XXX/tilities-terminal',
	'apps/XXX/org.xfce.terminalemulator': 'apps/XXX/utilities-terminal',
	'apps/XXX/org.xfce.thunar': 'apps/XXX/Thunar',
	'apps/XXX/org.xfce.volman': 'devices/XXX/drive-removable-media',
	'apps/XXX/org.xfce.webbrowser': 'apps/XXX/browser',
	'apps/XXX/org.xfce.workspaces': 'apps/XXX/xfce4-workspaces',
	'apps/XXX/org.xfce.xfburn': 'apps/XXX/xfburn',
	'apps/XXX/org.xfce.xfdesktop': 'apps/XXX/preferences-desktop-wallpaper',
	'apps/XXX/org.xfce.xfmpc': 'devices/XXX/multimedia-player',
	'apps/XXX/org.xfce.xfwm4-tweaks': 'apps/XXX/wmtweaks',
	'apps/XXX/org.xfce.xfwm4': 'apps/XXX/window-manager',
	'actions/XXX/xfsm-switch-user': 'apps/XXX/xfsm-switch',
	'actions/XXX/xfsm-lock': 'actions/XXX/lock',
	'status/XXX/notification-disabled-symbolic': 'status/XXX/dialog-error',
	'status/XXX/notification-symbolic': 'status/XXX/dialog-information',
	'status/XXX/org.xfce.notification.unread-emblem-symbolic': 'status/XXX/dialog-warning'
}

if __name__ == "__main__":
	for new, old in mapping.items():
		for theme in icon_folders:
			for res in icon_res:
				ext = ".png"
				if res == "scalable":
					ext = ".svg"
				new_icon = icon_root + "/" + theme + "/" + new.replace("XXX", res) + ext
				old_icon = icon_root + "/" + theme + "/" + old.replace("XXX", res) + ext
				if os.path.exists(old_icon):
					cmd = "ln -rsf \"" + old_icon + "\" \"" + new_icon + "\""
					if dry_run:
						print(cmd)
					else:
						subprocess.run(cmd, shell=True)
