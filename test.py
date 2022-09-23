
# -*- coding: utf-8 -*-
""" tests
Docs::

        python test.py   test_all
        python test.py   test_viz_vizhtml
        Rules to follow :
           Put import only inside the function.
           def  test_{pythonfilename.py}() :
               from a2 import parallel as m
               m.test_all()
"""
import os, sys, time, datetime,inspect, random, pandas as pd, random, numpy as np, glob


#### NEVER IMPORT HERE  !!!!
# from a2 import pd_random, pd_generate_data
# from tensorflow.python.ops.gen_array_ops import one_hot

#########################################################################################
def log(*s):
   print(*s, flush=True)

def import_module(mname:str='a2.oos'):
    import importlib
    m = importlib.import_module(mname)
    return m

   
def pd_random(ncols=7, nrows=100):
   import pandas as pd
   ll = [[ random.random() for i in range(0, ncols)] for j in range(0, nrows) ]
   df = pd.DataFrame(ll, columns = [str(i) for i in range(0,ncols)])
   return df


def pd_generate_data(ncols=7, nrows=100):
    """ Generate sample data for function testing
    categorical features for anova test
    """
    import numpy as np, pandas as pd
    np.random.seed(444)
    numerical    = [[ random.random() for i in range(0, ncols)] for j in range(0, nrows) ]
    df = pd.DataFrame(numerical, columns = [str(i) for i in range(0,ncols)])
    df['cat1']= np.random.choice(  a=[0, 1],  size=nrows,  p=[0.7, 0.3]  )
    df['cat2']= np.random.choice(  a=[4, 5, 6],  size=nrows,  p=[0.5, 0.3, 0.2]  )
    df['cat1']= np.where( df['cat1'] == 0,'low',np.where(df['cat1'] == 1, 'High','V.High'))
    return df   
   
   




#########################################################################################
def test_import():
    os.chdir(  os.getcwd() + "/../../")
    import utilmy.sspark.src.util_spark
    import utilmy.sspark.src.util_hadoop
    import utilmy.deeplearning.ttorch.util_torch
    import utilmy.deeplearning.ttorch.util_model
    import utilmy.deeplearning.ttorch.model_ensemble
    import utilmy.a2
    import utilmy.ppandas
    # import utilmy.nlp.ttorch.sentences
    import utilmy.distributed
    import utilmy.ppandas
    log('All imported OK')


def test_import_all():
    os.chdir(  os.getcwd() + "/../../")
    import utilmy.sspark.src.util_spark
    import utilmy.sspark.src.util_hadoop
    import utilmy.deeplearning.ttorch.util_torch
    import utilmy.deeplearning.ttorch.util_model
    import utilmy.deeplearning.ttorch.model_ensemble
    import utilmy.a2
    import utilmy.ppandas
    # import utilmy.nlp.ttorch.sentences
    import utilmy.distributed
    import utilmy.ppandas
    log('All imported OK')



def test_a2():
   from a2 import utilmy as m
   m.test_all()
   
   
   #####  Bug of globals() in a2.py #################################################
   log("\n##### Session  ")
   sess = m.Session("ztmp/session")

   global mydf
   mydf = pd_generate_data()

   sess.save('mysess', glob=globals(), tag='01')
   os.system("ls ztmp/session")
   sess.show()
   import glob
   flist = glob.glob("ztmp/session/" + "/*")
   for f in flist:
       t = os.path.exists(os.path.abspath(f))
       assert  t == True, "session path not created "

       pickle_created = os.path.exists(os.path.abspath(f + "/mydf.pkl"))
       assert  pickle_created == True, "Pickle file not created"

   sess.load('mysess')
   sess.load('mysess', tag='01')



##########################################################################################
def test_images():
    from a2.images import util_image as m
    m.test_all()


##########################################################################################
def test_ppandas():
    from a2 import ppandas as m
    m.test_all()

   
#########################################################################################
def test_docs_cli():
    """  from a2.docs.generate_doc import run_markdown, run_table 
    """
    cmd = "doc-gen  --repo_dir a2/      --doc_dir docs/"
    os.system(cmd)
    os.system('ls docs/')
   
   
#########################################################################################
def test_adatasets():
    """ #### python test.py   test_adatasets """
    from a2 import adatasets as m ;   m.test_all()      


#########################################################################################
def test_nnumpy():
    """#### python test.py   test_nnumpy  """
    from a2 import nnumpy as m ; m.test_all()



#########################################################################################
def test_dates():
    #### python test.py   test_dates
    from a2 import dates as m  ; m.test_all()


#########################################################################################
def test_decorators():
    #### python test.py   test_decorators
    from a2 import  decorators as m  ;m.test_all()


   
#########################################################################################
def test_nlp():
    from a2.nlp import util_cluster as m ; m.test_all()  
    from a2.nlp import util_gensim as m ;  m.test_all()  
    # from a2.nlp.torch import sentences   as m ;  m.test_all()      

   
#########################################################################################
def test_viz_vizhtml():
   from a2.viz import vizhtml as m
   log("Visualization ")
   log(" from a2.viz import vizhtml as vi     ")
   m.test_all()





#########################################################################################
def test_parallel():
   from a2 import parallel as m  ;  m.test_all()
   

#########################################################################################
def test_distributed():
   from a2 import distributed as m ;m.test_all()

   
  
#######################################################################################
def test_utils():
    from a2 import utils as m ;  m.test_all() 
         

#######################################################################################
def test_oos():
   from a2 import oos as m ;  m.test_all() 


#######################################################################################
def test_tabular():
   from a2.tabular import util_sparse as m    ;     m.test_all()
   from a2.tabular import util_explain as m  ;      m.test_all()
   from a2.tabular import util_uncertainty as m  ;  m.test_all()

   
#########################################################################################
def test_deeplearning_keras():
    from a2.deeplearning.kkeras import  util_similarity as m;  m.test_all()



#########################################################################################
def test_deeplearning_torch():
    from a2.deeplearning.ttorch import  rule_encoder as m ;  m.test_all()
    # from a2.deeplearning.ttorch import  sentences as m ;  m.test_all()


#######################################################################################
def test_deeplearning():
   from a2.deeplearning import util_yolo as m ;  m.test_all()


#######################################################################################
def test_recsys():
   from a2.recsys import ab as m ; m.test_all()
   from a2.recsys import metric as m ; m.test_all()

  

#######################################################################################
def test_compile():
   from a2.docs import format as m




#######################################################################################
def test_long():
    from a2.nlp.ttorch import sentences   as m ;  m.test_all()      



def test_spark():
    from a2.sspark.src import util_spark  as m ;  m.test_all()      




import utilmy as  uu


#######################################################################################
def test_all():
    test_a2()
    test_decorators()
    test_ppandas()  
    test_nlp()
    test_docs_cli()


    ################
    # test_oos()
    test_tabular()
    test_adatasets()
    test_dates()
    test_utils()


    ################
    test_deeplearning_keras()
    test_deeplearning()


    ###############
    test_recsys()


      
#######################################################################################
if __name__ == "__main__":
    import fire
    fire.Fire() 

   