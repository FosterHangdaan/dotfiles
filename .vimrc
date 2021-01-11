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

" Allows you to re-use the same window and switch from an unsaved buffer
" without saving it first. Also allows you to keep an undo history for
" multiple files when re-using the same window in this way. Note that using
" persistent undo also lets you undo in multiple files even in the same
" window, but is less efficient and is actually designed for keeping undo
" history after losing Vim entirely. Vim will complain if you try to quit
" without saving, and swap files will keep you safe if your computer crashes.
set hidden

" Allow backspacing over autoindent, line breaks and start of insert action.
set backspace=indent,eol,start

" When opening a new lien and no filetype-specific indenting is enabled, keep
" the same indent as the line you're currently on. Useful for READMEs, etc.
set autoindent

" Always display the status line, even if only one windoe is displayed.
set laststatus=2

" Enable use of the mouse for all modes
"set mouse=a

" Display line numbers on the left
set number

" Default indentation
set tabstop=2
set shiftwidth=2

" Set a vim-airline theme
let g:airline_theme='base16_monokai'

" Mappings
" -------------------------------------------------------------------------------------------


" Plugins
" -------------------------------------------------------------------------------------------

" VIM AIRLINE
" -----------
" Enable vim-airline fonts
let g:airline_powerline_fonts = 1

" Display all buffers when there is only one tab open
let g:airline#extensions#tabline#enabled = 1

" Choose the path format when tabline status (above) is enabled.
let g:airline#extensions#tabline#formatter = 'unique_tail'
