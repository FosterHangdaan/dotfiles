#  ______ _    _ 
# |  ____| |  | |
# | |__  | |__| | Author:		Foster Hangdaan
# |  __| |  __  | Website:	www.fosterhangdaan.com
# | |    | |  | | Github:		https://github.com/FosterHangdaan
# |_|    |_|  |_|
#
# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
umask 022

# set custom path for Starship configuration file
#if [ -r "/path/to/config" ] ; then
#	export STARSHIP_CONFIG="/path/to/config"
#fi

if [ -n "$BASH_VERSION" ]; then
	if [ -r "$HOME/.bashrc" ]; then
		. "$HOME/.bashrc"
	fi
fi

# Custom ENV Variables
export TZ='America/Toronto'

# set favourite editor
if [ -x '/usr/bin/vim' ]; then
	export EDITOR='/usr/bin/vim'
fi


# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ]; then
  PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ]; then
  PATH="$HOME/.local/bin:$PATH"
fi

# XDG Base Directory Specification
# More information at https://specifications.freedesktop.org
# and at https://wiki.archlinux.org/index.php/XDG_Base_Directory
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_CACHE_HOME="$HOME/.cache"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_STATE_HOME="$HOME/.local/state"

# Rust
export RUSTUP_HOME="$XDG_DATA_HOME/rustup"
export CARGO_HOME="$XDG_DATA_HOME/cargo"
if [ -d "$CARGO_HOME/bin" ]; then
	PATH="$PATH:$CARGO_HOME/bin"
fi

# Doom Emacs
############
#export EMACSDIR="$XDG_DATA_HOME/emacs"
# Emacs needs to know the location of the new data directory.
#export EMACS_USER_DIRECTORY="$EMACSDIR"

#export DOOMLOCALDIR="$XDG_DATA_HOME/emacs/doom"
export DOOMDIR="$XDG_CONFIG_HOME/doom"


# set PATH so it includes Doom Emacs bin if it exists
if [ -d "$HOME/.emacs.d/bin" ]; then
  PATH="$HOME/.emacs.d/bin:$PATH"
fi
