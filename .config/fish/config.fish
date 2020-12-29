#  ______ _    _ 
# |  ____| |  | |
# | |__  | |__| | Author:		Foster Hangdaan
# |  __| |  __  | Website:	www.fosterhangdaan.com
# | |    | |  | | Github:		https://github.com/FosterHangdaan
# |_|    |_|  |_|
#
# This configuration file serves as the main entry point for FISH.
# By default, this file is sourced by ~/.config/fish/config.fish

# General Settings
# ----------------------------------------------------------------
# Source alias file if it exists
if test -r ~/.config/fish/aliases.fish
	source ~/.config/fish/aliases.fish
end


# Plugins
# ----------------------------------------------------------------
# Enable Starfish plugin.
if command -qs starship
	starship init fish | source
end


# Greeting
# ----------------------------------------------------------------
# There are multiple ways to set the greeting message in FISH
# Choose only one of the following.

# (1) Define the fish_greeting function.
# This is the recommended method.
#
function fish_greeting
	# Pick the greeting number here
	#set -l select (random 0 2)
	set -l select 1

	if test $select -eq 0; and command -qs figlet; and command -qs lolcat
		figlet 'Foster Hangdaan' | lolcat
	else if test $select -eq 1; and command -qs cowsay; and command -qs fortune; and command -qs lolcat
		fortune -s | cowsay -f (ls /usr/share/cows | shuf -n 1) | lolcat
	else if test $select -eq 2; and command -qs neofetch
			neofetch
	else
		echo "Hello $USER! Welcome to the FISH shell."
	end
end

# (2) Run commands when launching an interactive shell.
#
#if status is-interactive
#	# Only enable one at a time.
#
#	# Neofetch
#	#if command -qs neofetch
#	#	neofetch
#	#end
#
#	# My name in fancy neon text
#	if command -qs figlet; and command -qs lolcat
#		figlet 'Foster Hangdaan' | lolcat
#		echo ''
#		fortune -s | lolcat
#	end
#end


