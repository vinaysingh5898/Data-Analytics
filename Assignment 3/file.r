#Churn Analysis(written in R-studio)
#Author-Vinay Singh

#setwd("~/Desktop/DA proj-3/")	
#Load Libraries
library(caret)
library(rpart)
library(C50)
library(party)
library(partykit)
library(randomForest)
library(klaR)
library(ROCR)
library(ggplot2)
library(reshape2)
library(car)
library(corrplot)
library(e1071)

#Load Data
f <- file.choose() #choose the database file.
mydata <- read.csv(f)

######################################Part-1###################################################
#Data Munging
mydata$churn <- as.integer(mydata$churn)
mydata$international_plan <- as.integer(mydata$international_plan)
mydata$voice_mail_plan <- as.integer(mydata$voice_mail_plan)

mydata$churn[mydata$churn=="1"] <- 0
mydata$churn[mydata$churn=="2"] <- 1

mydata$international_plan[mydata$international_plan=="1"] <- 0
mydata$international_plan[mydata$international_plan=="2"] <- 1

mydata$voice_mail_plan[mydata$voice_mail_plan=="1"] <- 0
mydata$voice_mail_plan[mydata$voice_mail_plan=="2"] <- 1

#Drop the extra variables
mydata$state <- NULL
mydata$area_code <- NULL
mydata$phone_number <- NULL

#Handling of missing values
na.omit(mydata)

#Run a summary data
summary(mydata)
##############################################Part-2#############################################

#Split database into training and testing (70%-30% ratio)
train.index <- createDataPartition(mydata$churn, p = .7, list = FALSE)
trainData <- mydata[ train.index,]
testData <- mydata[-train.index,]
  
 
#############################################Part-3##############################################
#Model-1(SVM)
SVMmodel <- svm(churn~.,data=trainData,gamma = 0.1,cost = 1)
print(SVMmodel)
summary(SVMmodel)
svm_result <- predict(SVMmodel,testData,type="response")
testData$YHat1 <- predict(SVMmodel,testData,type= "response")
predict1 <- function(t) ifelse(svm_result >t,1,0)
confusionMatrix(predict1(0.5),testData$churn)
#For drawing ROC curve
pred1 <- prediction(testData$YHat1,testData$churn)
perf_svm <- performance(pred1,"tpr","fpr")

#Model-2(C5.0 Improved version of C4.5)

#decision variable class must be converted into a factor variable for C5.0
mydata$churn <- as.factor(mydata$churn)
tree_result <- C5.0(churn~.,data=mydata)
#display summary
summary(tree_result)
C5imp(tree_result,metric = 'usage')
C5imp(tree_result,metric = 'splits')
#now run C5.0 algorithm
rule_result <- C5.0(churn~.,data=mydata,rules=TRUE)
#display summary
summary(rule_result)

rf <- randomForest(churn~.,data = trainData,ntree=500,ntry=500)
c50_result <- predict(rf,testData,type="response")

testData$YHat2 <- predict(rf,testData,type= "response")
predict2 <- function(t) ifelse(c50_result >t,1,0)
confusionMatrix(predict2(0.5),testData$churn)
#For drawing ROC curve
pred2 <- prediction(testData$YHat2,testData$churn)
c50.prff <- performance(pred2,"tpr","fpr")

#Model-3(Naive Baysian Classifier)

trainData$churn <- as.factor((trainData$churn))
testData$churn <- as.factor((testData$churn))
  #build nb model and make predictions 
nb <- NaiveBayes(churn ~ ., data = trainData)
nbprediction = predict(nb, testData, type='raw')

#For Drawing Roc Curve
score = nbprediction$posterior[, 2]
actual.class = testData$churn
pred = prediction(score, actual.class)
nb.prff = performance(pred, "tpr", "fpr")




###################################Part-4#################################
#This part has been mentioned in the respective modelling part



#####################################Part-5################################

#ROC curve

plot.new()
plot(perf_svm,col="green",lwd=2.5)#svm
plot(nb.prff,add=TRUE,col="red",lwd=2.5)#naive bayesian
plot(c50.prff,add=TRUE,col="blue",lwd=2.5)#c5.0
abline(0,1,col="Red",lwd=2.5,lty=2)
