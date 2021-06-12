"  ______ _    _ 
" |  ____| |  | |
" | |__  | |__| | Author:   Foster Hangdaan
" |  __| |  __  | Website:  https://www.fosterhangdaan.com
" | |    | |  | | Github:   https://github.com/FosterHangdaan
" |_|    |_|  |_|
"
" Personalized VIM experience just for me.
"
" To source this file, place the line below to ~/.vimrc:
" so /path/to/source

" -------------------------------------------------------------------------------------------
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

" Display hybrid line numbers on the left
set number relativenumber

" Default indentation
set tabstop=2
set shiftwidth=2

" Automatically resize splits when window size changes.
"autocmd VimResized * wincmd =

" Highlight the current line
set cursorline

" Enable code folding
set foldmethod=indent
set foldlevelstart=1

" Change cursor on mode
"let &t_SI = "\<Esc>[6 q"
"let &t_SR = "\<Esc>[4 q"
"let &t_EI = "\<Esc>[2 q"

" Show indent lines
"set listchars=tab:\|\ 
"set list

" -------------------------------------------------------------------------------------------
" Theming
" -------------------------------------------------------------------------------------------
" Set cursor line and cursor column colors
highlight CursorLineNR cterm=NONE
highlight CursorLine cterm=NONE ctermbg=236
highlight CursorColumn cterm=NONE ctermbg=236
highlight VertSplit ctermfg=7 ctermbg=7 cterm=none

" -------------------------------------------------------------------------------------------
" Functions
" -------------------------------------------------------------------------------------------
function! RelativeNumbersToggle()
	:set relativenumber!
endfunction


" -------------------------------------------------------------------------------------------
" Mappings
" -------------------------------------------------------------------------------------------
nnoremap <SPACE> <Nop>
let mapleader=' '

" Buffers
map <leader>i :bn<cr>
map <leader>u :bp<cr>
map <leader>bq :bd<cr>
map <leader>b :buffers <cr>:buffer<space>

" Tabs
map <leader>t :tabnew<cr>
map <leader>o :tabnext<cr>
map <leader>y :tabprev<cr>
map <leader>tq :tabclose<cr>

" Switch windows
map <leader>h :wincmd h<cr>
map <leader>l :wincmd l<cr>
map <leader>j :wincmd j<cr>
map <leader>k :wincmd k<cr>

" Move windows
map <leader>H <C-w>H<cr>
map <leader>L <C-w>L<cr>
map <leader>J <C-w>J<cr>
map <leader>K <C-w>K<cr>

" Splits
" -----------
" Remove pipes (|) on the border of split windows
"set fillchars+=vert:\

" Split window
map <leader>v :vsplit<cr>
map <leader>s :split<cr>

" Resize window
map <leader>] 3 :wincmd +<cr>
map <leader>[ 3 :wincmd -<cr>
map <leader>, 3 :wincmd <<cr>
map <leader>. 3 :wincmd ><cr>

" Swap splits
map <leader>R <C-w>R<cr>

" Equalize split
map <leader>= <C-w>=<cr>

" Maximize horizontal split.
map <leader>_ <C-w>_<cr>

" Maximize vertical split.
map <leader>\| <C-w>\|<cr>

" Close Window
map <leader>wq <C-w>c<cr>

" Change 2 split windows from vert to horiz and vice-versa
map <leader>V <C-w>t<C-w>K
map <leader>S <C-w>t<C-w>H

" NERDTree
" -----------
map <C-p> :NERDTreeToggle<cr>
map <leader>n :NERDTreeFocus<cr>

" Toggle Relative Line Numbers
" -----------
map <leader>r :call RelativeNumbersToggle()<cr>

" Save
" -----------
"map <leader>w : w<cr>

" Quit
"map <leader>q : q<cr>

" -------------------------------------------------------------------------------------------
" Plugins
" -------------------------------------------------------------------------------------------

" VIM AIRLINE
" -----------
" Enable vim-airline fonts
let g:airline_powerline_fonts = 1

" Set a vim-airline theme
let g:airline_theme='base16_monokai'

" Display all buffers when there is only one tab open
let g:airline#extensions#tabline#enabled = 1

" Choose the path format when tabline status (above) is enabled.
let g:airline#extensions#tabline#formatter = 'unique_tail'
