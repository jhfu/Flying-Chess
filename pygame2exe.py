#!python
# -*- coding: utf-8 -*-

try:
    from distutils.core import setup
    import py2exe, pygame
    from modulefinder import Module
    import glob, fnmatch
    import sys, os, shutil
except ImportError, message:
    raise SystemExit,  "Sorry, you must install py2exe, pygame. %s" % message
 
origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
    if os.path.basename(pathname).lower() in (
            "sdl_ttf.dll", "libfreetype-6.dll", "libogg-0.dll"):
            return 0
    return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL
 
class pygame2exe(py2exe.build_exe.py2exe):
    def copy_extensions(self, extensions):
        py2exe.build_exe.py2exe.copy_extensions(self, extensions)
 
class BuildExe:
    def __init__(self):
        self.script = "Chess.py"
        self.project_name = "Flying Chess"
        self.project_url = "http://??"
        self.project_version = "0.1"
        self.license = "NO License"
        self.author_name = "fffff"
        self.author_email = "fffff@qq.com"
        self.copyright = "Copyright (c) 2012 fffff"
        self.project_description = "Just for fun"
        self.icon_file = None
        self.extra_datas = ['data']
        self.extra_modules = None
        self.exclude_modules = [
                "pywin", "pywin.debugger", "pywin.debugger.dbgcon",
                "pywin.dialogs", "pywin.dialogs.list", 
                "Tkconstants","Tkinter","tcl",
                "numpy", "OpenGL", "_ssl", "ssl"
                ]
        self.exclude_dll = []
        self.extra_scripts = []
        self.zipfile_name = "game.res"
        self.dist_dir ='dist'
 
    def opj(self, *args):
        path = os.path.join(*args)
        return os.path.normpath(path)
 
    def find_data_files(self, srcdir, *wildcards, **kw):
        def walk_helper(arg, dirname, files):
            if '.svn' in dirname:
                return
            names = []
            lst, wildcards = arg
            for wc in wildcards:
                wc_name = self.opj(dirname, wc)
                for f in files:
                    filename = self.opj(dirname, f)
 
                    if fnmatch.fnmatch(filename, wc_name) and not os.path.isdir(filename):
                        names.append(filename)
            if names:
                lst.append( (dirname, names ) )
 
        file_list = []
        recursive = kw.get('recursive', True)
        if recursive:
            os.path.walk(srcdir, walk_helper, (file_list, wildcards))
        else:
            walk_helper((file_list, wildcards),
                        srcdir,
                        [os.path.basename(f) for f in glob.glob(self.opj(srcdir, '*'))])
        return file_list
 
    def run(self):
        if os.path.isdir(self.dist_dir):
            shutil.rmtree(self.dist_dir)
        
        if self.icon_file == None:
            path = os.path.split(pygame.__file__)[0]
            self.icon_file = os.path.join(path, 'pygame.ico')
 
        extra_datas = []
        for data in self.extra_datas:
            if os.path.isdir(data):
                extra_datas.extend(self.find_data_files(data, '*'))
            else:
                extra_datas.append(('.', [data]))
        
        setup(
            cmdclass = {'py2exe': pygame2exe},
            version = self.project_version,
            description = self.project_description,
            name = self.project_name,
            url = self.project_url,
            author = self.author_name,
            author_email = self.author_email,
            license = self.license,
 
            windows = [{
                'script': self.script,
                'icon_resources': [(0, self.icon_file)],
                'copyright': self.copyright
            }],
            options = {'py2exe': {'optimize': 2,
                                  'bundle_files': 1,
                                  'compressed': True,
                                  'excludes': self.exclude_modules,
                                  'packages': self.extra_modules,
                                  'dist_dir': self.dist_dir,
                                  'dll_excludes': self.exclude_dll,
                                  'includes': self.extra_scripts} },
            zipfile = self.zipfile_name,
            data_files = extra_datas,
            )
        
        if os.path.isdir('build'):
            shutil.rmtree('build')
 
if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.argv.append('py2exe')
    BuildExe().run()
    raw_input("Finished! Press any key to exit.")

