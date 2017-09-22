setwd("C:/Users/willi/Desktop/code/bball/yearly record as csv")
fileNames=list.files("C:/Users/willi/Desktop/code/bball/yearly record as csv")
file_names <- dir("C:/Users/willi/Desktop/code/bball/yearly record as csv") #where you have your file
alldat<- lapply(file_names,read.csv)
dat <- paste("data", 1976:2017, sep="")
variance=c(1:len(fileNames))
n <- 1
parity = c(0:0)

for(i in 1:length(file_names)){
  assign(dat[i], read.csv(file_names[i]))
}

for (fileName in fileNames) {
  
  # read data:
  sample <- read.csv(fileName,
                     header = TRUE,
                     sep = ",")
  pct=sample$win_loss_pct
  var <- var(pct)
  print(var(pct))
  parity[n]<-var
  n<-n+1
}
year <- c(1976:2017)
df <- data.frame(year,parity)


write.csv(df, file = "parity.csv")
