import os                                                                       
from multiprocessing import Pool                                                
                                                                                
                                                                                
processes = ('source1.py', 'source2.py', 'source3.py')                                    
                                                  
                                                                                
def run_process(process):                                                             
    os.system('python {}'.format(process))                                       
                                                                                
                                                                                
pool = Pool(processes=3)                                                        
pool.map(run_process, processes)
