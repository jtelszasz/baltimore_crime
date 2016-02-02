import pandas as pd
import import_funcs

BPD_arrests = import_funcs.import_BPDarrests()

# A little bit of processing/clean-up - this breaks 'ChargeDescription' field in two, divided at '||'
BPD_arrests['ChargeDescr1'] = BPD_arrests.ChargeDescription.apply(lambda x: str(x).split('||')[0])
BPD_arrests['ChargeDescr2'] = BPD_arrests.ChargeDescription.apply(lambda x: str(x).split('||')[1] if len(str(x).split('||'))>1 else '')
BPD_arrests.Neighborhood = BPD_arrests.Neighborhood.str.upper()

a = pd.DataFrame(BPD_arrests.groupby(['Neighborhood', BPD_arrests.index.year]).count().Arrest)
neighborhood_arrests = pd.concat([a.xs(2013,level=1),a.xs(2014,level=1),a.xs(2015,level=1)], axis=1)
neighborhood_arrests.columns = ['arr13','arr14','arr15']

neighborhood_arrests['PcCng1314'] = 100*(neighborhood_arrests['arr14']-neighborhood_arrests['arr13'])/neighborhood_arrests['arr13']
neighborhood_arrests['PcCng1415'] = 100*(neighborhood_arrests['arr15']-neighborhood_arrests['arr14'])/neighborhood_arrests['arr14']

neighborhood_arrests.to_csv('output/neighborhood_arrests.csv', index_label='Neighborhood')