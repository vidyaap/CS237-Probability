
#QUESTION 10, first version of significance

# significance <- function(n, sig, mu, x){
#   z = (x-mu)/(sig/(sqrt(n)))
#   p = 1- pnorm(z)
#   paste("z = ", z, "  p = ", p)
# }


#Question 11, second version of significance

# significance <- function(n, sig, mu, x){
#   z = (x-mu)/(sig/(sqrt(n)))
#   p = 1- pnorm(z)
#   significant = ifelse(p<=0.05, "yes", "no")
#   paste("n = ", n, "   z= ", z, "  p = ", p, "  significant = ", significant)
# }

#Question 15, final version of significance

significance <- function(n, sig, mu, x, alt){
  z = (x-mu)/(sig/(sqrt(n)))
  if (alt == "two.sided"){
    p = (1 - pnorm(z))*2
  }
  else{
    p = 1- pnorm(z) 
  }
  paste("x = ", x, "  n = ", n, "  z = ", z, "  p = ", p)
}


#Problem 19
x <- seq(10, 30, length.out = 100)
y <- dnorm(x, mean = 20.38028169, sd = 4.7)
plot(x, y, type = 'l', col = '#00ABFF', lwd = 3, axes = TRUE, xlab = 'mpg', ylab = '', main = 'MPG Distribution')
axis(side = 1, at = seq(10,30, by = 1))
abline(v=21.297841929)
abline(v=19.462721451)


#Problem 25
x <- seq(-4, 4, length.out = 100)
y <- dnorm(x, mean = 0, sd = 1)
plot(x, y, type = 'l', col = '#00ABFF', lwd = 3, axes = TRUE, xlab = '', ylab = '', main = 'T-Dist with Different DFs')
axis(side = 1, at = seq(-4, 4, by = 1))

t1 <- dt(x,df=1)
t3 <- dt(x,df=3)
t8 <- dt(x,df=8)
t30 <- dt(x,df=30)


lines(x,t1,type="l",col="blue",yaxt='n',ann=FALSE, lwd = 3)
par(new=TRUE)
lines(x,t3,type="l",col="green",yaxt='n',ann=FALSE, lwd = 3)
par(new=TRUE)
lines(x,t8,type="l",col="orange",yaxt='n',ann=FALSE, lwd = 3)
par(new=TRUE)
lines(x,t30,type="l",col="red",yaxt='n',ann=FALSE, lwd = 3)
