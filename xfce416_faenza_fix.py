#!/bin/python3

import os
import sys
import subprocess

icon_root = '/usr/share/icons'
icon_folders = {'Faenza', 'Faenza-Ambiance', 'Faenza-Dark', 'Faenza-Darker', 'Faenza-Darkest', 'Faenza-Radiance'}
icon_res = {'16', '22', '24', '32', '48', '64', '96', 'scalable'}
dry_run = True

mapping_symb = {
	'mimetypes/XXX/audio-x-generic-symbolic',
	'places/XXX/start-here-debian-symbolic',
	'places/XXX/start-here-gnome-symbolic',
	'places/XXX/folder-symbolic',r
	'places/XXX/start-here-opensuse-symbolic',
	'places/XXX/start-here-ubuntu-symbolic',
	'places/XXX/user-trash-symbolic',
	'places/XXX/start-here-slackware-symbolic',
	'places/XXX/start-here-fedora-symbolic',
	'places/XXX/start-here-linux-mint-symbolic',
	'places/XXX/start-here-gentoo-symbolic',
	'places/XXX/start-here-archlinux-symbolic',
	'places/XXX/start-here-frugalware-symbolic',
	'places/XXX/start-here-mandriva-symbolic',
	'emblems/XXX/emblem-symbolic-link',
	'status/XXX/weather-clear-symbolic',
	'status/XXX/battery-good-charging-symbolic',
	'status/XXX/network-wireless-acquiring-symbolic',
	'status/XXX/network-wired-symbolic',
	'status/XXX/battery-full-symbolic',
	'status/XXX/audio-volume-medium-symbolic',
	'status/XXX/network-wired-acquiring-symbolic',
	'status/XXX/audio-volume-low-symbolic',
	'status/XXX/microphone-sensitivity-high-symbolic',
	'status/XXX/battery-full-charging-symbolic',
	'status/XXX/network-wireless-signal-ok-symbolic',
	'status/XXX/network-wireless-encrypted-symbolic',
	'status/XXX/user-invisible-symbolic',
	'status/XXX/user-available-symbolic',
	'status/XXX/avatar-default-symbolic',
	'status/XXX/security-low-symbolic',
	'status/XXX/mail-unread-symbolic',
	'status/XXX/media-playlist-shuffle-symbolic',
	'status/XXX/network-wireless-signal-excellent-symbolic',
	'status/XXX/battery-low-symbolic',
	'status/XXX/weather-clouds-symbolic',
	'status/XXX/bluetooth-active-symbolic',
	'status/XXX/weather-few-clouds-symbolic',
	'status/XXX/display-brightness-symbolic',
	'status/XXX/network-cellular-connected-symbolic',
	'status/XXX/network-cellular-signal-ok-symbolic',
	'status/XXX/media-playlist-repeat-symbolic',
	'status/XXX/user-away-symbolic',
	'status/XXX/starred-symbolic',
	'status/XXX/printer-error-symbolic',
	'status/XXX/user-offline-symbolic',
	'status/XXX/audio-volume-muted-symbolic',
	'status/XXX/network-wireless-signal-good-symbolic',
	'status/XXX/user-status-pending-symbolic',
	'status/XXX/network-cellular-signal-good-symbolic',
	'status/XXX/security-medium-symbolic',
	'status/XXX/mail-attachment-symbolic',
	'status/XXX/non-starred-symbolic',
	'status/XXX/network-cellular-3g-symbolic',
	'status/XXX/security-high-symbolic',
	'status/XXX/network-cellular-umts-symbolic',
	'status/XXX/battery-good-symbolic',
	'status/XXX/user-busy-symbolic',
	'status/XXX/network-error-symbolic',
	'status/XXX/network-wireless-signal-weak-symbolic',
	'status/XXX/network-vpn-acquiring-symbolic',
	'status/XXX/weather-clear-night-symbolic',
	'status/XXX/network-wireless-signal-none-symbolic',
	'status/XXX/network-cellular-4g-symbolic',
	'status/XXX/battery-empty-symbolic',
	'status/XXX/network-cellular-edge-symbolic',
	'status/XXX/network-cellular-signal-weak-symbolic',
	'status/XXX/microphone-sensitivity-none-symbolic',
	'status/XXX/weather-showers-symbolic',
	'status/XXX/network-cellular-signal-acquiring-symbolic',
	'status/XXX/software-update-available-symbolic',
	'status/XXX/network-transmit-symbolic',
	'status/XXX/microphone-sensitivity-medium-symbolic',
	'status/XXX/weather-clouds-night-symbolic',
	'status/XXX/network-cellular-signal-excellent-symbolic',
	'status/XXX/printer-printing-symbolic',
	'status/XXX/software-update-urgent-symbolic',
	'status/XXX/changes-allow-symbolic',
	'status/XXX/network-cellular-signal-none-symbolic',
	'status/XXX/weather-showers-scattered-symbolic',
	'status/XXX/battery-empty-charging-symbolic',
	'status/XXX/network-wired-disconnected-symbolic',
	'status/XXX/printer-warning-symbolic',
	'status/XXX/dialog-question-symbolic',
	'status/XXX/battery-low-charging-symbolic',
	'status/XXX/user-idle-symbolic',
	'status/XXX/dialog-information-symbolic',
	'status/XXX/weather-storm-symbolic',
	'status/XXX/mail-read-symbolic',
	'status/XXX/battery-full-charged-symbolic',
	'status/XXX/keyboard-brightness-symbolic',
	'status/XXX/battery-missing-symbolic',
	'status/XXX/network-cellular-gprs-symbolic',
	'status/XXX/weather-fog-symbolic',
	'status/XXX/bluetooth-disabled-symbolic',
	'status/XXX/battery-caution-charging-symbolic',
	'status/XXX/dialog-warning-symbolic',
	'status/XXX/audio-volume-high-symbolic',
	'status/XXX/changes-prevent-symbolic',
	'status/XXX/dialog-error-symbolic',
	'status/XXX/weather-snow-symbolic',
	'status/XXX/microphone-sensitivity-low-symbolic',
	'status/XXX/weather-severe-alert-symbolic',
	'status/XXX/network-receive-symbolic',
	'status/XXX/battery-caution-symbolic',
	'status/XXX/dialog-password-symbolic',
	'status/XXX/network-vpn-symbolic',
	'status/XXX/weather-overcast-symbolic',
	'status/XXX/weather-few-clouds-night-symbolic',
	'apps/XXX/preferences-desktop-accessibility-symbolic',
	'actions/XXX/go-previous-symbolic',
	'actions/XXX/system-run-symbolic',
	'actions/XXX/document-save-symbolic',
	'actions/XXX/format-text-italic-symbolic',
	'actions/XXX/edit-clear-symbolic',
	'actions/XXX/go-next-symbolic',
	'actions/XXX/zoom-out-symbolic',
	'actions/XXX/edit-find-symbolic',
	'actions/XXX/process-stop-symbolic',
	'actions/XXX/format-text-underline-symbolic',
	'actions/XXX/go-up-symbolic',
	'actions/XXX/go-first-symbolic',
	'actions/XXX/go-last-symbolic',
	'actions/XXX/media-playback-pause-symbolic',
	'actions/XXX/format-indent-more-symbolic',
	'actions/XXX/media-skip-forward-symbolic',
	'actions/XXX/window-close-symbolic',
	'actions/XXX/media-playback-stop-symbolic',
	'actions/XXX/format-indent-less-symbolic',
	'actions/XXX/go-top-symbolic',
	'actions/XXX/edit-copy-symbolic',
	'actions/XXX/zoom-fit-symbolic',
	'actions/XXX/view-refresh-symbolic',
	'actions/XXX/view-list-details-symbolic',
	'actions/XXX/edit-delete-symbolic',
	'actions/XXX/zoom-original-symbolic',
	'actions/XXX/format-justify-left-symbolic',
	'actions/XXX/zoom-in-symbolic',
	'actions/XXX/format-text-strikethrough-symbolic',
	'actions/XXX/format-justify-fill-symbolic',
	'actions/XXX/list-add-symbolic',
	'actions/XXX/format-text-bold-symbolic',
	'actions/XXX/mail-send-receive-symbolic',
	'actions/XXX/edit-redo-symbolic',
	'actions/XXX/media-skip-backward-symbolic',
	'actions/XXX/list-remove-symbolic',
	'actions/XXX/media-record-symbolic',
	'actions/XXX/system-shutdown-symbolic',
	'actions/XXX/document-open-recent-symbolic',
	'actions/XXX/go-bottom-symbolic',
	'actions/XXX/view-restore-symbolic',
	'actions/XXX/format-justify-center-symbolic',
	'actions/XXX/view-fullscreen-symbolic',
	'actions/XXX/format-justify-right-symbolic',
	'actions/XXX/view-list-compact-symbolic',
	'actions/XXX/media-eject-symbolic',
	'actions/XXX/edit-cut-symbolic',
	'actions/XXX/document-save-as-symbolic',
	'actions/XXX/media-playback-start-symbolic',
	'actions/XXX/view-list-icons-symbolic',
	'actions/XXX/go-down-symbolic',
	'actions/XXX/edit-paste-symbolic',
	'actions/XXX/edit-undo-symbolic',
	'devices/XXX/media-optical-symbolic',
	'devices/XXX/audio-input-microphone-symbolic',
	'devices/XXX/video-display-symbolic',
	'devices/XXX/camera-web-symbolic',
	'devices/XXX/camera-photo-symbolic',
	'devices/XXX/phone-symbolic',
	'devices/XXX/computer-symbolic',
	'devices/XXX/printer-symbolic',
	'devices/XXX/input-keyboard-symbolic',
	'devices/XXX/drive-harddisk-symbolic'
}

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
	'status/XXX/notification-disabled-symbolic': 'status/XXX/dialog-error-symbolic',
	'status/XXX/notification-symbolic': 'status/XXX/dialog-information-symbolic',
	'status/XXX/org.xfce.notification.unread-emblem-symbolic': 'status/XXX/dialog-warning-symbolic',
	'status/XXX/battery-level-0-symbolic': 'status/XXX/battery-empty-symbolic',
	'status/XXX/battery-level-0-charging-symbolic': 'status/XXX/battery-empty-charging-symbolic',
	'status/XXX/battery-level-10-symbolic': 'status/XXX/battery-caution-symbolic',
	'status/XXX/battery-level-10-charging-symbolic': 'status/XXX/battery-caution-charging-symbolic',
	'status/XXX/battery-level-20-symbolic': 'status/XXX/battery-caution-symbolic',
	'status/XXX/battery-level-20-charging-symbolic': 'status/XXX/battery-caution-charging-symbolic',
	'status/XXX/battery-level-30-symbolic': 'status/XXX/battery-low-symbolic',
	'status/XXX/battery-level-30-charging-symbolic': 'status/XXX/battery-low-charging-symbolic',
	'status/XXX/battery-level-40-symbolic': 'status/XXX/battery-low-symbolic',
	'status/XXX/battery-level-40-charging-symbolic': 'status/XXX/battery-low-charging-symbolic',
	'status/XXX/battery-level-50-symbolic': 'status/XXX/battery-low-symbolic',
	'status/XXX/battery-level-50-charging-symbolic': 'status/XXX/battery-low-charging-symbolic',
	'status/XXX/battery-level-60-symbolic': 'status/XXX/battery-good-symbolic',
	'status/XXX/battery-level-60-charging-symbolic': 'status/XXX/battery-good-charging-symbolic',
	'status/XXX/battery-level-70-symbolic': 'status/XXX/battery-good-symbolic',
	'status/XXX/battery-level-70-charging-symbolic': 'status/XXX/battery-good-charging-symbolic',
	'status/XXX/battery-level-80-symbolic': 'status/XXX/battery-good-symbolic',
	'status/XXX/battery-level-80-charging-symbolic': 'status/XXX/battery-good-charging-symbolic',
	'status/XXX/battery-level-90-symbolic': 'status/XXX/battery-full-symbolic',
	'status/XXX/battery-level-90-charging-symbolic': 'status/XXX/battery-full-charging-symbolic',
	'status/XXX/battery-level-100-symbolic': 'status/XXX/battery-full-symbolic',
	'status/XXX/battery-level-100-charged-symbolic': 'status/XXX/battery-full-charged-symbolic',
	'devices/XXX/battery-symbolic': 'status/XXX/battery-full-symbolic'
}

