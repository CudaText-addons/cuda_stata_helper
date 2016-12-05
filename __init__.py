import re
import subprocess
from cudatext import *


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


class Command:

    def exec_file(self):
        x0, y0, x1, y1 = ed.get_carets()[0]
        #selected
        s = ed.get_text_sel()
        if not s:
            #curr line
            s = ed.get_text_line(y0)
        #debug
        print('todo: execute Stata text:')
        print(s)
        
    def on_key(self, ed_self, key, state):
        #tick-char
        if key==192:
            s = ed.get_text_sel()
            if s:
                x0, y0, x1, y1 = ed.get_carets()[0]
                #reverse-select: swap coord
                if (y0, x0)>(y1, x1):
                    x0, y0, x1, y1 = x1, y1, x0, y0
                s = '`'+s+"'"
                ed.delete(x0, y0, x1, y1)
                ed.insert(x0, y0, s)
                ed.set_caret(x0+1, y0, x1+1, y1) #sel inside ticks
            return False #block char
