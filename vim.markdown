[TOC]
# Vim Commands

## Startup
**ls -l | vim -** (pipe stuff into a new vim buffer)   
**vim -p file3 file2 file3** (open files in tabbed mode)   
**vim -n file** (don't create a swap file; e.g. when you handle sensitive data)  
**vim -M file** (non-modifiable mode; read files safely without being able to modify them)  

## Navigation (Normal Mode)
**h,j,k,l** (left, down, up, right)  
**gg** (beginning of document)  
**G** (end of document)  
**30G** (go to line 30)  
**w** (go to beginning of next word (C style))  
**W** (go to beginning of next word (Text style))  
**b** (go to beginning of previous word)   
**e** (go to end of next word)  
**30j** (jump 30 lines down)   
**f <char>** (go to next occurence of <char> in this line)   
**5f <char>** (go to fith occurence of <char> in this line)  
**t <char>** (place cursor before next occurence of <char> in this line)  
**5t <char>** (place cursor before fifth occurence of <char> in this line)  
**H** (move cursor to top of the screen)  
**M** (move curstor to middle of the screen)  
**L** (move cursor to end of the screen)  
**0** (move cursor to beginning of line)  
**^** (move cursor to first non-empty character of line)  
**$** (move cursor to end of line)  

## Text Manipulation (Normal Mode)
**dd** (cut one line)  
**5dd** (cut 5 lines)  
**yy** (copy current line)  
**Y** (copy current line)  
**5yy** (copy 5 lines)  
**p** (paste copied lines in next line)    
**P** (paste copied lines in this line)  
**D** (tail line - delete from cursor to end of line)  
**J** (join line under cursor with next line, adding 1 or 2 spaces)  
**u** (undo last change)  
**x** (delete character under cursor)  
**5x** (delete 5 chars beginning with cursor)      
**~** (swap case of character under cursor)  
**5~~** (swap case of character under cursor + 4)  

## Text Manipulation (Entering Insert Mode)
**c** 

## Search and Replace (in command mode)  
**:/pattern** (search for pattern downwards)  
**:?pattern** (search for pattern upwards)  
**:n** (go to next match)  
**:N** (go to previous match)  
**:$ s/pattern/replacement/** (replace pattern with replacement in last line)  
**:0 s/pattern/replacement/** (replace pattern with replacement in first line)  
**:% s/pattern/replacement/** (replace pattern with replacement in whole file)  
**:7,9 s/pattern/replacement/** (replace pattern with replacement in range from line 7 to line 9)  
**:2,+5 s/pattern/replacement/** (replace pattern with replacement in range from line 2 plus 5 lines)  
**:17,$ s/pattern/replacement/** (replace pattern with replacement in range from line 17 through the last line)  
**:s/pattern/replacement/g** (replace all matches in a line)  

## Read and write files
**:r file** (read file content into current buffer)  
**:w** (save current buffer)  
**:w file** (save current buffer to given file)  

## Issue shell commands
**:! <shell-command>** (run a shell command)  
**:w ! <shell-command>** (pipe current buffer into shell command)  
**:r ! <shell-command>** (pipe output of shell command into current file  
**:sh** (open a new shell instance; exit returns to vim)  

## Working With Buffers
**:e file** (open file to edit in new buffer)  
**:b 1** (jump to buffer 1)  
**:bdelete** (delete current buffer)  

## Working with Tabs
**:tab new** (open new, empty tab)  
**:tabe file** (open file in tab)   
**:tab close** (close current tab)  
**:tabs** (list tabs)  
**:q** (close current tab)  
**gt** (go to next tab)  
**gT** (go to previous tab)  

## Working with Windows
**ctrl\w n** (open a new window horizontally)  
**ctrl\w s** (open samle file in new window horizontally)  
**ctrl\w v**(open same file in new window vertically)  
**ctrl\w h/j/k/l** (change window in given direction)  
**ctrl\w gf** (open file under cursor in new window)  
**:q** (close current window)  

## Abbreviations
**:ab hs Horst Schneider** (replace all occurences of abbreviation hs with Horst Schneider)  
**:una hs** (unabbreviate hs)  
**:abc** (clear all abbreviations)  

## Entering Visual Mode
**v** (Enter visual mode, selecting characters and lines)  
**shift\v** (Enter visual mode, selecting whole lines)  
**ctrl\v** (Enter visual mode, selecting blocks)  

## Misc
**:Ex** (open file explorer)  
