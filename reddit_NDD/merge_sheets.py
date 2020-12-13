import pandas as pd

df1 = pd.read_excel(r"Reddit_posts_18000.xlsx")
df2 = pd.read_excel(r"subreddits.xlsx")
#df3 = pd.read_excel("subreddits_parentingautism.xlsx")

frames = [df1,df2]

result  = pd.concat(frames)
print(result.shape)
result.drop_duplicates(inplace=True)
result.to_excel("reddit_posts_"+str(result.shape[0])+".xlsx")
print(result.shape)