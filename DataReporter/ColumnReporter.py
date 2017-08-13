import matplotlib.pyplot as plt
import pandas as pd
class ColumnReporter():
    """process one column of data"""
    def __init__(self,data_column,config):
        self.data_column=data_column
        self.config=config

    def report(self):
        """
        
        :return:  report data Structure:
         { 
            name: "",
            uniq_values:[]
            data_dype: [numeric| categoricial]
            plot object
            statistic info
         
         }
        """
        _data=self.data_column
        self.report_dict=  {
            "name": _data.name,
            "unique_values": self.unique(),
            "data_dype": self.conclude_data_type(),
            "plot_object": self.plot(),
            "statistic_info":self.statistics()
         }

        return self.report_dict

    def statistics(self):
        statistic_dict= {}
        _data = self.data_column[self.data_column.notnull()]

        if str(self.data_column.dtype)!='object':
            try: statistic_dict["median "]=_data.median()
            except: pass
            try: statistic_dict["mean"]=_data.mean()
            except: pass
            try: statistic_dict["max"]=_data.max()
            except: pass
            try: statistic_dict["min"]=_data.min()
            except: pass
        try: statistic_dict["mode "] = ";".join(list(_data.mode()))
        except: pass


        return statistic_dict

    def plot(self):
        plt.style.use('ggplot')
        plot_dict={
            "object" :[{"kind":"bar"}],
            "bool"   :[{"kind":"bar"}],
            "float64": [{"kind": "box"}, {"kind": "line"}, {"kind": "hist"}],
            "int64"  :[{"kind":"box"},{"kind":"hist"}],
            "float32":[{"kind":"box"},{"kind":"line"}],
            "int32"  :[{"kind":"box"},{"kind":"hist"}],
        }
        _data= self.data_column
        fig_path = self.config.fig_path("{}.png".format(self.data_column.name))
        fig = plt.figure()
        # ax = fig.gca()
        ax=[]
        plot_lst=plot_dict[str(_data.dtype)]
        for i,plitm in enumerate(plot_lst):
            ax.append(fig.add_subplot(len(plot_lst), 1, i+1))

            _kind=plitm['kind']
            if str(_data.dtype) in ['object','int64','bool'] and len(_data.unique())<50:
                _df=_data.apply(pd.value_counts)
                x_val=list(_df)
                y_val=_df.sum()
                ax[i].set_title("{}-{}-{}".format(_data.name,_kind,'count'))
                y_val.plot(kind='bar',title=self.data_column.name+ ' count',ax=ax[i])
            elif str(_data.dtype) not in ['object','bool']:
                _data.plot(kind=_kind,ax=ax[i])
            else:
                return None

        print("fig_path={}".format(fig_path))
        fig.savefig(fig_path)
        plt.cla()
        plt.clf()
        return fig_path

    def unique(self):
        _data = self.data_column
        uniq_vals = _data.unique()
        uv = sorted(list(map(str, uniq_vals)))
        if len(uv) > 20:
            uv=map(str,uv[0:9] + ["..."] + uv[-9:-1])
        return ", ".join(uv)

    def conclude_data_type(self):
        return self.data_column.dtype

