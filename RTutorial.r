data("AirPassengers")
class(AirPassengers)

start(AirPassengers)
end(AirPassengers)

frequency(AirPassengers)

summary(AirPassengers)

plot(AirPassengers)

abline(reg = lm(AirPassengers~time(AirPassengers)))

cycle(AirPassengers)

#this will aggregate the cycles and display a year on year trend
plot(aggregate(AirPassengers,FUN = mean))

boxplot(AirPassengers~cycle(AirPassengers))

## ARMA models are commonly used in time series modeling.
## In ARMA model, AR stands for auto-regression and MA stands for moving average

## The primary difference between an AR and MA model is based on the correlation between time series objects at different time points. The correlation between x(t) and x(t-n) for n > order of MA is always zero. This directly flows from the fact that covariance between x(t) and x(t-n) is zero for MA models (something which we refer from the example taken in the previous section). However, the correlation of x(t) and x(t-n) gradually declines with n becoming larger in the AR model. This difference gets exploited irrespective of having the AR model or MA model. The correlation plot can give us the order of MA model.

## Once we have got the stationary time series, we must answer two primary questions:
### Is it an AR or MA process?
### What order of AR or MA process do we need to use?

# Auto - correlation function / ACF
## ACF is a plot of total correlation between different lag functions


## We need to address two issues before we test stationary series.
## One, we need to remove unequal variances.

adf.test(diff(log(AirPassengers)),alternative = 'stationary',k=0)

acf(log(AirPassengers))

acf(diff(log(AirPassengers)))

pacf(diff(log(AirPassengers)))
