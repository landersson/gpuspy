import time
import curses
import math
# import curses.textpad as ctxtpad

def hbar(scr, y, x, l, c=197):
    # scr.addstr(y, x, , curses.color_pair(c))
    scr.attrset(curses.color_pair(240))
    scr.hline(y, x, curses.ACS_CKBOARD, l)
    scr.attrset(curses.color_pair(c))
    scr.hline(y, x, curses.ACS_CKBOARD, l//2)

# def pbar(src, y, x, size, percentage, color):

def rectangle(win, uly, ulx, lry, lrx):
    """Draw a rectangle with corners at the provided upper-left
    and lower-right coordinates.
    """
    win.vline(uly+1, ulx, curses.ACS_VLINE, lry - uly - 1)
    win.hline(uly, ulx+1, curses.ACS_HLINE, lrx - ulx - 1)
    win.hline(lry, ulx+1, curses.ACS_HLINE, lrx - ulx - 1)
    win.vline(uly+1, lrx, curses.ACS_VLINE, lry - uly - 1)
    win.addch(uly, ulx, curses.ACS_ULCORNER)
    win.addch(uly, lrx, curses.ACS_URCORNER)
    win.addch(lry, lrx, curses.ACS_LRCORNER)
    win.addch(lry, ulx, curses.ACS_LLCORNER)
    # win.addch(lry, ulx, curses.ACS_LLCORNER, curses.A_REVERSE)

def interp_range(x, x1, x2, cs):
    i = round((float(x - x1) / (x2 - x1)) * (len(cs) - 1))
    return cs[i]

def grad_hline(win, y, x1, x2, colors):
    for x in range(x1, x2+1):
        c = interp_range(x, x1, x2, colors)
        win.addch(y, x, curses.ACS_HLINE, curses.color_pair(c))

def grad_vline(win, y1, y2, x, colors):
    for y in range(y1, y2+1):
        c = interp_range(y, y1, y2, colors)
        win.addch(y, x, curses.ACS_VLINE, curses.color_pair(c))

def grad_box(win, y1, x1, y2, x2, title=None):
    grad_hline(win, y1, x1, x2, list(range(240, 245)))
    grad_hline(win, y2, x1, x2, list(range(240, 245)))
    grad_vline(win, y1, y2, x1, list(range(240, 245)))
    grad_vline(win, y1, y2, x2, list(range(240, 245)))

    win.attrset(curses.color_pair(250))
    win.addch(y1, x1, curses.ACS_ULCORNER)
    win.addch(y1, x2, curses.ACS_URCORNER)
    win.addch(y2, x2, curses.ACS_LRCORNER)
    win.addch(y2, x1, curses.ACS_LLCORNER)

    if title is not None:
        win.addstr(y1, x1 + 2, title)

def bar_meter(scr, y, x, name, value):

    scr.addstr(y, x, name + ":", curses.color_pair(208))
    x = x + len(name) + 2
    blen = 50
    hbar(scr, y, x, blen, 168)
    scr.addstr(y, x + blen + 1, "%d%%" % value)


# ╔═╗╔═╗╦ ╦╔═╗╔═╗╦ ╦
# ║ ╦╠═╝║ ║╚═╗╠═╝╚╦╝
# ╚═╝╩  ╚═╝╚═╝╩   ╩

 # ██████╗ ██████╗ ██╗   ██╗███████╗██████╗ ██╗   ██╗
# ██╔════╝ ██╔══██╗██║   ██║██╔════╝██╔══██╗╚██╗ ██╔╝
# ██║  ███╗██████╔╝██║   ██║███████╗██████╔╝ ╚████╔╝
# ██║   ██║██╔═══╝ ██║   ██║╚════██║██╔═══╝   ╚██╔╝
# ╚██████╔╝██║     ╚██████╔╝███████║██║        ██║
 # ╚═════╝ ╚═╝      ╚═════╝ ╚══════╝╚═╝        ╚═╝


def main(scr):
    curses.noecho()
    curses.start_color()
    curses.curs_set(False)
    scr.addstr(1, 1, "COLORS: %d" % curses.COLORS, curses.color_pair(208))
    scr.addstr(2, 1, "COLOR PAIR : %d" % curses.COLOR_PAIRS)
    scr.addstr(3, 1, "SIZE : %dx%d" % (curses.LINES, curses.COLS))
    scr.addstr(4, 1, "CHANGE COLOR : %s" % (str(curses.can_change_color())))
    scr.addstr(5, 1, "NASSE")
    scr.addstr(5, 1, "╔═╗╔═╗╦ ╦╔═╗╔═╗╦ ╦", curses.color_pair(248))
    scr.addstr(6, 1, "║ ╦╠═╝║ ║╚═╗╠═╝╚╦╝", curses.color_pair(246))
    scr.addstr(7, 1, "╚═╝╩  ╚═╝╚═╝╩   ╩", curses.color_pair(244))

    scr.addstr(3, 1, " ██████╗ ██████╗ ██╗   ██╗███████╗██████╗ ██╗   ██╗", curses.color_pair(248))
    scr.addstr(4, 1, "██╔════╝ ██╔══██╗██║   ██║██╔════╝██╔══██╗╚██╗ ██╔╝", curses.color_pair(246))
    scr.addstr(5, 1, "██║  ███╗██████╔╝██║   ██║███████╗██████╔╝ ╚████╔╝", curses.color_pair(244))
    scr.addstr(6, 1, "██║   ██║██╔═══╝ ██║   ██║╚════██║██╔═══╝   ╚██╔╝", curses.color_pair(242))
    scr.addstr(7, 1, "╚██████╔╝██║     ╚██████╔╝███████║██║        ██║", curses.color_pair(240))
    scr.addstr(8, 1, " ╚═════╝ ╚═╝      ╚═════╝ ╚══════╝╚═╝        ╚═╝", curses.color_pair(238))
    # curses.use_default_colors()
    # curses.color_s
    scr.bkgd(' ', curses.color_pair(1))

    for i in range(1, curses.COLORS):
        curses.init_pair(i, i, 235)
    try:
        for i in range(0, 255):
            scr.addstr("%x (%d) " % (i, i), curses.color_pair(i))
    except curses.ERR:
        # End of screen reached
        pass
    curses.init_pair(1, 235, 235)
    scr.addstr(25, 1, str(curses.ACS_VLINE))
    rectangle(scr, 25, 2, 30, 30)
    scr.addstr(20, 1, '\u2622', curses.color_pair(208))
    scr.addch(21, 1, 97, curses.color_pair(208) | curses.A_ALTCHARSET)
    scr.addch(21, 2, curses.ACS_CKBOARD, curses.color_pair(208))
    scr.addch(22, 2, curses.ACS_CKBOARD, curses.color_pair(208))
    # scr.addstr(21, 1, 97, curses.color_pair(208),)
    # scr.addch(20, 2, 97, curses.A_ALTCHARSET

    # for i in range(30):
        # hbar(scr, 32, 5, 10+i)
        # scr.refresh()
        # time.sleep(0.1)
    hbar(scr, 33, 2, 40, 165)
    hbar(scr, 32, 2, 60, 165)
    grad_box(scr, 34, 2, 44, 80, "kursk")
    grad_box(scr, 45, 2, 55, 80, "panzer")
    bar_meter(scr, 47, 3, "gpu0", 80)

    scr.getch()
import locale
locale.setlocale(locale.LC_ALL,"")

curses.wrapper(main)
