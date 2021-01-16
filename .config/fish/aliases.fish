#  ______ _    _ 
# |  ____| |  | |
# | |__  | |__| | Author:		Foster Hangdaan
# |  __| |  __  | Website:	www.fosterhangdaan.com
# | |    | |  | | Github:		https://github.com/FosterHangdaan
# |_|    |_|  |_|
#
# FISH Shortcuts to ease life in a terminal.

if command -qs lsd
	# Listing configs
	alias ls    'lsd --group-dirs first'
	alias lsl   'lsd --group-dirs first -l'
	alias tree	'lsd --group-dirs first --tree'

	# Lazy Admin
	function cds
		cd $argv[1]; and ls
	end
end

# Connect to my personal FTP Server.
alias myftp 'lftp foster@ftp.fhang.lan'

# Backup home directory to NAS.
alias synchome "rsync -ah --compress --progress --delete --delete-excluded --exclude='Downloads' --exclude='.cache' $HOME/ silentcartographer:/srv/backups/foster/home/"

# Perform virus scan on home directory.
alias scanhome "clamscan -ri $HOME"

# Manage common configuration (dotfiles) via bare git repo
# The bare repo is at ~/.commfig
alias dotfiles "git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME"

# Package Manager
if command -qs pacman
	alias pminstall	'sudo pacman -S'
	alias pmremove	'sudo pacman -Rs'
	alias pmupgrade	'sudo pacman -Syu'
	alias pmsearch	'pacman -Ss'
	alias pminfo		'pacman -Si'
else if command -qs apt
	alias pminstall	'sudo apt install'
	alias pmremove	'sudo apt remove'
	alias pmpurge		'sudo apt purge'
	alias pmupdate	'sudo apt update'
	alias pmupgrade	'sudo apt update && sudo apt upgrade'
	alias pmsearch	'apt search'
	alias pminfo		'apt info'
end

# Who needs etcher?
function etch
	sudo dd if=$argv[1] of=$argv[2] bs=8M status=progress
end

# Warn me when I'm overwriting files.
alias cp 'cp -i'
alias mv 'mv -i'
