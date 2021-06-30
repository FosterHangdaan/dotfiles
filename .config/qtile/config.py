from typing import List  # noqa: F401

import os, subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

#from .themes.dracula.py import theme
theme = {
    "foreground": "f8f8f2",
    "background": "282a36",
    "selection_foreground": "ffffff",
    "selection_background": "44475a",
    "url_color": "8be9fd",

    # black
    "color0":  "21222c",
    "color8":  "6272a4",

    # red
    "color1":  "ff5555",
    "color9":  "ff6e6e",

    # green
    "color2":  "50fa7b",
    "color10": "69ff94",

    # yellow
    "color3":  "f1fa8c",
    "color11": "ffffa5",

    # blue
    "color4":  "bd93f9",
    "color12": "d6acff",

    # magenta
    "color5":  "ff79c6",
    "color13": "ff92df",

    # cyan
    "color6": "8be9fd",
    "color14": "a4ffff",

    # white
    "color7": "f8f8f2",
    "color15": "ffffff",

    # Cursor colors
    "cursor": "f8f8f2",
    "cursor_text_color": "282a36",

    # Tab bar colors
    "active_tab_foreground": "282a36",
    "active_tab_background": "f8f8f2",
    "inactive_tab_foreground": "282a36",
    "inactive_tab_background": "6272a4",

    # Marks
    "mark1_foreground": "282a36",
    "mark1_background": "ff5555"
}

mod = "mod4"
terminal = "kitty"

keys = [
    #Key(
    #    [mod, "control"], "Return",
    #    lazy.spawncmd(),
    #    desc="Spawn a command using a prompt widget"
    #),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    #Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
    #    desc="Toggle between split and unsplit sides of stack"),

    # Main Keybindings
    Key(
        [mod], "Return", lazy.spawn(terminal),
        desc="Launch terminal"
    ),
    Key(
        [mod, "shift"], "Return",
        lazy.spawn(
            "dmenu_run -m 0 -p 'Run: ' -fn 'Ubuntu Mono:bold:pixelsize=15' -nb '#{0}' -nf '#{1}' -sb '#{2}' -sf '#{3}'".format(theme["color0"], theme["color7"], theme["color3"], theme["color0"])
        ),
        desc="Dmenu Launcher"
    ),
    Key(
        [mod], "Tab", lazy.next_layout(),
        desc="Toggle between layouts"
    ),
    Key(
        [mod], "w", lazy.window.kill(),
        desc="Kill focused window"
    ),
    Key(
        [mod, "mod1"], "l", lazy.spawn("light-locker-command -l"),
        desc="Lock the session."
    ),
    Key(
        [mod, "mod1"], "r", lazy.restart(),
        desc="Restart qtile"
    ),
    Key(
        [mod, "mod1"], "q", lazy.shutdown(),
        desc="Shutdown qtile"
    ),

    # Switch between windows in current stack pane
    Key(
        [mod], "j", lazy.layout.down(),
        desc="Move focus down in stack pane"
    ),
    Key(
        [mod], "k", lazy.layout.up(),
        desc="Move focus up in stack pane"
    ),

    # Resize windows in current stack
    Key(
        [mod], "h", lazy.layout.grow(),
        desc="Grow window"
    ),
    Key(
        [mod], "l", lazy.layout.shrink(),
        desc="Shrink window"
    ),

    # Window Properties
    Key(
        [mod], "n", lazy.layout.normalize(),
        desc="Normalize window"
    ),
    Key(
        [mod], "m", lazy.layout.maximize(),
        desc="Toggle window between minimum and maximum sizes"
    ),
    Key(
        [mod, "control"], "f", lazy.window.toggle_floating(),
        desc="Toggle floating"
    ),
    Key(
        [mod, "control"], "m", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen"
    ),

    # Move windows up or down in current stack
    Key(
        [mod, "control"], "j", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "
    ),
    Key(
        [mod, "control"], "k", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "
    ),


    # Treetab controls
    Key(
        [mod, "control"], "h", lazy.layout.move_left(),
        desc="Move up a section in treetab"
    ),
    Key(
        [mod, "control"], "l", lazy.layout.move_right(),
        desc="Move down a seciton in treetab"
    ),

    # Panes
    Key(
        [mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"
    ),

    # Split Stack
    Key(
        [mod, "control"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"
    ),

    # Launch Applications (ALT + SHIFT)
    Key([mod, "shift"], "j", lazy.spawn("joplin"), desc="Launch Joplin"),
    Key([mod, "shift"], "w", lazy.spawn("icecat"), desc="Launch IceCat"),
    Key([mod, "shift"], "k", lazy.spawn("keepassxc"), desc="Launch KeepassXC"),
    Key([mod, "shift"], "m", lazy.spawn("icedove"), desc="Launch IceDove Mail"),
    Key([mod, "shift"], "g", lazy.spawn("gimp"), desc="Launch GIMP"),
    Key([mod, "shift"], "e", lazy.spawn("emacs"), desc="Launch Doom Emacs"),
    Key([mod, "shift"], "v", lazy.spawn("virt-manager"), desc="Launch Virt-Manager"),
    Key([mod, "shift"], "i", lazy.spawn(terminal + " irssi"), desc="Launch IRSSI"),
]

my_groups = [   ('WEB', {'layout': 'monadtall'}),
                ('ADM', {'layout': 'monadwide'}),
                ('CODE',{'layout': 'monadwide'}),
                ('DEV',{'layout': 'monadtall'}),
                ('VIRT',{'layout': 'treetab'}),
                ('CHAT',{'layout': 'treetab'}),
                ('GFX',{'layout': 'monadtall'}),
                ('UTILS',{'layout': 'treetab'}),
]

groups = [ Group(name, **kwargs) for name, kwargs in my_groups ]

# Groups keybindings
group_key = 1
for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(group_key), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(group_key), lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),

        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),

    ])
    group_key += 1

