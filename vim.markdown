# Vim Commands

# Startup

**ls -l | vim -** (pipe stuff into a new vim buffer)  
**vim -p file3 file2 file3** (open files in tabbed mode)  
**vim -n file** (don't create a swap file; e.g. when you handle sensitive data)  
**vim -M file** (non-modifiable mode; read files safely without being able to modify them)  

# Commands
**:! <shell-command>** (run a shell command)
**:w ! <shell-command>** (pipe current buffer into shell command)
