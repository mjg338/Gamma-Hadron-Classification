# Gamma | Hadron Classification

This project details a method of improving Gamma research efficiency through the use of a Random Forest Classifier. 

The experimentation itself requires a Cherenkov telescope, a device which uses a highly sophisticated imaging technique to detect atmospheric Gamma rays and consequent Hadron showers, or "Cherenkov Light."

The images produced provide several dimensions for analysis and discernment between the two phenomena. From a set of about 19k instances with 10 features each, already preclassified as either Gammas or Hadrons, I detail my process to create a model that could be used to improve research efficiencies in otherwise naive settings. 

To do this I employed several classification models from sklearn, finding the random forest classifier to outperform all other models in this case by a wide margin. I then looked over relevant research papers to find means of creating additional features from the intial 10. I find and implement 3 such derivations, improving the metric scores of my model accross the board. 

In the end I achieved a true positive rate for Gammas of 94%, and a true positive rate for Hadrons of 81%. I consider this a fairly successful model, as the Gammas accounted for 65% of my data, and the Hadrons 35%. The 10-fold cross validation score was also just under 89%.

Despite considerable efforts in hyperparameter optimization, the only measure that seemed to improve model performance beyond the default setting was for tree count. This was suggested in one study, and observed here, to optimize at 50 trees. 

To improve this model further, I would look through the research to see what else could be found on attribution creation.
