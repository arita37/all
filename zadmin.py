
import os


from utilmy.util_download import download_github




ll = {
      0 : {
         'url'   : ('https://github.com/TylerYep/torchinfo.git'  , 'main')
        ,'copy'  :  [ ('fromfolder', '/utilmy' ) ]
        ,'rename':  [ ('ptorch', 'totch2') ]
      }


     ,1 : {
         'url'   : 'https://github.com/TylerYep/torchinfo.git'
        ,'copy'  :  [ ('fromfolder', '/utilmy' ) ]
        ,'rename':  [ ('ptorch', 'totch2') ]
      }





}


def download_overwrite():
    """
      1) Donwload repo in zip, unzip it



      2) Copy Overwrite   folderXXX   to utilmy/my



      3) Rename some names inside the .py and folder


    """
    dir0 = ''
    for _, dd in ll.items():

        url    = dd['url'][0]
        branch = dd['url'][1]
        repo   = url,split"/")['-1'].replace(".git", ::)

        git_clone(url,branch, dir0)

        for fromdir, todir in dd['copy'].items():

            fromdir = dir0 + repo + fromdir
            todir   = todir

            os.copy(fromdir, todir)

            for fromtxt, totxt in dd['rename'].items():
                os.replace_in_file(todir,  fromtxt, totxt)

    







