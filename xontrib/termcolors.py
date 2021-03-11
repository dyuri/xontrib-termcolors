from xonsh.tools import color_style
from xonsh.style_tools import Token

# setting terminal colors
# - \033]4;N;#RRGGBB\033\\ - set color N to #RRGGBB
# - \033]S;#RRGGBB\033\\ - set special color to #RRGGBB where S is:
# -- 10 - foreground - Token.Terminal.Foreground
# -- 11 - background - Token.Terminal.Background
# -- 12 - cursor - Token.Terminal.Cursor
# more info: https://www.xfree86.org/current/ctlseqs.html => Operating System Controls


__all__ = ()

_TC_COLOR_NAMES = [
    "BLACK",
    "RED",
    "GREEN",
    "YELLOW",
    "BLUE",
    "PURPLE",
    "CYAN",
    "WHITE",
    "INTENSE_BLACK",
    "INTENSE_RED",
    "INTENSE_GREEN",
    "INTENSE_YELLOW",
    "INTENSE_BLUE",
    "INTENSE_PURPLE",
    "INTENSE_CYAN",
    "INTENSE_WHITE",
]

_TC_SPECIAL_NAMES = [
    "Foreground",
    "Background",
    "Cursor",
]


def _tc_set_color(idx, color):
    print(f"\x1b]4;{idx};{color}\x1b\\", end="")


def _tc_set_special(idx, color):
    print(f"\x1b]{10+idx};{color}\x1b\\", end="")


def _tc_set_term_colors():
    style = color_style()
    for idx, key in enumerate(_TC_COLOR_NAMES):
        token = getattr(Token.Color, key)
        try:
            color = style.get(token)
            _tc_set_color(idx, color)
        except:
            pass


def _tc_set_spec_colors():
    style = color_style()
    for idx, key in enumerate(_TC_SPECIAL_NAMES):
        token = getattr(Token.Terminal, key)
        try:
            color = style.get(token)
            _tc_set_special(idx, color)
        except:
            pass


def _tc_show_colors():
    collist = []
    for line in range(0, 2):
        for col in range(0, 8):
            collist.append(f"\x1b[48;5;{line * 8 + col}m   ")
        collist.append("\n")
    return "".join(collist)


def _tc_set_colors(args, stdin=None):
    _tc_set_term_colors()
    _tc_set_spec_colors()

    if __xonsh__.env.get('XONTRIB_TERMCOLORS_DEBUG', False):
        return _tc_show_colors()


aliases["termcolors"] = _tc_set_colors
