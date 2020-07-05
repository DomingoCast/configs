# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget

from typing import List  # noqa: F401

mod = "mod4"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("alacritty")),

    Key([mod], "a", lazy.spawn("pavucontrol")),
    Key([mod], "c", lazy.spawn("chromium")),
    Key([mod], "d", lazy.spawn("discord")),
    Key([mod], "f", lazy.spawn("dolphin")),
    Key([mod], "m", lazy.spawn("dmenu_run")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
]

##### GROUPS #####

# <edit>
group_names = 'WWW DEV SYS ETC'.split()
# groups = [Group(name, layout='monad_tall') for name in group_names]
groups = [Group(name, layout='monadtall') for name in group_names]
for i, name in enumerate(group_names):
    indx = str(i + 1)
    keys += [
        Key([mod], indx, lazy.group[name].toscreen()),
        Key([mod, 'shift'], indx, lazy.window.togroup(name))]
# </edit>
colors = {
        "grey_dark": "575757",
        "white": "f7f7f7"
        }

layout_theme = {"border_width": 5,
                "margin": 20,
                "border_focus": colors["grey_dark"],
                "border_normal": colors["white"]
                }
layouts = [
    layout.Max(),
    layout.MonadTall(**layout_theme),
    layout.Bsp(**layout_theme)
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top = bar.Bar(
            [
                widget.Sep(
                    background = colors["grey_dark"],
                    forground = colors["grey_dark"],
                    padding = 20,
                    linewidth = 0,
                    ),
                # widget.CurrentLayout(
                    # background = colors["white"]
                    # ),
                widget.GroupBox(
                    padding = 3,
                    padding_y = 6,
                    margin_y = 5,
                    background = colors["grey_dark"],
                    foreground = colors["white"],
                    block_highlight_text_color = colors["grey_dark"],
                    highlight_method = "line",
                    highlight_color = [colors["white"], colors["white"]]
                    ),
                widget.Sep(
                    background = colors["grey_dark"],
                    forground = colors["grey_dark"],
                    padding = 1200,
                    linewidth = 0,
                    # size_percent = 100
                    ),
                # widget.AGroupBox(
                    # background = colors['white']
                    # ),
                # widget.GroupBox(),
                # widget.GroupBox(font="Ubuntu Bold",
                        # fontsize = 9,
                        # margin_y = 3,
                        # margin_x = 0,
                        # padding_y = 5,
                        # padding_x = 5,
                        # borderwidth = 3,
                        # active = colors[2],
                        # inactive = colors[2],
                        # rounded = False,
                        # highlight_color = colors[1],
                        # highlight_method = "line",
                        # this_current_screen_border = colors[3],
                        # this_screen_border = colors [4],
                        # other_current_screen_border = colors[0],
                        # other_screen_border = colors[0],
                        # foreground = colors[2],
                        # background = colors[0]
                        # ),
                widget.Prompt(background = colors["grey_dark"]),
                widget.PulseVolume(                          #percentage volume
                    background = colors["grey_dark"],
                    ),
                widget.Sep(
                    background = colors["grey_dark"],
                    forground = colors["grey_dark"],
                    # size_percent = 100
                    ),
                widget.Battery(
                    background = colors["grey_dark"],
                    format = '{char} {percent:2.0%}'
                    ),
                widget.Sep(
                    background = colors["grey_dark"],
                    forground = colors["grey_dark"],
                    # size_percent = 100
                    ),
                # widget.BatteryIcon(background = colors["grey_dark"]),
                # widget.WindowName(background = colors["grey_dark"]),
                # widget.TextBox("default config", name="default"),
                # libqtile.widget.Volume(),
                widget.Systray(background = colors["grey_dark"]),
                widget.Clock(background = colors["grey_dark"], format='%Y-%m-%d %a %I:%M %p'),
                # widget.QuickExit(background = colors["grey_dark"]),
                widget.Sep(
                    background = colors["grey_dark"],
                    forground = colors["grey_dark"],
                    linewidth = 0,
                    padding = 20,

                    # size_percent = 100
                    ),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
