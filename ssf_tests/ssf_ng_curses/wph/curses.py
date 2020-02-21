#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''WPH curses wrapper library'''

import curses

class CursesAbstract():
    ''' curses library helper object '''
    @staticmethod
    def text(win, yyy, xxx, label, color=None):
        ''' put text into window '''
        try:
            if color:
                win.addstr(yyy, xxx, label, color)
            else:
                win.addstr(yyy, xxx, label)
        except curses.error:
            pass

    @staticmethod
    def draw_rectangle(win, uly, ulx, lry, lrx, dashed=False):
        """Rectangle with corners."""
        if dashed:
            hch = ord('-')
            vch = ord('|')
        else:
            hch = curses.ACS_HLINE
            vch = curses.ACS_VLINE

        # Borders
        win.vline(uly+1, ulx, vch, lry - uly - 1)
        win.hline(uly, ulx+1, hch, lrx - ulx - 1)
        win.hline(lry, ulx+1, hch, lrx - ulx - 1)
        win.vline(uly+1, lrx, vch, lry - uly - 1)
        win.addch(uly, ulx, curses.ACS_ULCORNER)
        try:
            win.addch(uly, lrx, curses.ACS_URCORNER)
            '''
            * The _WRAPPED flag is useful only for telling an application that we've just
            * wrapped the cursor.  We don't do anything with this flag except set it when
            * wrapping, and clear it whenever we move the cursor.  If we try to wrap at
            * the lower-right corner of a window, we cannot move the cursor (since that
            * wouldn't be legal).  So we return an error (which is what SVr4 does).
            * Unlike SVr4, we can successfully add a character to the lower-right corner
            * (Solaris 2.6 does this also, however).
            */
            '''
            win.addch(lry, lrx, curses.ACS_LRCORNER)
        except curses.error:
            pass
        win.addch(lry, ulx, curses.ACS_LLCORNER)

class CursesWindowAbstract(CursesAbstract):
    ''' curses window abstract object'''
    def __init__(self):
        self._stdscr = curses.initscr()
        curses.start_color()
        self._stdscr.keypad(1)
        curses.noecho()
        curses.cbreak()
        self._padding = 0
        self._size_y, self._size_x = (self._stdscr.getmaxyx())
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)
        curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        self._win = curses.newwin(self._size_y - self._padding * 2,
                                  self._size_x - self._padding * 2,
                                  self._padding, self._padding)

    @property
    def win(self):
        ''' window object '''
        return self._win

    @property
    def padding(self):
        ''' set window padding '''
        return self._padding

    @padding.setter
    def padding(self, padding):
        self._padding = padding

    def curses_stop(self):
        ''' return from ncurses '''
        curses.nocbreak()
        self._stdscr.keypad(0)
        curses.echo()
        curses.endwin()

    def resize_window(self):
        ''' update window if resized '''
        self._size_y, self._size_x = self._stdscr.getmaxyx()
        self._win.resize(self._size_y - self._padding * 2,
                         self._size_x - self._padding * 2)
        self._win.clear()
        self.redraw()
        curses.doupdate()

    def text(self, yyy, xxx, label, color=None):
        super().text(self._win, yyy + self._padding, xxx + self._padding, label, color)

    def redraw(self):
        ''' clear window screen - must to be overriden '''
        self._win.clear()

    def redraw_borders(self):
        ''' create window borders '''
        self.draw_rectangle(self._win, 0, 0, self._size_y - 1, self._size_x - 1)

class CursesPadAbstract(CursesAbstract):
    ''' curses pad abstract object '''
    def __init__(self, pos_x, pos_y, size_x, size_y, virtual_y,
                 padding=0, borders=False, header=""):
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._size_x = size_x
        self._size_y = size_y
        self._visible = True
        self._padding = padding
        self._borders = borders
        self._header = header
        self._redraw_callback = None
        self._pad = curses.newpad(virtual_y, size_x)

    @property
    def padding(self):
        ''' padding for pad '''
        return self._padding

    @property
    def visible(self):
        ''' define if pad should be visible on the screen'''
        return self._visible

    @visible.setter
    def visible(self, visible):
        self._visible = visible

    @property
    def borders(self):
        ''' borders - enabled/disabled '''
        return self._borders

    @property
    def pad(self):
        ''' curses pad object '''
        return self._pad

    def text(self, yyy, xxx, label, color=None):
        super().text(self._pad, yyy + self._padding, xxx + self._padding, label, color)

    def redraw(self):
        ''' clear the window and redraw borders '''
        if self.visible:
            self._pad.clear()
            if self._borders:
                self.redraw_borders()

    def key_handler(self, key_code):
        ''' set properties according key_code'''
        if key_code == ord('c'):
            self._visible = False

    def redraw_borders(self):
        ''' create window borders '''
        self.draw_rectangle(self._pad, 0, 0,
                            self._size_y - 1, self._size_x - 1)

class CursesCursorList(CursesPadAbstract):
    ''' curses pad with list object and cursor '''
    def __init__(self, pos_x, pos_y, size_x, size_y, data, header="", cursor=0):
        self._data = data
        super().__init__(pos_x, pos_y, size_x, size_y, size_y, padding=0, borders=True)
        self._cursor = cursor
        self._pad_cursor = 0
        self._header = header
        self._datapad = CursesPadAbstract(pos_x + 1, pos_y + 1,
                                          size_x - 2, size_y - 2, self.data_size)
        self.cursor_color = curses.color_pair(3)
        self._selected = None

    @property
    def data_size(self):
        ''' number of lines in list counted from data '''
        return len(self._data)

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, visible):
        if visible:
            self._selected = None
        self._visible = visible

    @property
    def selected(self):
        ''' choosen item from data '''
        return self._selected

    def redraw(self):
        ''' redraw pad content '''
        super().redraw()
        if self.visible:
            y_axis = 0
            for line in self._data:
                color = None
                if y_axis == self._cursor:
                    color = self.cursor_color
                self._datapad.text(y_axis, 0, str(line).ljust(self._size_x - 2), color)
                y_axis += 1
            self.redraw_borders()
            self.text(0, 1, " %s " % self._header)
            #self.text(0, 0, "%s/%s/%s" % (self._cursor, self._pad_cursor, self.data_size))
            self.pad.refresh(0, 0, self._pos_y, self._pos_x,
                             self._pos_y + self._size_y, self._pos_x + self._size_x)
            self._datapad.pad.refresh(self._pad_cursor, 0,
                                      self._pos_y + 1, self._pos_x + 1,
                                      self._pos_y + 1 + (self._size_y - 3),
                                      self._pos_x + 1 + (self._size_x - 2))

    def key_handler(self, key_code):
        super().key_handler(key_code)
        if key_code == curses.KEY_UP:
            if self._cursor > 0:
                self._cursor -= 1
            if self._pad_cursor - self._cursor > 0 and self._pad_cursor > 0:
                self._pad_cursor -= 1
        if key_code == curses.KEY_DOWN:
            if self._cursor < len(self._data) - 1:
                self._cursor += 1
            if self._cursor >= (self._size_y - 2) and self.data_size - self._cursor < self.data_size - self._size_y - self._pad_cursor + 3:
                self._pad_cursor += 1
        if key_code in [curses.KEY_ENTER, 10, 13]:
            self._selected = self._data[self._cursor]
            self.visible = False
