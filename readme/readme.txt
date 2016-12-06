Plugin for CudaText.
Gives some commands for Stata lexer. 
First, install "Stata" lexer from addons: Plugins - Addons Manager - Install.

-------
Command: Plugins - Stata Helper - Execute current text
  Runs in Stata: selected text, or current line of 1st caret, if none selected.

-------
Command: Plugins - Stata Helper - Insert break-line
  Insert commented line like this:
  /* ------ break line ------ (by Stata Helper) */

-------
Command: Plugins - Stata Helper - Execute block between break-lines
  Runs in Stata: lines inside nearest break-lines (inserted before).

-------
Commands:
  Plugins - Stata Helper - Make selected as `word'
  Plugins - Stata Helper - Make selected as ${word}
  These converts selected word like shown.
  
-------
Event: pressing of `-char (tick-char) makes selected text quoted:
  aabb --> `aabb'
