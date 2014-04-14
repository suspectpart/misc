# Vim Commands

# Startup

**ls -l | vim -** (pipe stuff into a new vim buffer)   
**vim -p file3 file2 file3** (open files in tabbed mode)   
**vim -n file** (don't create a swap file; e.g. when you handle sensitive data)  
**vim -M file** (non-modifiable mode; read files safely without being able to modify them)  

# Commands
**:! <shell-command>** (run a shell command)  
**:w ! <shell-command>** (pipe current buffer into shell command)  

# Working with Tabs
**:tabe file** (open file in tab)   
**:tab new** (open new, empty tab)  
**:tab close** (close current tab)  
**:tabs** (list tabs)  
**:q** (close current tab)  
**gt** (go to next tab)  
**gT** (go to previous tab)  

# Working with Windows
**ctrl\w n** (open a new window horizontally)  
**ctrl\w v**(open a new window vertically)  
**ctrl\w h/j/k/l** (change window in given direction)  
**:q** (close current window)  