my_layout = {   "border_width": 2,
                "margin": 10,
                "border_focus": theme["color12"],
                "border_normal": theme["color8"]
}

layouts = [
    layout.Max(),
    #layout.Stack(num_stacks=2, **my_layout),
    # Try more layouts by unleashing below layouts.
    #layout.Bsp(**my_layout),
    #layout.Columns(**my_layout),
    #layout.Matrix(**my_layout),
    layout.MonadTall(**my_layout),
    layout.MonadWide(**my_layout),
    #layout.RatioTile(**my_layout),
    #layout.Tile(**my_layout),
    layout.TreeTab(
        font = "Ubuntu Bold",
        fontsize = 12,
        padding_y = 5,
        panel_width = 250,
        active_bg = theme["active_tab_background"],
        active_fg = theme["active_tab_foreground"],
        inactive_bg = theme["inactive_tab_background"],
        inactive_fg = theme["inactive_tab_foreground"],
        section_fg = theme["color3"],
        bg_color = theme["background"],
    ),
    #layout.VerticalTile(**my_layout),
    #layout.Zoomy(**my_layout),
    layout.Floating(**my_layout),
]

widget_defaults = dict(
    font = 'Ubuntu Bold',
    fontsize = 12,
    padding = 1,
    background = theme["background"],
)
extension_defaults = widget_defaults.copy()

