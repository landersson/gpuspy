#!/usr/bin/python

import curses
import locale

locale.setlocale(locale.LC_ALL,"")

def doStuff(stdscr):
  message = "hello \u2622"
  stdscr.addstr(0, 0, message)
  stdscr.getch() # pauses until a key's hit

curses.wrapper(doStuff)
