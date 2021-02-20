from typing import List  # noqa: F401

import os, subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "kitty"

# Monokai Color Theme
colors = {  "black":    "1a1a1a",
            "white":    "f6f6ef",
            "dark":     "625e4c",
            "grey":     "c4c5b5",
            "red":      "f4005f",
            "green":    "98e024",
            "orange":   "fd971f",
            "yellow":   "e0d561",
            "purple":   "9d65ff",
            "blue":     "58d1eb",
}

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Resize windows in current stack
    Key([mod], "h", lazy.layout.grow(),
        desc="Grow window"),
    Key([mod], "l", lazy.layout.shrink(),
        desc="Shrink window"),

    # Window Properties
    Key([mod], "n", lazy.layout.normalize(),
        desc="Normalize window"),
    Key([mod], "m", lazy.layout.maximize(),
        desc="Toggle window between minimum and maximum sizes"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(),
        desc="Toggle floating"),
    Key([mod, "shift"], "m", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    #Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
    #    desc="Toggle between split and unsplit sides of stack"),

    # Main Keybindings
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "control"], "Return", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(["mod1", "control"], "l", lazy.spawn("light-locker-command -l"), desc="Lock the session."),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),

    # Launch Applications (MOD + ALT)
    Key(["mod1", "shift"], "j", lazy.spawn("joplin"), desc="Launch Joplin"),
    Key(["mod1", "shift"], "w", lazy.spawn("icecat"), desc="Launch IceCat"),
    Key(["mod1", "shift"], "k", lazy.spawn("keepassxc"), desc="Launch KeepassXC"),
    Key(["mod1", "shift"], "m", lazy.spawn("icedove"), desc="Launch IceDove Mail"),
    Key(["mod1", "shift"], "g", lazy.spawn("gimp"), desc="Launch GIMP"),
    Key(["mod1", "shift"], "v", lazy.spawn("virt-manager"), desc="Launch Virt-Manager"),
    Key(["mod1", "shift"], "i", lazy.spawn(terminal + " irssi"), desc="Launch IRSSI"),
]

my_groups = [   ('WEB', {'layout': 'monadtall'}),
                ('ADM', {'layout': 'treetab'}),
                ('CODE',{'layout': 'monadtall'}),
                ('DEV',{'layout': 'monadwide'}),
                ('VIRT',{'layout': 'treetab'}),
                ('CHAT',{'layout': 'monadtall'}),
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
                "border_focus": "f4005f",
                "border_normal": "1D2330"
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
        active_bg = colors["red"],
        active_fg = colors["white"],
        inactive_bg = colors["dark"],
        inactive_fg = colors["white"],
        section_fg = colors["yellow"],
        bg_color = colors["black"],
    ),
    #layout.VerticalTile(**my_layout),
    #layout.Zoomy(**my_layout),
    layout.Floating(**my_layout),
]

widget_defaults = dict(
    font='Ubuntu Bold',
    fontsize=12,
    padding=1,
    background=colors["black"],
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
            foreground=colors["red"],
        ),
        widget.Sep(linewidth=0, padding=10),
        widget.GroupBox(
            font = "Ubuntu Bold",
            padding_x = 3,
            margin_y = 5,
            disable_drag = True,
            active = colors["green"],
            inactive = colors["grey"],
            highlight_method = "line",
            highlight_color = colors["dark"],
            this_current_screen_border = colors["red"],
            this_screen_border = colors["red"],
            other_current_screen_border = colors["black"],
            other_screen_border = colors["black"],
        ),
        widget.Prompt(
            foreground = colors["orange"],
            prompt = 'Run  ',
            padding = 10,
        ),
        widget.Sep(linewidth=0, padding=10),
        widget.WindowName(
            font='FiraCode Nerd Font Bold',
            padding=0,
            foreground=colors["blue"],
            fmt=': {}',
        ),
        # Widgets below are for main monitor only.
        widget.Sep(linewidth=0, padding=10),
        widget.TextBox(
            text = '',
            foreground = colors["red"],
            padding = 0,
            width = 31,
            fontsize = 75,
        ),
        widget.TextBox(
            text = '',
            foreground = colors["black"],
            background = colors["red"],
            padding = 6,
            fontsize = 20,
        ),
        widget.CurrentLayout(
            background = colors["red"],
            foreground = colors["black"],
            padding = 6,
        ),
        widget.TextBox(
            text = '',
            foreground = colors["yellow"],
            background = colors["red"],
            padding = 0,
            width = 31,
            fontsize = 75,
        ),
        widget.TextBox(
            text = '',
            foreground = colors["black"],
            background = colors["yellow"],
            padding = 6,
            fontsize = 20,
        ),
        widget.CheckUpdates(
                foreground = colors["black"],
                background = colors["yellow"],
                colour_have_updates = colors["black"],
                colour_no_updates = colors["black"],
                fmt = '{}',
                display_format = 'Updates: {updates}',
                no_update_string = 'No Updates',
                distro = 'Arch',
                update_interval = 60 * 10,
        ),
        widget.TextBox(
            text = '',
            foreground = colors["red"],
            background = colors["yellow"],
            padding = 0,
            width = 31,
            fontsize = 75,
        ),
        widget.TextBox(
            text = '',
            foreground = colors["black"],
            background = colors["red"],
            padding = 6,
            fontsize = 20,
        ),
        widget.CPU(
            foreground = colors["black"],
            background = colors["red"],
            format = '{freq_current}GHz {load_percent}%',
            padding = 6,
        ),
        widget.TextBox(
            text = '',
            foreground = colors["yellow"],
            background = colors["red"],
            padding = 0,
            width = 31,
            fontsize = 75,
        ),
        widget.TextBox(
            text = '',
            foreground = colors["black"],
            background = colors["yellow"],
            padding = 6,
            fontsize = 20,
        ),
        widget.Memory(
                foreground = colors["black"],
                background = colors["yellow"],
        ),
        widget.TextBox(
            text = '',
            foreground = colors["red"],
            background = colors["yellow"],
            padding = 0,
            width = 31,
            fontsize = 75,
        ),
        widget.TextBox(
            text = '',
            foreground = colors["black"],
            background = colors["red"],
            padding = 6,
            fontsize = 20,
        ),
        widget.ThermalSensor(
            foreground = colors["black"],
            background = colors["red"],
            foreground_alert = colors["white"],
            fmt = 'CPU Temp: {}',
            tag_sensor = "CPUTIN",
            padding = 6,
        ),
        widget.TextBox(
            text = '',
            foreground = colors["yellow"],
            background = colors["red"],
            padding = 0,
            width = 31,
            fontsize = 75,
        ),
        widget.TextBox(
            text = '',
            foreground = colors["black"],
            background = colors["yellow"],
            padding = 6,
            fontsize = 20,
        ),
        widget.Clock(
            foreground = colors["black"],
            background = colors["yellow"],
            format = ' %A, %B %d [ %I:%M %p ]',
        ),
        widget.Sep(linewidth=0, padding=10, background=colors["yellow"]),
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
