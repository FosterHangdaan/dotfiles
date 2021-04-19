#  ______ _    _ 
# |  ____| |  | |
# | |__  | |__| | Author:		Foster Hangdaan
# |  __| |  __  | Website:	www.fosterhangdaan.com
# | |    | |  | | Github:		https://github.com/FosterHangdaan
# |_|    |_|  |_|
#
# BASH aliases that ease my life in the shell terminal.

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
#alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# ls and cd shortcuts to simplify
# navigation and listing
if command -v lsd > /dev/null ; then
	alias ls='lsd --group-dirs first'
	alias lsa='lsd --group-dirs first -A'
	alias lsl='lsd --group-dirs first -l'
	alias lsla='lsd --group-dirs first -lA'
	alias tree='lsd --tree --group-dirs first'
	cds() {	cd $1 && lsd ; }
else
	cds() {	cd $1 && ls ; }
fi

# Connect to my personal FTP server
alias myftp='lftp foster@ftp.fhang.lan'

# Backup home directory to NAS
alias synchome="rsync -ah --compress --progress --delete --delete-excluded --exclude='Downloads' --exclude='.cache' ${HOME}/ silentcartographer:/srv/backups/foster/home/"

# Perform virus scan on home directory.
alias scanhome="clamscan -ri $HOME"

# For writing images to removeable media.
# My command line version of etcher.
etch () { sudo dd if="$1" of="$2" bs=8M status=progress ; }

# Package Manager
if command -v apt > /dev/null ; then
	pminstall() { sudo apt update && sudo apt install $@ ; }
	pmremove() { sudo apt remove $@ ; }
	pmpurge() { sudo apt purge $@ ; }
	alias pmsearch="apt search"
	alias pminfo="apt info"
	pmupdate() {
		sudo apt update && sudo apt upgrade && sudo apt autoremove
		if [ -e "/var/run/reboot-required.pkgs" ] ; then
			echo "A restart is required to finish updates."
		fi
	}
elif command -v pacman > /dev/null ; then
	pminstall() { sudo pacman -S $@ ; }
	pmremove() { sudo pacman -Rs $@ ; }
	pmupdate() { sudo pacman -Syu ; }
	alias pmsearch="pacman -Ss"
	alias pminfo="pacman -Si"
fi

# Managing dotfiles repo
# The bare repo is at ~/.dotfiles
alias dotfiles='git --git-dir=${HOME}/.dotfiles/ --work-tree=$HOME'

# Font Management
alias listfonts="fc-list | cut -d':' -f1"

# Warn me when I'm overwriting files.
alias cp='cp -i'
alias mv='mv -i'

# Programs
alias monero='monero-wallet-gui'
