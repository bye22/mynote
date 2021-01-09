ag.vim                    
gruvbox.vim               
unite-gtags.vim
asyncomplete-buffer.vim   
java_getset.vim           
unite-radio.vim
asyncomplete-clang.vim    
jedi-vim.vim              
unite.vim
asyncomplete-necovim.vim  
LeaderF.vim               
vim-airline.vim
asyncomplete-omni.vim     
neocomplcache.vim         
vim-expand-region.vim
asyncomplete.vim          
neocomplete.vim           
vimfiler.vim
completor.vim             
neomake.vim               
vim-grepper.vim
ctrlp.vim                 
neosnippet.vim            
vim-gutentags.vim
ctrlsf.vim                
nerdcommenter.vim         
vim-javacomplete2.vim
defx-git.vim              
nerdtree.vim              
vim-multiple-cursors.vim
defx.vim                  
open-browser.vim          
vim-ref.vim
denite.vim                
phpcomplete-extended.vim  
vim-signify.vim
deoplete-clang.vim        
syntastic.vim             
vim-startify.vim
deoplete.vim              
tagbar.vim
goyo.vim                  
taglist.vim




" Nerd Tree Setup<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
map <C-h> :NERDTreeToggle<CR>
"当打开vim且没有文件时自动打开NERDTree
"autocmd vimenter * NERDTree
" 只剩 NERDTree时自动关闭
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
"列出当前目录文件  
map <F3> :NERDTreeToggle<CR>
imap <F3> <ESC> :NERDTreeToggle<CR>
"打开树状文件目录  
map <C-F3> \be  
" Nerd Tree Setup end>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>