library(lmtest)
library(tseries)
library(ggplot2)

select.lags<-function(x,y,max.lag=8) {
  y<-as.numeric(y)
  y.lag<-embed(y,max.lag+1)[,-1,drop=FALSE]
  x.lag<-embed(x,max.lag+1)[,-1,drop=FALSE]
  
  t<-tail(seq_along(y),nrow(y.lag))
  
  ms=lapply(1:max.lag,function(i) lm(y[t]~y.lag[,1:i]+x.lag[,1:i]))
  
  pvals<-mapply(function(i) anova(ms[[i]],ms[[i-1]])[2,"Pr(>F)"],max.lag:2)
  ind<-which(pvals<0.05)[1]
  ftest<-ifelse(is.na(ind),1,max.lag-ind+1)
  
  aic<-as.numeric(lapply(ms,AIC))
  bic<-as.numeric(lapply(ms,BIC))
  structure(list(ic=cbind(aic=aic,bic=bic),pvals=pvals,
                 selection=list(aic=which.min(aic),bic=which.min(bic),ftest=ftest)))
}

setwd("C:/Users/willi/Desktop/code/bball")
paritydat <- read.csv("C:/Users/willi/Desktop/Does NBA Parity Predict Final Ratings/bball/parity/parity.csv")
ratingdat <- read.csv("C:/Users/willi/Desktop/Does NBA Parity Predict Final Ratings/bball/ratings/ratings.csv")
parity <- paritydat$parity
rating_descending <- ratingdat$Avg
n <- 42
rating <- c(1:42)

for( i in 1:42){
  rating[i] <- rating_descending[n]
  n <- n-1
}
parity_years = paritydat$year

plot(rating)
ggplot(data=paritydat, aes(x=year, y=parity, group=1)) +
  geom_line()
ggplot(data=ratingdat, aes(x=Years, y=Avg, group=1))+ geom_line()

adf.test(rating)#p-value = .5465 => accept null hypothesis => existence of unit root and non stationary
adf.test(parity)#p-value = 0.08 =>accept null hypotheses => existence of unit root and non stationary

ratingdiff <- diff(rating, differences = 1)
paritydiff <- diff(parity, difference = 1)


plot(paritydiff)
plot(ratingdiff)

adf.test(paritydiff)#p-value = .018 => reject null tests=>reject existence of unit root and non-stationarity=>stationary
adf.test(ratingdiff)#p-value = .0183 =>reject null tests=>reject existence of unit root and non-stationarity=>stationary

s <- select.lags(ratingdiff, paritydiff, 8)
t(s$selection)
#determine optimal lags. lag = 1

#p-value = .3912 > than significance interval => accept h0 => no granger causality
#if p-value is smaller than significance interval => reject h0
#does parity granger cause rating
grangertest( ratingdiff ~ paritydiff,order=1) 

#does ratingdiff granger cause parity?
#p-value = .1909 > greater than significan interval => no granger causality
grangertest( paritydiff ~ ratingdiff,order=1) 

cor(rating, parity)# correlation of .38, weak positive linear correlation


