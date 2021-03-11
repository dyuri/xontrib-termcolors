<p align="center">
Set terminal colors based on selected xonsh theme.
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=Nice%20xontrib%20for%20the%20xonsh%20shell!&url=https://github.com/dyuri/xontrib-termcolors" target="_blank">tweet</a>.
</p>


## Installation

To install use pip:

```bash
xpip install xontrib-termcolors
# or: xpip install -U git+https://github.com/dyuri/xontrib-termcolors
```

## Usage

This xontrib sets the colors of your terminal based on your xonsh theme.

```bash
$ xontrib load termcolors
$ termcolors
```

## Colors

The main 16 colors will be used directly from the pygments/ptk theme. The following special colors can be set by adding the tokens to your theme:

- `Token.Terminal.Foreground` - foreground color
- `Token.Terminal.Background` - background color
- `Token.Terminal.Curson` - cursor color

## Example

To replace all colors in xonsh and terminal to green add this to your `.xonshrc`:
```python
from xonsh.tools import register_custom_style
from xonsh import style_tools
from pygments.token import Token

mystyle = {k: '#00ff00' for k,c in style_tools.DEFAULT_STYLE_DICT.items()}
mystyle[Token.Color.DEFAULT] = "#00ff00"
mystyle[Token.Terminal.Foreground] = '#00ff00'
mystyle[Token.Terminal.Curson] = '#00ff00'
mystyle[Token.Terminal.Background] = '#000000'

register_custom_style("green", mystyle, base=__xonsh__.env['XONSH_COLOR_STYLE'])
$XONSH_COLOR_STYLE="green"

xontrib load termcolors

@events.on_post_init
def on_post_init(**_):
    termcolors
```

## Known issues

`termcolors` command cannot be used in `.xonshrc` currently, it needs a working shell instance to get the theme.

## Credits

This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).

