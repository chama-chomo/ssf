#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import urwid
import random
import os

class ItemWidget (urwid.WidgetWrap):

    def __init__ (self, id, description):
        self.id = id
        self.content = '%s >> %s...' % (str(id), description[:25])
        self.item = [
            ('fixed', 25, urwid.Padding(urwid.AttrWrap(
                urwid.Text('Device %s' % str(id)), 'body', 'focus'), left=2)),
            urwid.AttrWrap(urwid.Text('%s' % description), 'body', 'focus'),
        ]
        w = urwid.Columns(self.item)
        self.__super.__init__(w)

    def selectable (self):
        return True

    def keypress(self, size, key):
        return key

def main ():

    palette = [
        ('body','dark cyan', '', 'standout'),
        ('focus','dark red', '', 'standout'),
        ('head','light red', 'black'),
        ]

    wphs = [{'name': 'f-000000029042', 'ip': '10.10.29.42', 'ilo_ip': '10.10.29.43', 'os_name': 'WPH_main 1.9', 'comment': 'mci: test oddelenie od Fireflies', 'global_status': 'OK', 'build_status': 'Installed', 'owner_name': 'Petr Gadorek', 'model_name': 'SKU1 Edge', 'hostgroup_title': 'Scarabs', 'index': 1}, {'name': 'f-000000029054', 'ip': '10.10.29.54', 'ilo_ip': '10.10.29.55', 'os_name': 'WPH_main 1.9', 'comment': 'dpr: testing acronis beta\r\nmci: ', 'global_status': 'OK', 'build_status': 'Installed', 'owner_name': 'David Pravec', 'model_name': 'SKU3 Edge', 'hostgroup_title': 'Scarabs', 'index': 2}, {'name': 'f-010010029066', 'ip': '10.10.29.66', 'ilo_ip': '10.10.29.67', 'os_name': 'WPH_main+fire', 'comment': 'mci: https://jira.kmiservicehub.', 'global_status': 'OK', 'build_status': 'Installed', 'owner_name': 'Jaroslav Sin', 'model_name': 'SKU2', 'hostgroup_title': 'Scarabs', 'index': 3}]
    
    def find_wph(selected):
        #  raise urwid.ExitMainLoop()
        loop.stop()
        #  os.system('clear')
        selected = selected.split()
        selected = selected[0]

        print(f'selected: "{selected}"')

        for wph in wphs:
            if wph['name'] == selected:
                print(f'''
name: {wph['name']}
IP: {wph['ip']}
OS name: {wph['os_name']}''')


    def keystroke (input):
        if input in ('q', 'Q'):
            raise urwid.ExitMainLoop()

        if input is 'enter':
            focus = listbox.get_focus()[0].content
            view.set_header(urwid.AttrWrap(urwid.Text(
                'selected: %s' % str(focus)), 'head'))

            find_wph(str(focus))

    items = []
    for row in wphs:
            items.append(ItemWidget(row['name'], row['model_name']))

    #  for i in items:
        #  print(i)
    header = urwid.AttrMap(urwid.Text('selected:'), 'head')
    listbox = urwid.ListBox(urwid.SimpleListWalker(items))
    view = urwid.Frame(urwid.AttrWrap(listbox, 'body'), header=header)
    loop = urwid.MainLoop(view, palette, unhandled_input=keystroke)
    loop.run()
    


if __name__ == '__main__':
    main()


