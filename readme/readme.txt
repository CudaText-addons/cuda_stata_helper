Plugin for CudaText.
Gives some commands for Stata lexer. 
First, install "Stata" lexer from addons: Plugins - Addons Manager - Install.


1) Event: pressing of `-char (tick-char) makes selected text quoted:
  aabb --> `aabb'
  
2) Command: Plugins - Stata Helper - Execute current text
Runs selected text (or current line of 1st caret, if none selected) in Stata.
