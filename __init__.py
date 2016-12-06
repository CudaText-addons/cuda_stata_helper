import re
import subprocess
from cudatext import *


BREAK_LINE = '/* ------ break line ------ (by Stata Helper) */'

def get_stata_version():
    '''
    based on the Stata Enhanced - https://github.com/andrewheiss/SublimeStataEnhanced/
    '''
    cmd = """osascript<< END
                try
                    tell me to get application id "com.stata.stata14"
                    set stata to 14
                end try
                try
                    tell me to get application id "com.stata.stata13"
                    set stata to 13
                end try
                try
                    tell me to get application id "com.stata.stata12"
                    set stata to 12
                end try
                try
                    tell me to get application id "com.stata.stata11"
                    set stata to 11
                end try
                return stata
            END"""
    try:
        version = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError:
        msg_status("Cannot find version of Stata")
        raise Exception("Cannot find version of Stata") 
    version = version.decode("utf-8").strip()
    return((int(version), "com.stata.stata{}".format(version)))

def do_stata_exec(s):
    if not s:
        msg_status('Cannot run empty text')
        return
    msg_status('Running in Stata')
    print('todo: execute Stata text: "'+s+'"')


def do_quote_selected(quote1, quote2):
    s = ed.get_text_sel()
    if s:
        x0, y0, x1, y1 = ed.get_carets()[0]
        #reverse-select: swap coord
        if (y0, x0)>(y1, x1):
            x0, y0, x1, y1 = x1, y1, x0, y0
        s = quote1+s+quote2
        ed.delete(x0, y0, x1, y1)
        ed.insert(x0, y0, s)
        ed.set_caret(
          x0+len(quote1), 
          y0, 
          x1+(len(quote1) if y1==y0 else 0), 
          y1)
        return True



class Command:

    def ins_break_line(self):
        #cannot do with select
        if ed.get_text_sel(): return
        
        x0, y0, x1, y1 = ed.get_carets()[0]
        ed.insert(0, y0, BREAK_LINE+'\n')
        ed.set_caret(0, y0+1)
        msg_status('Inserted break-line')


    def exec_block(self):
        #dont allow sel
        if ed.get_text_sel(): return
        x0, y0, x1, y1 = ed.get_carets()[0]
        
        y_st = y0
        while (y_st>=0) and (ed.get_text_line(y_st)!=BREAK_LINE):
            y_st -= 1
        
        y_end = y0
        while (y_end<ed.get_line_count()-1) and (ed.get_text_line(y_end)!=BREAK_LINE):
            y_end += 1
            
        s = ed.get_text_substr(0, y_st+1, 0, y_end)
        do_stata_exec(s)
        

    def exec_cur(self):
        x0, y0, x1, y1 = ed.get_carets()[0]
        #selected
        s = ed.get_text_sel()
        if not s:
            #curr line
            s = ed.get_text_line(y0)
        do_stata_exec(s)
        
        
    def quote_tick(self):
        do_quote_selected('`', "'")

    def quote_var(self):
        do_quote_selected('${', "}")

    def on_key(self, ed_self, key, state):
        #tick-char
        if key==192:
            if do_quote_selected('`', "'"):
                return False #block char

