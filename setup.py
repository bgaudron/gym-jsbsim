from setuptools import setup, find_packages
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import platform
import subprocess
import sys, os
import re

dep = """
C++ dependencies for this project are:

If you see compilation error FIRST THING TO CHECK if pkg-config call was successful.
Install dependencies that pkg-config cannot find.
"""

from setuptools.command.install import install as DistutilsInstall
from setuptools.command.egg_info import egg_info as EggInfo

setup_py_dir = os.path.dirname(os.path.realpath(__file__))

class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

class Build(build_ext):
    def run(self):
        try:
            out = subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError("CMake must be installed to build the following extensions: " +
                               ", ".join(e.name for e in self.extensions))

        if platform.system() == "Windows":
            cmake_version = LooseVersion(re.search(r'version\s*([\d.]+)', out.decode()).group(1))
            if cmake_version < '3.1.0':
                raise RuntimeError("CMake >= 3.1.0 is required on Windows")

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_args = ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + extdir,
                      '-DPYTHON_EXECUTABLE=' + sys.executable,
                      '-DBUILD_SHARED_LIBS=ON',
                      '-DCYTHON_EXECUTABLE=' + os.path.join(os.path.abspath(os.path.dirname(sys.executable)) + os.sep + 'cython'),
                      '-DBUILD_PYTHON_MODULE=ON']

        cfg = 'Debug' if self.debug else 'Release'
        build_args = ['--config', cfg]

        if platform.system() == "Windows":
            cmake_args += ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{}={}'.format(cfg.upper(), extdir)]
            if sys.maxsize > 2**32:
                cmake_args += ['-A', 'x64']
            build_args += ['--', '/m']
        else:
            cmake_args += ['-DCMAKE_BUILD_TYPE=' + cfg]
            build_args += ['--', '-j4']

        env = os.environ.copy()
        env['CXXFLAGS'] = '{} -DVERSION_INFO=\\"{}\\"'.format(env.get('CXXFLAGS', ''),
                                                              self.distribution.get_version())
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, cwd=self.build_temp, env=env)
        subprocess.check_call(['cmake', '--build', '.'] + build_args, cwd=self.build_temp)

need_files = ['.so']
hh = setup_py_dir + "/jsbsim"
need_files_ext = 'png jpg urdf obj mtl dae off stl STL xml glsl dylib'.split()
need_files_re = [re.compile(r'.+\.'+p) for p in need_files_ext]
need_files_re.append(re.compile(r'.+\.so(.\d+)*'))
need_files_re.append(re.compile(r'.+/\.libs/.+'))
need_files_re.append(re.compile(r'.+/\.qt_plugins/.+'))

for root, dirs, files in os.walk(hh):
    for fn in files:
        fn = root + '/' + fn
        if any([p.match(fn) for p in need_files_re]):
            need_files.append(fn[1+len(hh):])

print("found resource files: %i" % len(need_files))
for n in need_files: print("-- %s" % n)

setup(
    name = 'gym-jsbsim',
    version = '1.0.0',
    description = 'Gym JSBSim environment',
    maintainer = 'John Doe',
    maintainer_email = 'john.doe@gmail.com',
    url = 'https://github.com/galleon/gym-jsbsim',
    packages=[x for x in find_packages()],
    ext_modules=[CMakeExtension(name='jsbsim', sourcedir='jsbsim')],
    cmdclass={'build_ext': Build},
    install_requires=['gym'],
    package_data = { '': need_files }
)
