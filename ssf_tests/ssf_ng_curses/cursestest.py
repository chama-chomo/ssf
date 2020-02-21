#!/usr/bin/python3
# -*- coding: utf-8 -*-

''' Curses testing script '''

import curses
from wph.curses import CursesWindowAbstract, CursesCursorList

class CursesApplication(CursesWindowAbstract):
    ''' curses application wrapper '''
    def __init__(self):
        super().__init__()
        self.data = None
        self.test_data = []
        for tdata in range(1, 41):
            self.test_data.append("test%s" % tdata)
        self._listdir = CursesCursorList(5, 5, 26, 26, self.test_data)
        curses.wrapper(self.curses_loop)
        self.curses_stop()

    def redraw(self):
        super().redraw()
        self.redraw_borders()
        self.text(1, 1, "%s:%s" % (self._size_x, self._size_y))
        self.text(1, 10, "Selected %s" % self.data)
        self.win.refresh()

    def curses_loop(self, stdscr):
        ''' main curses loop '''
        while True:
            resize = curses.is_term_resized(self._size_y, self._size_x)
            if resize is True:
                self.resize_window()
            self.redraw()
            self._listdir.redraw()
            key_code = stdscr.getch()
            if key_code == ord('q'):
                break
            if key_code == ord('p'):
                self._listdir.visible = True

            if self._listdir.visible:
                self._listdir.key_handler(key_code)
                if self._listdir.selected:
                    self.data = self._listdir.selected
            self.redraw()
            self._listdir.redraw()

def main():
    ''' program entry point '''
    CursesApplication()

if __name__ == "__main__":
    main()