if __name__ == "__main__":
	cmd = "find " + icon_root + "/Faenza-Dark -iname \"*-symbolic.svg\" -type l"
	if not dry_run:
		cmd = cmd + " -delete"
	else:
		cmd = cmd + " -printf \"delete: %p\n\""
	subprocess.run(cmd, shell=True)
	for symb in mapping_symb:
		for theme in icon_folders:
			reference_icon = icon_root + "/" + theme + "/" + symb.replace("XXX", "scalable") + ".svg"
			if os.path.exists(reference_icon):
				for res in icon_res:
					if (res != "scalable"):
						output = os.path.dirname(icon_root + "/" + theme + "/" + symb.replace("XXX", res))
						if os.path.exists(output):
							cmd = "gtk-encode-symbolic-svg -o " + output + " " + reference_icon + " " + res + "x" + res
							if dry_run:
								print(cmd)
							else:
								subprocess.run(cmd, shell=True)
												
	for new, old in mapping.items():
		for theme in icon_folders:
			for res in icon_res:
				ext = ".png"
				symb = ".symbolic"
				if res == "scalable":
					ext = ".svg"
					symb = ""
				if new.endswith("-symbolic"):
					ext = symb + ext
				new_icon = icon_root + "/" + theme + "/" + new.replace("XXX", res) + ext
				old_icon = icon_root + "/" + theme + "/" + old.replace("XXX", res) + ext
				if os.path.exists(old_icon) and os.path.exists(os.path.dirname(new_icon)):
					cmd = "ln -rsf \"" + old_icon + "\" \"" + new_icon + "\""
					if dry_run:
						print(cmd)
					else:
						subprocess.run(cmd, shell=True)
	for theme in icon_folders:
		cmd = "gtk-update-icon-cache -f " + icon_root + "/" + theme
		if dry_run:
			print(cmd)
		else:
			subprocess.run(cmd, shell=True)
