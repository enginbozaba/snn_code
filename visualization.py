# -*- coding: utf-8 -*-
"""
Burada ağımızın çıktısını düzenli bir şekilde görüntülemek bir class için yazıldı.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Visualization:
    
    """
    Bu Sınıf spiking sinir ağının çıktısını görselleştirmek için yazılmıştır.
    """
    
    def __init__(self,data:np.ndarray):
        
        self.data=data
        
        self.noron_number,self.example_number=data.shape #rows,cols
        
        self.df = self.toDataFrame()

    def toDataFrame(self):
        
        func = lambda x : "nöron "+str(x+1)
            
        index_name_arr= np.asarray(list(map(func,range(self.noron_number))))
        
        func = lambda x : "example "+str(x+1)
            
        columns_name_arr=np.asarray(list(map(func,range(self.example_number))))
        
        df=pd.DataFrame(data=self.data,
                        index=index_name_arr,
                        columns=columns_name_arr)
        
        return df
    
    
    def DataFrameShow(self):
        
        print(self.df)

        
    def heatmap(self):
        
        f, ax = plt.subplots(figsize=(9, 6))
        
        sns.heatmap(self.toDataFrame(), annot=True,  linewidths=.5, ax=ax)
    
    
    def noron_spike_barplot(self):
        
        """
        Satırlar ,her bir örnek için nöronların çıktısını gosterir.
        """
        
        fig, axs = plt.subplots(nrows=self.example_number)
        
        fig.suptitle(' spike count plotting of outputs neurals for each a example')
        
        for i in range(self.example_number):
            
            axs[i].bar(range(self.noron_number),self.df.iloc[:,i])
        

#import template as tl
#
#d=tl.Visualization(data=b)
#d.DataFrameShow()
#d.heatmap()
#d.noron_spike_barplot()

#for help
#Example ,help(d.noron_spike_barplot)
