"  ______ _    _ 
" |  ____| |  | |
" | |__  | |__| | Author:		Foster Hangdaan
" |  __| |  __  | Website:	www.fosterhangdaan.com
" | |    | |  | | Github:		https://github.com/FosterHangdaan
" |_|    |_|  |_|
"
" Personalized VIM experience just for me.
"
" To source this file, place the line below to ~/.vimrc:
" so /path/to/source

" General Settings
" -------------------------------------------------------------------------------------------
" Set 'nocompatible' to ward off unexptected things that your distro might
" have made, as well as sanely reset options when re-sourcing .vimrc
set nocompatible

" Attempt to determine the type of a file based on its name and possible its
" contents. Use this to alow intelligent aut-indenting for each filetype,
" and for plugins that are filetype specific.
filetype indent plugin on

" Enable syntax highlighting
syntax on

" Better command line completion
set wildmenu

" Allow backspacing over autoindent, line breaks and start of insert action.
set backspace=indent,eol,start

" When opening a new lien and no filetype-specific indenting is enabled, keep
" the same indent as the line you're currently on. Useful for READMEs, etc.
set autoindent

" Always display the status line, even if only one windoe is displayed.
set laststatus=2

" Enable use of the mouse for all modes
set mouse=a

" Display line numbers on the left
set number

" Indentation
set tabstop=2
set shiftwidth=2

" Mappings
" -------------------------------------------------------------------------------------------


" Plugins
" -------------------------------------------------------------------------------------------

" Enable vim-airline
if filereadable("/usr/share/vim/registry/vim-airline.yaml")
	let g:airline_powerline_fonts = 1
endif
