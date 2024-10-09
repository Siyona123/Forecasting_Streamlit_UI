library(tidyverse)
df=read.csv('titanic.csv')
View(df)
df1=drop_na(df)
View(df1)
ggplot(df1,aes(x=Fare,fill='sex'))+
