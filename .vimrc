set background=dark
set mouse=a
set nu
set relativenumber
set noerrorbells
set belloff=all
set tabstop=4 
set shiftwidth=4
set softtabstop=4 
set expandtab
set smartindent
set nowrap
set incsearch
set noswapfile
set pastetoggle=<F3>
set encoding=utf-8

set cursorline     "highlight current line
set cursorcolumn   "highlight current column

set clipboard=unnamedplus
" cambiar a dos para html
"autocmd BufRead,BufNewFile *.htm,*.html setlocal tabstop=2 shiftwidth=2 softtabstop=2
highlight ColorColumn ctermbg = 0 guibg = lightgrey

let mapleader = ","
map <leader>. :w <ejter> :!cls<enter> :! py % <enter>
map <leader>r :w<cr>:!clear<cr>:!node %<cr>
imap <F5> <esc> :w <enter> :!cls<enter> :! py % <enter>

imap jk <esc>:w<cr>
imap ä <esc>:w<cr>

imap ì <esc>:w<cr> 

xmap <Leader>c "*y
xmap <Leader>C "+y
xmap <Leader>v "*p
xmap <Leader>V "+p

map <leader><tab> ^i<<esc>wv$yA></<esc>pA><esc>bbli
map <leader>html i<!DOCTYPE html><cr><html><cr><head><cr><meta charset="utf-8"><cr><title></title><cr><backspace></head><cr><body><cr></body><cr><backspace></html><esc>gg
imap <leader>lorem iLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum
imap <leader><tab> <esc>I<<esc>wveyA></<esc>pA><esc>bbli
"react function component template
"
map <leader>fr Oimport React from 'react'<cr><esc>jveyo<cr>export default <esc>p<esc>kkIconst <esc>A = (props) => (<esc>
map <leader>n :set nu<cr>
map <leader>N :set nu!<cr>

"sustituir una palabra por otra en una linea 'word/newWord'
map <leader>s kYpjvEyk:s/<c-r>"/g<cr>jdwxA/<esc>
"sustituir una palabra por otra en una linea 'word/newWord'y sustituir linea
map <leader>S ^vEyk:s/<c-r>"/g<cr>j
"sustituir una palabra por otra en todo el file 'word/newWord'
map <leader>ts  kYpjvEyk:%s/<c-r>"/g<cr>

call plug#begin('~/.vim/plugged')
"Plug 'valloric/youcompleteme'       "autocomplition

Plug 'neoclide/coc.nvim', {'branch': 'release'} "autocomplition
Plug 'preservim/nerdtree'           "sidebar for files
Plug 'morhetz/gruvbox'              "colorscheme
Plug 'phanviet/vim-monokai-pro'
Plug 'vim-airline/vim-airline'
Plug 'flazz/vim-colorschemes'
Plug 'turbio/bracey.vim'            "html server
Plug 'preservim/nerdcommenter'      "comment sections of code
Plug 'jiangmiao/auto-pairs'         "double brackets
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } } "Buscar files
Plug 'junegunn/fzf.vim'
Plug 'othree/yajs.vim'
"Plug 'mxw/vim-jsx'
Plug 'mattn/emmet-vim' "write html faster
Plug 'lilydjwg/Colorizer'
Plug 'dense-analysis/ale'           "linting
"Plug 'sheerun/vim-polyglot'         "languages syntax
Plug 'pangloss/vim-javascript'
Plug 'arcticicestudio/nord-vim'     "nord colorscheme


call plug#end()

au FileType javascript setlocal formatprg=prettier
au FileType javascript.jsx setlocal formatprg=prettier
au FileType typescript setlocal formatprg=prettier\ --parser\ typescript
au FileType html setlocal formatprg=js-beautify\ --type\ html
au FileType scss setlocal formatprg=prettier\ --parser\ css
au FileType css setlocal formatprg=prettier\ --parser\ css


"colorscheme gruvbox
colorscheme nord

let g:bracey_refresh_on_save = 1
let g:bracey_auto_start_server = 1
let g:bracey_eval_on_save = 1

"emmet
":

"
"MOVE TROUGH FILES
map <c-b> <c-^>
"NERDTREE
map <leader>t :NERDTree<cr>

"fzf
let g:fzf_preview_window = 'right:60%'
map <c-p> :Files<cr>

"linting
let g:ale_sign_column_always = 1
let g:ale_set_balloons = 1