def init_widgets():
    return [
        widget.Sep(linewidth=0, padding=10),
        widget.TextBox(
            font='FiraCode Nerd Font',
            fontsize = 16,
            padding = 5,
            text='',
            foreground = theme["color4"],
        ),
        widget.Sep(linewidth=0, padding=10),
        widget.GroupBox(
            font = "Ubuntu Bold",
            padding_x = 3,
            margin_y = 5,
            disable_drag = True,
            active = theme["color2"],
            inactive = theme["color8"],
            highlight_method = "line",
            highlight_color = theme["selection_background"],
            this_current_screen_border = theme["color1"],
            this_screen_border = theme["color1"],
            other_current_screen_border = theme["color0"],
            other_screen_border = theme["color0"],
        ),
        widget.Prompt(
            foreground = theme["color3"],
            prompt = 'Run  ',
            padding = 10,
        ),
        widget.Sep(linewidth=0, padding=10),
        widget.WindowName(
            font='FiraCode Nerd Font Bold',
            padding=0,
            foreground = theme["color6"],
            fmt=': {}',
        ),
        # Widgets below are for main monitor only.
        widget.Sep(linewidth=0, padding=10),
        widget.TextBox(
            text = '',
            foreground = theme["color4"],
            padding = 0,
            width = 31,
            fontsize = 75,
        ),
        widget.TextBox(
            text = '',
            foreground = theme["color0"],
            background = theme["color4"],
            padding = 6,
            fontsize = 20,
        ),
        widget.CurrentLayout(
            background = theme["color4"],
            foreground = theme["color0"],
            padding = 6,
        ),
        widget.TextBox(
            text = '',
            foreground = theme["color12"],
            background = theme["color4"],
            padding = 0,
            width = 31,
            fontsize = 75,
        ),
        widget.TextBox(
            text = '',
            foreground = theme["color0"],
            background = theme["color12"],
            padding = 6,
            fontsize = 20,
        ),
        widget.CheckUpdates(
                foreground = theme["color0"],
                background = theme["color12"],
                colour_have_updates = theme["color0"],
                colour_no_updates = theme["color0"],
                fmt = '{}',
                display_format = 'Updates: {updates}',
                no_update_string = 'No Updates',
                distro = 'Arch',
                update_interval = 60,
        ),
        widget.TextBox(
            text = '',
            foreground = theme["color4"],
            background = theme["color12"],
            padding = 0,
            width = 31,
            fontsize = 75,
        ),
        widget.TextBox(
            text = '',
            foreground = theme["color0"],
            background = theme["color4"],
            padding = 6,
            fontsize = 20,
        ),
        widget.CPU(
            foreground = theme["color0"],
            background = theme["color4"],
            format = '{freq_current}GHz {load_percent}%',
            padding = 6,
        ),
        widget.TextBox(
            text = '',
            foreground = theme["color12"],
            background = theme["color4"],
            padding = 0,
            width = 31,
            fontsize = 75,
        ),
        widget.TextBox(
            text = '',
            foreground = theme["color0"],
            background = theme["color12"],
            padding = 6,
            fontsize = 20,
        ),
        widget.Memory(
                foreground = theme["color0"],
                background = theme["color12"],
        ),
        widget.TextBox(
            text = '',
            foreground = theme["color4"],
            background = theme["color12"],
            padding = 0,
            width = 31,
            fontsize = 75,
        ),
        widget.TextBox(
            text = '',
            foreground = theme["color0"],
            background = theme["color4"],
            padding = 6,
            fontsize = 20,
        ),
        widget.ThermalSensor(
            foreground = theme["color0"],
            background = theme["color4"],
            foreground_alert = theme["color7"],
            fmt = 'CPU Temp: {}',
            tag_sensor = "CPUTIN",
            padding = 6,
        ),
        widget.TextBox(
            text = '',
            foreground = theme["color12"],
            background = theme["color4"],
            padding = 0,
            width = 31,
            fontsize = 75,
        ),
        widget.TextBox(
            text = '',
            foreground = theme["color0"],
            background = theme["color12"],
            padding = 6,
            fontsize = 20,
        ),
        widget.Clock(
            foreground = theme["color0"],
            background = theme["color12"],
            format = ' %A, %B %d [ %I:%M %p ]',
        ),
        widget.Sep(linewidth=0, padding=10, background=theme["color12"]),
    ]

screens = [
    Screen(top=bar.Bar(init_widgets(), size=24)),       # Center Monitor
    Screen(top=bar.Bar(init_widgets()[:11], size=24)),  # Left Monitor
    Screen(top=bar.Bar(init_widgets()[:11], size=24)),  # Right Monitor
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
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# Run when starting qtile
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/init.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
