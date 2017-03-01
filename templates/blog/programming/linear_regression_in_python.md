<div id='title'>
    Real GDP ~ Median Household Income with Linear Regression
    <br>
    <pre><code> Andrew Berger Oct. 15, 2016 </code></pre>
</div>

<div id='text'>

    In this tutorial we are going to use simple linear regression to correlate and forecast U.S. Median Household Income based on Real (inflation-adjusted) GDP. Intuitively, one may assume that a higher economic well-being for a country would lead to a higher median income for its citizens. We might make the hypothesis that there is a correlation between a country producing more goods and services and it's citizens living on a higher income.

    <br> <br>

    <code> Gross Domestic Product </code>, or GDP - the monetary value of final goods and services in a country - is one of the most well-known measurements of economic well-being.
    When we're done, we will be able to determine the effect of GDP on median income in the U. S. We are going to test this hypothesis for the U. S. with data since 1985 from the St. Louis Federal Reserve.
    <br> <br>
    
    To access these data, we are going to use an API hosted by Quandl.
    In the previous tutorial we introducted Quandl, an open-source, web-based 
    database provider. Hopefully at this point you have your own API token and 
    have registered your free account.
    <hr>

    <strong> Required: </strong>
    <br>
</div>

    :::
    import quandl
    from scipy import stats
    from bokeh.plotting import figure, show

<hr>
<div id='text'>
    The below function will allow us to pass the independent and dependent variables for our linear regression as first and second arguments and plot the regression line. Lucky for us, Python's scipy module provides everything we need to abstract the actual linear regression computations. The function <code> stats.linregress </code> is the magic here, giving us our parameters from the regression: the slope, intercept, Pearson's r value, p value, and even standard error. To fit our line to the data, we just need the slope and intercept values. We can map the simple linear formula <code> y = mx + b </code> to our y values with Python's list comprehension! All we need to know is how to interpret the final results.
</div>
<hr>

    :::python
    def plot_linear_regression(x, y):
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        fit = [slope*_x + intercept for _x in x]
        
        p = figure(title='Real GDP vs. Median Household Income')
        p.scatter(x, y, legend='r^2: %s' % r_value**2)
        p.line(x, fit, color='red', legend='y = %sx + %s' % (slope, intercept))
        
        show(p)

<div id='text'>
    Essentially, in two lines we have our linear regression. The rest of the above code is for the plotting from matplotlib. We're going to forward fill missing data, so if anything is missing, just use the previous value. 
    Quandl likes the format <code> 'DATABASE/TABLE' </code> for the quandl.get function.
    Make sure to drop any rows that are nan (not a number) to avoid errors in regression.
</div>
<hr>
    

    :::python
    if __name__ == '__main__':
        dat = quandl.get(['FRED/GDPC1', 'FRED/MEHOINUSA672N'], collapse='quarterly')
        dat = dat.fillna(method='ffill').dropna()

        x, y = dat['FRED/GDPC1 - VALUE'], dat['FRED/MEHOINUSA672N - VALUE']
        plot_linear_regression(x, y)
    
<hr>
<div id='text'>
    Let's visualize both of our datasets.
<hr>

<div class='crop'>
    <img src='/static//images/real_gdp.png'>
</div>
<hr>

Real GDP has a nice, positive slope most of the time - a little kink during the 2008 recession, but otherwise looks healthy.
Just from eyeballing, it looks like the last thirty years we have increased our GDP about 10,000 billion dollars!.

<hr>

<div class='crop'>
    <img src='/static//images/med_hh_income.png'>
</div>
<hr>

Median Household Income (MHI) does not look as consistent as GDP, although we are better off now (~$57,000) than we were thirty years ago (~$46,000).
<hr>

We also want to look at the returns for each of these datasets. Returns are just a percent change, and <code> pandas.DataFrame.pct_change </code> allows us to do exactly that.
<hr>

    :::python
    def plot_returns(xs, ys):
        xs_returns = xs[1:].pct_change()
        ys_returns = ys[1:].pct_change()
    
        p, k = figure(), figure()
        p.line(xs_returns.index, xs_returns, color='blue')
        k.line(ys_returns.index, ys_returns, color='blue')
    
        fig = Column(*[p, k])
        show(fig)

