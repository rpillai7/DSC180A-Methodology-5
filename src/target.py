import pandas as pd

def score_averages(fp):
    dic_avgs = {}
    df = pd.read_csv(fp)
    dic_avgs['Score_Average'] = df['score'].mean()
    dic_avgs['Score_Aligmment_Average'] = df['score_alignment'].mean()
    dic_avgs['Score_Deep_Average'] = df['score_deep'].mean()
    dic_avgs['Score_Eff_Average'] = df['score_efficiency'].mean()
    return dic_avgs
