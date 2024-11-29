# -*- coding: utf-8 -*-
"""bayesian_prediction_for_PH.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19flp2N91HoP5zSeNiA1kzZUi-HdnCkng
"""

install.packages(c("bnlearn", "bnclassify", "dplyr", "ggplot2"))

install.packages("rmarkdown")

library(bnlearn)

grades <- read.table("/content/2020_bn_nb_data.txt",head=TRUE)

head(grades)

grades <- lapply(grades,as.factor)

grades <- data.frame(grades)

grades.bayseianNet <- hc(grades[,-9],score = 'k2')

plot(grades.bayseianNet)

grades.fit <- bn.fit(grades.bayseianNet,grades[,-9])

grades.fit$EC100
grades.fit$EC160
grades.fit$IT101
grades.fit$IT161
grades.fit$MA101
grades.fit$PH100
grades.fit$PH160
grades.fit$HS101

bn.fit.barchart(grades.fit$EC100)
bn.fit.barchart(grades.fit$EC160)
bn.fit.barchart(grades.fit$IT101)
bn.fit.barchart(grades.fit$IT161)
bn.fit.barchart(grades.fit$MA101)
bn.fit.barchart(grades.fit$PH100)
bn.fit.barchart(grades.fit$PH160)
bn.fit.barchart(grades.fit$HS101)

grades.PH100 <- data.frame(cpdist(grades.fit,nodes = c("PH100"), evidence = ((EC100 == "DD") & (IT101 == "CC") & (IT101 == "CC") & (MA101 == "CD"))))

library(dplyr)
library(ggplot2)

# Assuming grades.PH100 is your dataframe
df <- grades.PH100 %>%
  group_by(PH100) %>%
  summarise(counts = n())

ggplot(df, aes(x = PH100, y = counts)) +
  geom_bar(fill = "#0073C2FF", stat = "identity") +
  geom_text(aes(label = counts), vjust = -0.3)
