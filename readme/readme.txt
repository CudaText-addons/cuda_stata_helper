Plugin for CudaText.
Gives some commands for Stata lexer. 
First, install "Stata" lexer from addons: Plugins - Addons Manager - Install.


1) Event: pressing of `-char (tick-char) makes selected text quoted:
  aabb --> `aabb'
  (Needs selected text.)
  
2) Command: Plugins - Stata Helper - Execute current text
  Runs in Stata: selected text, or current line of 1st caret, if none selected.

3) Command: Plugins - Stata Helper - Insert break-line
  Insert commented line like this:
  /* ------ break line ------ (by Stata Helper) */

4) Command: Plugins - Stata Helper - Execute block between break-lines
  Runs in Stata: lines inside nearest break-lines (inserted before).
