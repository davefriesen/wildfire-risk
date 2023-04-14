# Project to Predict Wildfire Risk
__Dave Friesen, John Chen, and Kyle Dalope__<br>
__dfriesen@sandiego.edu, johnchen@sandiego.edu, kdalope@sandiego.edu__<br>
__GitHub: https://github.com/davefriesen/wildfire-risk__<br>

#### -- Programming Languages: Python with cloud-based service AWS

## Overview
EnviroTech DJK has been engaged to analyze and inform wildfire management throughout the Western United States including California, Oregon, and Washington. This engagement aims to understand underlying wildfire factors and identify high-risk scenarios to predict, prevent, and manage wildfire impact on communities and natural ecosystems.

## Problem Statement
According to the National Oceanic and Atmospheric Administration (NOAA), the risk and extent of wildfires in the Western United States have increased over the last two decades. This increase can be linked in part to climate variability and factors like temperature, humidity, and lack of moisture in foliage, in addition to other terrestrial characteristics and management practices (NOAA, 2023).

The growing wildfire challenge in the Western United States presents a need and opportunity: to apply technology and expertise to understand, predict (identify high-risk scenarios), and monitor the occurrence and scope of wildfires in order to prevent and mitigate their ecological and economic impact.

## Goals
* Identify key factors and relationships that lead to wildfires, for example through a risk-ranking system. 
* Identify high-risk wildfire scenarios using these critical factors and location-based data. For example, generate binary fire/no-fire predictions based on the      
  probability of wildfire outcome from proximate factors like forest conditions, weather, and terrain.
* Create the basis for a reliable and resilient (cloud-based) alerting and monitoring system for wildfires.
* Ultimately inform the reduction and mitigation of wildfire risk throughout the Western U.S.

## Non-Goals
* Identifying the exact behavior for a wildfire (a next-step opportunity);
* Providing statutory or regulatory input to government officials;
* Considering controlled burns, e.g., coordinated with indigenous tribes;
* Providing information regarding fire suppression (best left to firefighters); or,
* Predicting or informing the environmental impact of wildfires.

## Getting Started
1. Clone the repo
   ```sh
   git clone https://github.com/davefriesen/wildfire-risk.git
   ```
2. Data is stored in the [data] folder within this repo (https://github.com/davefriesen/wildfire-risk/tree/main/data)
3. Code and steps for this project are stored in the [src] folder within this repo (https://github.com/davefriesen/wildfire-risk/tree/main/src)

## Data Sources
* Forest census data from the United States Forest Service’s (USFS) Forest Inventory and Analysis (FIA) Program (https://experience.arcgis.com/experience/3641cea45d614ab88791aef54f3a1849)
* Historical weather data from the National Oceanic and Atmospheric Administration (NOAA); ideally from NOAA’s Joint Polar Satellite System via AWS (https://registry.opendata.aws/noaa-jpss/) or, alternatively, from NOAA’s historical weather information (https://www.ncdc.noaa.gov/cdo-web/datasets)
* Historical wildfire data from the National Interagency Fire Center (NIFC) for select locations at a point in time (https://data-nifc.opendata.arcgis.com/maps/wildland-fire-incident-locations/)

## References
* National Oceanic and Atmospheric Administration (NOAA). (2023). Wildfire climate connection. https://www.noaa.gov/noaa-wildfire/wildfire-climate-connection
* National Interagency Fire Center. (n.d.). Wildland fire incident locations. Retrieved March 12, 2023, from https://data-nifc.opendata.arcgis.com/maps/wildland-fire-incident-locations/ 
* Service, U. S. F. (2019, March 20). USFS Forest Inventory and Analysis (FIA) program. Kaggle. Retrieved March 12, 2023, from https://www.kaggle.com/datasets/usforestservice/usfs-fia 
* FIA DataMart 2.0 : Home. (n.d.). Apps.fs.usda.gov. Retrieved March 24, 2023, from https://apps.fs.usda.gov/fia/datamart/recent_load_history.html
* FIA Database Description and User Guide for Phase 2 (version: 9.0.1) The Forest Inventory and Analysis Database: Database Description and User Guide for Phase 2 (version 9.0.1) Contents Preface User Guide Updates Changes from the Previous Database Version. (n.d.). Retrieved March 24, 2023, from https://www.fia.fs.usda.gov/library/database-documentation/current/ver90/FIADB%20User%20Guide%20P2_9-0-1_final.pdf
* Das, P., Ivkin, N., Bansal, T., Rouesnel, L., Gautier, P., Karnin, Z., Dirac, L., Ramakrishnan, L., Perunicic, A., Shcherbatyi, I., Wu, W., Zolic, A., Shen, H., Ahmed, A., Winkelmolen, F., Miladinovic, M., Archembeau, C., Tang, A., Dutt, B., & Grao, P. (2020). Amazon SageMaker Autopilot. Proceedings of the Fourth International Workshop on Data Management for End-To-End Machine Learning. https://doi.org/10.1145/3399579.3399870
