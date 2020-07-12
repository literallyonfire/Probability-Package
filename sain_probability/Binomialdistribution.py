import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of trials
    
    
    TODO: Fill out all TODOs in the functions below
            
    """
    
    def __init__(self, prob=.5, size=20):

        self.p = prob
        self.n = size
        Distribution.__init__(self)
    
    def calculate_mean(self):
    
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
                
        self.mean = self.p * self.n
        return self.mean



    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """

        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev
        
        
        
        
    def replace_stats_with_data(self):
    
        """Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """
        #data is expected to come in as an array of 0s and 1s.
        # ex data: [0,0,1,1,0,1,0,1] refering to tails if 0 and heads if 1

        #Keeps probability success to 0 at first
        p = 0
        for data in self.data:
            if data:
                p += 1

        #Calculates n and p for the class
        self.n = len(self.data)
        self.p = p/self.n

        #then calculates stdev and mean
        self.stdev = self.calculate_stdev()
        self.mean = self.calculate_mean()
        
        return self.p,self.n
        
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """

        #creates an array every time some data is close to 1 or 0
        one = [1 for x in self.data if x >= 0.5]
        zero = [0 for x in self.data if x < 0.5]


        x = [0,1]
        y = [len(zero), len(one)] #gets the count of zeros and ones in the data

        #Plots the bar chart
        plt.bar(x,y, color='red')
        plt.xlabel('Heads or Tails')
        plt.ylabel('Count')
        plt.title('Bar chart of Data')

        #changes the x-axis to be tails and heads
        plt.xsticks(x, ['tails','heads'])
             
        plt.show() #show the plot
        
    def pdf(self, k):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """

        #Uses the binomial probability function formula to calculate probability
        probability =  (math.factorial(self.n)/(math.factorial(k) * math.factorial(self.n -k))) * self.p**k * (1 - self.p)**(self.n - k)
        
        return probability

    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """

        #X-Values are just numbers from 0 to n
        #Y-Values are the probabilities from pdf function given some n number as input for k
        x = []
        y = []
        for num in range(self.n):
             x.append(num)
             y.append(pdf(num))

        #Plot the bar graph
        plt.bar(x,y, color='red')
        plt.xlabel('K Values from 0 to n')
        plt.ylabel('Probability of Success')
        plt.title('Bar Graph of Probility success of k from 0 to n')
        
        plt.show()
        return x,y
        
         
                
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        result_binomial = Binomial()
        result_binomial.n = self.n + other.n
        result_binomial.p = self.p
        
        return result_binomial
        
        
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
    
        return 'mean {}, standard deviation {}, p {}, n {}'.format(self.mean, self.stdev, self.p, self.n)
