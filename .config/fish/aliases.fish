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
	alias ls    'lsd'
	alias lsl   'lsd -l'
	alias tree	'lsd --tree'

	# Lazy Admin
	function cds
		cd $1; and lsd
	end
end

# Connect to my personal FTP Server.
alias myftp 'lftp foster@ftp.fhang.lan'

# Backup home directory to NAS.
alias synchome "rsync -ah --progress --delete --delete-excluded --exclude='Downloads' $HOME/ silentcartographer:/srv/backups/foster/home/"

# Perform virus scan on home directory.
alias scanhome "clamscan -ri $HOME"

# Manage common configuration (dotfiles) via bare git repo
# The bare repo is at ~/.commfig
alias commfig "git --git-dir=$HOME/.commfig/ --work-tree=$HOME"
