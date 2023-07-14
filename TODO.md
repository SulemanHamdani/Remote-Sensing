### TODO LIST:

- [x] 1. Download Landsat 8 data for Kansas from months January to June (5 days per month)
- [x] 2. Make sure that data has minimal cloud cover in them 
- [x] 3. For each image, use at least 4 bands + NDVI to create a composite image
- [x] 4. For each pixel, calculate the mean value or the median of the composite image. This gives us spatial and temporal information
- [x] 5. Preprocess CDL 2022 data to get the crop type for each pixel. Figure out which crop types to use for training. (Probbably just winter wheat in the beginning)
- [x] 6. Combine it with the CDL 2022 data to get the crop type for each pixel to create a training dataset.
- [x] 7. Gather equivalent LandSAT 7 data to remove missing values
- [x] 8. Gather data from January to July
- [x] 9. Preprocess the data to remove noise
- [x] 10. Concatenate the data
- [ ] 11. Train the data