<hr>
GDP Returns (0.6% average)
<div class='crop'>
    <img src='/static/images/gdp_returns.png'>
</div>

Median Household Income Returns (0.1% average)
<div class='crop'>
    <img src='/static/images/mhi_returns.png'>
</div>
<hr>

We have our linear fit for the dataset, a line that minimizes the sum of squared residuals (differences from the mean).
We also have our r squared correlation coefficient, which is a number between -1 and 1 that signifies 
the proportion of the variance in the dependent variable (MHI) that is predictable from the independent variable (GDP).
In other words,  r squared is a statistical measure of how well the regression line approximates the real data points.
<hr>

<div class='crop'>
    <img src='/static//images/gdp_to_med_hh_income.png'>
</div>
<hr>

We see how the trendline appears to 'fit' the scatterplot of data points.
The slope of the line can be interpreted as how much the dependant variable (MHI)
changes for each additional unit of change to the independent variable (GDP).

</div>
<hr>

<div id='title'>
    Conclusion
    <hr>
</div>

<div id='text'>
    Our correlation between inflation-adjusted GDP and Median Household Income in the U.S. since 1985
    came out to <strong>0.46</strong>. From a first glance, this number may not seem very strong, 
    so we may assume that there is a weak relationship between these variables, but further statistical
    testing is required to understand if this correlation is actually significant.
    <br> <br>
    In practice, meaningful correlations (i.e., correlations that are clinically or practically important) 
    can be as small as 0.4 (or -0.4) for positive (or negative) associations. So we shouldn't rule out a 0.46
    just because it's not a 0.8 or 0.9.
    <br> <br>
    For follow-up, we can conduct a p-test to determine if our correlation between GDP and MHI is significant.
    Conveniently, the scipy function <code> linregress </code> gives us everything we need, including slope,
    y-intercept, r-value, p-value, and the standard error.
    <br> <br>

<div id='title'>
P-Value
<hr>
</div>

<div id='text'>

In statistics, a p-value is a metric of probability used to determine the significance of a result.
More specifically, a significant p-value - usually below 0.05, sometimes less than 0.01 - allows the statistician to reject the counter, or null, hypothesis.
A rejection of the null hypothesis implies that the probability of the statistical summary being the same or more extreme than actual results
is very low.
<br> <br>

<div class='crop'>
    <img src=/static/images/p_value.svg
</div>
<br> <br>

In our study of Gross Domestic Product and Median Household Income, our p-value was  very low - 2.88e-19. For our intents and purposes,
this p-value is considered significant and we will reject the null hypothesis that our statistical results are insignificant.
<br> <br>

<div id='title'>
Discussion
<hr>
</div>

Going back to our relationship between GDP and MHI, we can now say with confidence that according to our p-value,
our statistical summary is significant.
However, our r-squared of 0.46 indicates that the model explains about half of the variability of the response data around its mean.
In other words, we should probably adjust or use a different model to increase our r-squared in order to explain more of the variability with these data.

<br> <br>


</div>

View the full source code below:


<br>
</div>

    :::
    import quandl
    from scipy import stats
    from bokeh.plotting import figure, show

    def plot_linear_regression(x, y):
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        fit = [slope*_x + intercept for _x in x]

        p = figure(title='Real GDP vs. Median Household Income')
        p.scatter(x, y, legend='r^2: %s' % r_value**2)
        p.line(x, fit, color='red', legend='y = %sx + %s' % (slope, intercept))

        show(p)
        
    if __name__ == '__main__':
        dat = quandl.get(['FRED/GDPC1', 'FRED/MEHOINUSA672N'], collapse='quarterly')
        dat = dat.fillna(method='ffill').dropna()

        x, y = dat['FRED/GDPC1 - VALUE'], dat['FRED/MEHOINUSA672N - VALUE']
        plot_linear_regression(x, y)


</div>
