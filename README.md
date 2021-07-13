# mlb_1
fun stats project


Question 1:

* Linear Dependence Between X and y's:

There is an issue when interpreting the y's.  

ya is normal-ish and OK for a linear model.

yb is left-skewed.  I apply a log transformation to reduce left-skew.

yc has a 'spike' in the middle, is symmetric, and tiny values.

Using R, I computed the summary statistics between X and y:

## ya


'''

lm(formula = ya ~ x1 + x2 + x3 + x5 + x6, data = ds1)

Residuals:
    Min      1Q  Median      3Q     Max 
-45.849  -7.057  -0.054   7.040  56.901 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept) 7.569655   0.089358  84.712   <2e-16 ***
x1          2.517667   0.020211 124.571   <2e-16 ***
x2          6.234627   0.016566 376.359   <2e-16 ***
x3          0.951090   0.033131  28.707   <2e-16 ***
x5          0.002319   0.033079   0.070    0.944    
x6          0.004127   0.007107   0.581    0.561    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 10.48 on 99994 degrees of freedom
Multiple R-squared:  0.6769,	Adjusted R-squared:  0.6769 
F-statistic: 4.19e+04 on 5 and 99994 DF,  p-value: < 2.2e-16

'''

## yb

* yb is left-skewed, and so I apply a logarithmic transformation to help reduce its left-skew.

Call:
lm(formula = log(yb) ~ x1 + x2 + x3 + x5 + x6, data = ds1)

Residuals:
    Min      1Q  Median      3Q     Max 
-7.5713 -0.1066  0.0445  0.1675  0.5799 

Coefficients:
              Estimate Std. Error t value Pr(>|t|)    
(Intercept) -1.106e-01  2.520e-03 -43.886   <2e-16 ***
x1           1.522e-01  5.693e-04 267.331   <2e-16 ***
x2          -1.343e-05  4.663e-04  -0.029   0.9770    
x3          -1.762e-03  9.326e-04  -1.889   0.0589 .  
x5           2.085e-04  9.310e-04   0.224   0.8228    
x6           3.244e-05  1.999e-04   0.162   0.8710    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.2947 on 99780 degrees of freedom
  (214 observations deleted due to missingness)
Multiple R-squared:  0.6843,	Adjusted R-squared:  0.6843 
F-statistic: 4.325e+04 on 5 and 99780 DF,  p-value: < 2.2e-16

* Compared to untransformed yb, not a huge difference in terms of linear significance:


Call:
lm(formula = (yb) ~ x1 + x2 + x3 + x5 + x6, data = ds1)

Residuals:
    Min      1Q  Median      3Q     Max 
-1.3846 -0.1563  0.0113  0.1703  0.9700 

Coefficients:
              Estimate Std. Error t value Pr(>|t|)    
(Intercept)  8.427e-01  2.127e-03 396.244   <2e-16 ***
x1           2.542e-01  4.810e-04 528.388   <2e-16 ***
x2           6.148e-05  3.943e-04   0.156   0.8761    
x3          -1.797e-03  7.885e-04  -2.279   0.0227 *  
x5           2.778e-04  7.872e-04   0.353   0.7242    
x6           7.677e-05  1.691e-04   0.454   0.6499    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.2494 on 99994 degrees of freedom
Multiple R-squared:  0.8949,	Adjusted R-squared:  0.8949 
F-statistic: 1.702e+05 on 5 and 99994 DF,  p-value: < 2.2e-16

## yc

* A LM scales the uniform variable down to a tiny scale to roughly approximate the 'spike'.

Call:
lm(formula = yc ~ x1 + x2 + x3 + x5 + x6, data = ds1)

Residuals:
     Min       1Q   Median       3Q      Max 
-0.54386 -0.00254 -0.00010  0.00239  0.81826 

Coefficients:
              Estimate Std. Error t value Pr(>|t|)  
(Intercept) -1.136e-04  2.661e-04  -0.427   0.6694  
x1           1.208e-04  6.019e-05   2.008   0.0447 *
x2           7.659e-06  4.933e-05   0.155   0.8766  
x3          -1.820e-04  9.866e-05  -1.844   0.0652 .
x5           8.846e-05  9.851e-05   0.898   0.3692  
x6          -9.798e-07  2.116e-05  -0.046   0.9631  
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 0.03121 on 99994 degrees of freedom
Multiple R-squared:  4.996e-05,	Adjusted R-squared:  -3.673e-08 
F-statistic: 0.9993 on 5 and 99994 DF,  p-value: 0.4163

