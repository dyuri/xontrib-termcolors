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

## Known issues

`termcolors` command cannot be used in `.xonshrc` currently, it needs a working shell instance to get the theme.

## Credits

This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).

