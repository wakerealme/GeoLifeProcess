#### 0. Download GeoLife Dataset and rename the director name as GeoLife
```python
https://www.microsoft.com/en-us/download/details.aspx?id=52367
```

#### 1. Transfer from PLT file to CSV file.

```python

python Plt2CSV.py

```

#### 2. Generate All Stay Points

```python

python StayPointsDetection.py

```


#### 3. An example of getting place name by the coordinate of Stay Point using Google Map API

```python

python GoogleMap.py

```

### Reference
[1] Zheng Y . Trajectory Data Mining: An Overview[J]. ACM Transactions on Intelligent Systems and Technology, 2015, 6(3):1-41.

[2] Q. Li, Y. Zheng, X. Xie, Y. Chen, W. Liu, and W.-Y. Ma, "Mining user similarity based on location history", in Proceedings of the 16th ACM SIGSPATIAL international conference on Advances in geographic information systems, New York, NY, USA, 2008, pp. 34:1--34:10. 

https://github.com/shanxuanchen/GeoLifeDataMining/tree/master
