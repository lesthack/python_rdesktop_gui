#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  python_rdesktop_gui.py
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the  nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

#  Homepage: https://gist.github.com/zeroSteiner/6179745
#  Author:   Spencer McIntyre (zeroSteiner)

import ConfigParser
import os
os.EX__BASE = 64
import subprocess
import sys
from urlparse import urlparse

from gi.repository import Gtk

def find_rdesktop():
	for directory in os.getenv('PATH').split(':'):
		location = os.path.join(directory, 'rdesktop')
		if os.path.isfile(location):
			return location
	return None

class RdesktopWindow(Gtk.Window):
	def __init__(self, rdesktop_bin, config_path):
		Gtk.Window.__init__(self)
		self.set_title('rdesktop GUI')
		self.set_size_request(300, 300)
		self.set_resizable(True)
		self.set_position(Gtk.WindowPosition.CENTER)
		self.rdesktop_bin = rdesktop_bin
		self.config_path = config_path

		self.config = ConfigParser.ConfigParser()
		self.config.readfp(open(config_path, 'r'))
		if not self.config.has_section('main'):
			self.config.add_section('main')

		main_vbox = Gtk.VBox(spacing = 5)
		self.add(main_vbox)

		frame = Gtk.Frame()
		frame.set_label('Settings')
		frame.set_border_width(10)
		main_vbox.add(frame)

		options_hbox = Gtk.HBox(spacing = 5)
		frame.add(options_hbox)
		column1_vbox = Gtk.VBox(spacing = 5)
		options_hbox.add(column1_vbox)
		column2_vbox = Gtk.VBox(spacing = 5)
		options_hbox.add(column2_vbox)

		column1_vbox.add(Gtk.Label('Host'))
		self.host_entry = Gtk.ComboBoxText.new_with_entry()
		if self.config.has_option('main', 'hosts'):
			hosts = self.config.get('main', 'hosts')
			hosts = hosts.split(',')
			for host in hosts[:5]:
				self.host_entry.append_text(host)
			self.host_entry.set_active(0)
		column2_vbox.add(self.host_entry)

		column1_vbox.add(Gtk.Label('Username'))
		self.username_entry = Gtk.Entry()
		if self.config.has_option('main', 'username'):
			self.username_entry.set_text(self.config.get('main', 'username'))
		column2_vbox.add(self.username_entry)

		column1_vbox.add(Gtk.Label('Password'))
		self.password_entry = Gtk.Entry()
		self.password_entry.set_property('visibility', False)
		column2_vbox.add(self.password_entry)

		column1_vbox.add(Gtk.Label('Domain'))
		self.domain_entry = Gtk.Entry()
		if self.config.has_option('main', 'domain'):
			self.domain_entry.set_text(self.config.get('main', 'domain'))
		column2_vbox.add(self.domain_entry)

		column1_vbox.add(Gtk.Label('Geometry'))
		self.geometry_combo = Gtk.ComboBoxText()
		self.geometry_combo.append_text('800x600')
		self.geometry_combo.append_text('1024x768')
		self.geometry_combo.append_text('1280x720')
		self.geometry_combo.append_text('1280x960')
		self.geometry_combo.append_text('1366x768')
		self.geometry_combo.append_text('1440x1080')
		self.geometry_combo.append_text('1600x900')
		self.geometry_combo.append_text('1920x1080')
		self.geometry_combo.append_text('[full-screen]')
		self.geometry_combo.set_active(0)
		if self.config.has_option('main', 'geometry'):
			desired_geometry = self.config.get('main', 'geometry')
			geometry_model = self.geometry_combo.get_model()
			idx = 0
			for row in self.geometry_combo.get_model():
				if row[0] == desired_geometry:
					self.geometry_combo.set_active(idx)
					break
				idx += 1
		column2_vbox.add(self.geometry_combo)

		column1_vbox.add(Gtk.Label(''))
		self.attach_to_console_btn = Gtk.CheckButton(label='Attach To Console')
		if self.config.has_option('main', 'console'):
			attach_to_console = self.config.getboolean('main', 'console')
			self.attach_to_console_btn.set_property('active', attach_to_console)
		column2_vbox.add(self.attach_to_console_btn)

		hbox = Gtk.HBox(False)
		main_vbox.add(hbox)
		connect_button = Gtk.Button()
		connect_button.set_border_width(10)
		self.connect_button = connect_button
		self.password_entry.connect('activate', lambda w: self.connect_button.emit('clicked'))
		hbox.pack_end(connect_button, False, False, 5)
		hbox = Gtk.HBox()
		hbox.add(Gtk.Image.new_from_stock(Gtk.STOCK_APPLY, Gtk.IconSize.BUTTON))
		hbox.add(Gtk.Label('Connect'))
		connect_button.add(hbox)
		connect_button.connect('clicked', self.on_connect_clicked)

	def on_connect_clicked(self, widget):
		execl_args = [self.rdesktop_bin]
		username = self.username_entry.get_text()
		if username:
			execl_args.append('-u')
			execl_args.append(username)
			self.config.set('main', 'username', username)
		password = self.password_entry.get_text()
		if password:
			execl_args.append('-p')
			execl_args.append(password)
		domain = self.domain_entry.get_text()
		if domain:
			execl_args.append('-d')
			execl_args.append(domain)
			self.config.set('main', 'domain', domain)
		geometry = self.geometry_combo.get_active_text()
		self.config.set('main', 'geometry', geometry)
		if geometry == '[full-screen]':
			execl_args.append('-f')
		else:
			execl_args.append('-g')
			execl_args.append(geometry)
		attach_to_console = self.attach_to_console_btn.get_active()
		if attach_to_console:
			execl_args.append('-0')
		self.config.set('main', 'console', attach_to_console)
		host = self.host_entry.get_active_text()
		if self.config.has_option('main', 'hosts'):
			hosts = self.config.get('main', 'hosts').split(',')
			hosts = filter(lambda h: h != host, hosts)
			hosts.insert(0, host)
			hosts = hosts[:5]
			self.config.set('main', 'hosts', ','.join(hosts))
		else:
			self.config.set('main', 'hosts', host)
		execl_args.append(host)

                # Experience
                execl_args.append('-x l')
                # Compress
                execl_args.append('-z')
                # Caching bitmaps
                execl_args.append('-P')
                # Title
                execl_args.append('-T {}_{}'.format(host,username))
                # Clipboard Activado
                execl_args.append('-r')
                execl_args.append('clipboard:PRIMARYCLIPBOARD')
                # disk remote
                execl_args.append('-r')
                execl_args.append('disk:remote={}'.format(os.path.expanduser('~') + '/Public'))

		self.config.write(open(self.config_path, 'w'))
		self.hide()
		while Gtk.events_pending():
			Gtk.main_iteration()
		proc_h = subprocess.Popen(execl_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		result = proc_h.wait()
		#if result < os.EX__BASE:
		#	Gtk.main_quit()
		#	return
		self.show_all()
		#error_dialog = Gtk.MessageDialog(self, Gtk.DialogFlags.DESTROY_WITH_PARENT, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, 'An Error Occurred')
		#error_dialog.set_title('Error')
		#error_dialog.run()
		#error_dialog.destroy()
		return

def main():
	rdesktop_bin = find_rdesktop()
	if not rdesktop_bin:
		print 'could not locate the rdesktop binary'
		return 0
	config_path = os.path.join(os.path.expanduser('~'), '.config', 'rdesktop-gui.conf')
	if not os.path.isfile(config_path):
		open(config_path, 'w')
	win = RdesktopWindow(rdesktop_bin, config_path)
	win.connect('delete-event', Gtk.main_quit)
	if len(sys.argv) > 1:
		connection_information = urlparse(sys.argv[1])
		if connection_information.scheme in ['rdp', 'mstsc']:
			win.host_entry.prepend_text(connection_information.hostname or '')
			win.host_entry.set_active(0)
			win.username_entry.set_text(connection_information.username or '')
			win.password_entry.set_text(connection_information.password or '')
	win.show_all()
	Gtk.main()

if __name__ == '__main__':
    main()
