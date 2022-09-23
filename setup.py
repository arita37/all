# pylint: disable=C0321,C0103,C0301,E1305,E1121,C0302,C0330,C0111,W0613,W0611,R1705
# -*- coding: utf-8 -*-
"""


"""
import io, os, subprocess, sys
from setuptools import find_packages, setup

######################################################################################
root = os.path.abspath(os.path.dirname(__file__))



##### Version  #######################################################################
version ='0.0.3'
cmdclass= None
print("version", version)



##### Requirements ###################################################################
#with open('install/reqs_image.cmd') as fp:
#    install_requires = fp.read()
install_requires = ['pyyaml', 'stdlib_list', 'python-box', 'fire' ]



###### Description ###################################################################
#with open("README.md", "r") as fh:
#    long_description = fh.read()

def get_current_githash():
   import subprocess 
   # label = subprocess.check_output(["git", "describe", "--always"]).strip();   
   label = subprocess.check_output([ 'git', 'rev-parse', 'HEAD' ]).strip();      
   label = label.decode('utf-8')
   return label

githash = get_current_githash()


#####################################################################################
ss1 = f"""

1000's of utilities functions.


Stats usage:
   > 1 million Donwload !
   https://pepy.tech/project/a2

   https://pypistats.org/packages/a2



Doc Access:
   https://tinyurl.com/2p848smu


   https://groups.google.com/g/a2




Hash:
{githash}


"""
### git hash : https://github.com/arita37/myutil/tree/{githash}

long_description = f""" ``` """ + ss1 +  """```"""



### Packages  ########################################################
packages = ["a2"] + ["a2." + p for p in find_packages("a2")]
#packages = ["a2"] + ["a2.viz" + p for p in find_packages("a2.viz")]
packages = ["a2"] + [ p for p in  find_packages(include=['a2.*']) ]
print(packages)


scripts = [     ]



### CLI Scripts  ###################################################   
entry_points={ 'console_scripts': [

    'docs      = a2.docs.cli:run_cli',

    'templates = a2.templates.cli:run_cli',

    #### generic
    'a2 = a2.cli:run_cli_a2',


    #### generic for All code
    'a22 = a2.cli:run_all_a22',

    ###  sspark
    'sspark = a2.sspark.src.util_spark:run_cli_sspark',


    ###  image
    'image = a2.images.util_image:run_cli',

 ] }




##################################################################   
setup(
    name="a2",
    description="utils",
    keywords='utils',
    
    author="Nono",    
    install_requires=install_requires,
    python_requires='>=3.6.5',
    
    packages=packages,

    include_package_data=True,
    #    package_data= {'': extra_files},

    package_data={
       '': ['*','*/*','*/*/*','*/*/*/*']
    },

   
    ### Versioning
    version=version,
    #cmdclass=cmdclass,


    #### CLI
    scripts = scripts,
  
    ### CLI pyton
    entry_points= entry_points,


    long_description=long_description,
    long_description_content_type="text/markdown",


    classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: ' +
          'Artificial Intelligence',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: ' +
          'Python Modules',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Operating System :: POSIX',
          'Operating System :: MacOS :: MacOS X',
      ]
)



def os_bash_append(cmd):
  """  Append to bashrc
  """
  try :
    fpath = os.path.expanduser("~/.bashrc")
    with open(fpath, "r") as bashrc:
        bashrc = "".join( bashrc.readlines())

    #if cmd in bashrc :
    #    return False   #### Already exist

    with open(fpath, "at") as bashrc:
        bashrc.write("\n"+ cmd +"\n")
    return True
  except Exception as e:
    print(e)  
    return False


#### Add environemment variables  a2 path
try :
    repopath = os.path.dirname( os.path.abspath(__file__).replace("\\", "/") )  + "/a2/"
    if 'win' in sys.platform :
        os.system(f" set  a2='{repopath}/' ")  ### Any new session
        os.system(f" setx a2='{repopath}/' ")  ### Current session

    elif 'linux' in sys.platform :
        os_bash_append(f"""export a2={repopath}/    """)
        os.system(f" export a2={repopath}/ ")
        print(' source  ~/.bashrc  ')

    print(" $a2  can be used as shortcut of the package library path for Command Line Usage")    

except :
    pass



def os_cmd_to_bashrc(cmd):
    try :
        if 'win' in sys.platform :
            os.system(f""" set  {cmd} """)  ### Any new session
            os.system(f""" setx {cmd} """)  ### Current session

        elif 'linux' in sys.platform :
            os_bash_append(f"""{cmd}""")
            print(' source  ~/.bashrc  ')

    except :
        pass


#### Spark Alias for command line
# cmd= "alias sspark='python $a2/sspark/src/util_spark.py '"
# os_cmd_to_bashrc(cmd)








































"""
alias sspark='python /workspace/myutil/a2/sspark/src/util_spark.py'


from setuptools import setup, find_packages


setup(
    name='xpdtools',
    version='0.2.0',
    packages=find_packages(),
    description='data processing module',
    zip_safe=False,
    package_data={'xpdan': ['config/*']},
    include_package_data=True,
    entry_points={'console_scripts': 'iq = xpdtools.raw_to_iq:main_cli'}
)


def main_cli(): fire.Fire(main)
    
    
"""





"""
:: Sets environment variables for both the current `cmd` window 
::   and/or other applications going forward.
:: I call this file keyz.cmd to be able to just type `keyz` at the prompt 
::   after changes because the word `keys` is already taken in Windows.

@echo off

:: set for the current window
set APCA_API_KEY_ID=key_id
set APCA_API_SECRET_KEY=secret_key
set APCA_API_BASE_URL=https://paper-api.alpaca.markets

:: setx also for other windows and processes going forward
setx APCA_API_KEY_ID     %APCA_API_KEY_ID%
setx APCA_API_SECRET_KEY %APCA_API_SECRET_KEY%
setx APCA_API_BASE_URL   %APCA_API_BASE_URL%

"""





