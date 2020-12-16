filetype plugin indent on
set tabstop=4
set shiftwidth=4
set expandtab
set rnu nu
set nowrap
set noswapfile

let mapleader = ","

imap jk <esc>:w<cr>
"map <leader>3 :!mono %:r.exe<cr>
"
map <leader>3 :term mono %:r.exe<cr>i
map <leader># :!csc %<cr>

map <leader>4 :term java %:r<cr>i
map <leader>$ :!javac %<cr>

map <C-b> <C-^>

inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
inoremap {<CR> {<CR>}<ESC>O
inoremap {;<CR> {<CR>};<ESC>O

map <Leader>c "*y
map <Leader>C "+y
map <Leader>v "*p
map <Leader>V "+p

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
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    Plug 'sheerun/vim-polyglot'
    Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
    Plug 'preservim/nerdcommenter'
    Plug 'mattn/emmet-vim'
    Plug 'OmniSharp/omnisharp-vim'
    Plug 'dense-analysis/ale'
                                                          
call plug#end()                                           
                                                          
nmap <C-P> :FZF<CR>                                       
"command! -nargs=0 Prettier :call CocAction('runCommand', 'prettier.formatFile')

"fzf
let g:fzf_preview_window = 'right:60%'

"emmet
let g:user_emmet_leader_key=','

let g:ale_linters = {
\ 'cs': ['OmniSharp']
\}
                                                          
