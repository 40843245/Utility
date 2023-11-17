"""
Objectives:
    1. Perform operations about Spyder in Anaconda Navigator.
    
Apprecation:
    Very thankful to a Github account, named Patrick Toche (nickname: ptoche) asked the issue on GitHub (shown in the Ref section)
    and provides the code. I modified it from it.

Used Module:
    Builtin:
        1. os
        2. sys
        3. inspect
        4. subprocess
        5. pathlib
        
    Open Source:
        1. ast
        2. spyder
        3. restarter
        4. IPython
NOTICE:
    NOTICE that:
        1. Before use the code, one has to install these modules mentioned in Open Source section.
        For more details, google it or see my notes named ModulesLink.txt on GitHub.
        
Ref:
    https://github.com/spyder-ide/spyder/issues/12910

See also:
    1. GitHub account named Patrick Toche:
        https://github.com/ptoche
"""

import os
import sys
import ast
from inspect import getsourcefile
from spyder.app.cli_options import get_options
import subprocess
import restarter
from pathlib import Path  # to create a directory if needed
from spyder.utils import encoding  # not needed, but more general
from spyder.py3compat import to_text_string  # not needed, but more general
from IPython import get_ipython  # to load a new instance of a file in the editor

"""
A class that perform operation about Spyder in Anaconda Navigator.
"""
class SpyderHandler():
    """
    A class that handles files in Editor.
    """
    class Editor():
        """
        Intro:
            Create a temp file for a named environment inside a subdirectory. 
            If the file already exists, load it (The author like to keep/edit the temp files across sessions).
        Parameter:
            1. envname: environment name. Defaults to None.
            2. filename: file name. Defaults to None.
        Returned Value:
            None
        """
        @staticmethod
        def MakeTempFile(envname=None, filename=None):

            if not filename:
                filename = os.path.join(os.path.expanduser('~'), '.spyder-py3/temp.py')
            # if no environment is supplied, use temp.py in root directory,
            root = os.path.dirname(filename)
            # otherwise create a temp.py inside an <envname> directory
            if not envname:
                envname =''
                envdir = root
                editor_location = "It resides in the <root> environment."
            else: 
                # if directory <envname> does not exist, create it:
                envdir = os.path.join(root, 'envs', envname)
                Path(envdir).mkdir(parents=True, exist_ok=True)
                editor_location = "It resides in the <"+envname+"> environment."
            tempfile = os.path.join(envdir, os.path.basename(filename))
            # if temp.py file does not exist, create it
            if not os.path.isfile(tempfile):
                # Creating temporary file
                default = ['# -*- coding: utf-8 -*-',
                            '"""', '' "Spyder Editor", '',
                            "This is a temporary script file", '',
                            editor_location, '',
                            '"""', '', '']
                text = os.linesep.join([encoding.to_unicode(qstr)
                                        for qstr in default])
                encoding.write(to_text_string(text), tempfile, 'utf-8')
            # now load the new temp file
            ipython = get_ipython()
            ipython.magic(f"%edit {tempfile}")
            return None
    """
    A class that handles about configuration.
    """
    class Config():
        """
        Intro:
            Reset Spyder configuration file while an instance of spyder is running.
        Parameter:
            None
        Returned Value:
            None
        """
        @staticmethod        
        def ResetConfig():        
            # store the environment
            env = os.environ.copy()
        
            # get the variables
            options, args = get_options()
            spyder_args = str(sys.argv[1:])  # can't find any spyder arguments  :-(
        
            if not spyder_args:
                error = "This script can only be called from within a Spyder instance"
                raise RuntimeError(error)
        
            # Parse variables stored as string literals in the environment.
            args = ast.literal_eval(spyder_args)
        
            # Enforce the --new-instance flag
            args.append('--new-instance')
        
            # Arrange arguments to be passed to the restarter subprocess
            args = ' '.join(args)
        
            # Get python excutable running this script
            python = sys.executable
        
            # Get the spyder base directory:
            this_folder = os.path.split(os.path.dirname(os.path.abspath(getsourcefile(lambda:0))))[0]
            spyder_folder = os.path.split(this_folder)[0]
            spyderdir = os.path.join(spyder_folder, 'spyder')
            spyder = os.path.join(spyderdir, 'app', 'start.py')
        
            # Build the command:
            cmd = '"{0}" "{1}" {2}'.format(python, spyder, args)
        
            # Restart -- Open a pipe to command cmd:
            try:
                print("cmd:"+cmd)
                subprocess.Popen(cmd, shell=True, env=env)
            except Exception as error:
                restarter.launch_error_message(error_type=restarter.RESTART_ERROR, error=error)
        


if __name__ == '__main__':
    SpyderHandler.Editor.MakeTempFile()
