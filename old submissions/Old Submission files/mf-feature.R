# Written in R
# Creating artificial data here.
mHeight = rnorm(n = 2000, mean = 69, sd = 6)
fHeight = rnorm(n = 2000, mean = 63, sd = 6)
mWeight = rnorm(n = 2000, mean = 196, sd = 6)
fWeight = rnorm(n = 2000, mean = 177, sd = 6)

# Run this to see the data
mHeight
fHeight
mWeight
fWeight

# Create Data frame
artif_data = data.frame("Height" = mHeight, "Height2" = fHeight, "Weight" = mWeight, "Weight2" = fWeight)

# Write data as csv
write.csv(artif_data, file = "D:/\User\/Programming Projects/R/r-mf-feature-normal-dist/data.csv")

# Height only sorted
plot(sort(mHeight), main = "Height Only", xlab = "Population", ylab = "Height (Inches)", pch = 20, col = "blue")
points(sort(fHeight), pch = 20, col = "red")

# Height and weight sorted
plot(sort(mWeight), sort(mHeight), main = "Height and Weight", xlab = "Weight (lb)", ylab = "Height (Inches)", pch = 20, col = "blue")
points(sort(fWeight), sort(fHeight), pch = 20, col = "red")

# Height only unsorted
plot((mHeight), main = "Height Only", xlab = "Population", ylab = "Height (Inches)", pch = 20, col = "blue")
points((fHeight), pch = 20, col = "red")
abline(h = 68, col = "green", lwd = 4, lty = 2)
legend(0, 88, legend = c("Male", "Female", "Separation Line Y=68"), col = c("blue", "red", "green"), lty = 1)

# Height and weight unsorted
plot((mWeight), (mHeight), main = "Height and Weight", xlab = "Weight (lb)", ylab = "Height (Inches)", pch = 20, col = "blue")
points((fWeight), (fHeight), pch = 20, col = "red")
abline(8251/17, -38/17, col = "green", lwd = 4, lty = 2)
legend(203, 89, legend = c("Male", "Female", "Separation Line Y=(-38X + 8251)/17"), col = c("blue", "red", "green"), lty = 1)

# Calculations for height only
# Get guess below or above the given inequality
count = 0
index = 1

# For non-sloped line
for (x in mHeight) { # Chamge the variable depending on the gender or use
  if(x < 68) { # Chamge the inequality depending on the gender or use
    count = count + 1
  }
}

# For sloped line
while (index < 2001) {
  if (mHeight[index] >= (-38*mWeight[index] + 8251)/17) {
    count = count + 1
  }
  index = index + 1
}
