![main](/images/waveform2.jpg)

# What Makes A Song Popular

## Topics

- How can attributes of a recorded song be analyzed, and how do these different attributes affect the popularity of a song on a streaming service like Spotify?

## Description

- I am curious what trends lay within different aspects of a song.
- I plan to do a comparative analysis on attribute's rankings using the Spearman Correlation testing method.
- After looking through the data initially, there are a few key attributes that I really want to explore.  I am most interested in seeing the correlation between popularity and loudness.

## Data Source

- This is a dataset which was obtained using Spotify's web API.  This dataset was discovered on [Kaggle](https://www.kaggle.com/tomigelo/spotify-audio-features/home?select=SpotifyAudioFeaturesNov2018.csv "Title").

## Data Description

- Each song is classified by 14 qualities: Acousticness, Danceability, Duration, Energy, Instrumentalness, Key, Liveness, Loudness, Mode, Speechiness, Tempo, Time_signature, Valence and Popularity.

- For this project, I have ommitted Instrumentalness, Speechiness, Time Signature, Key, and Mode.  These attributes were relatively distributed evenly across the dataset, leaving for little to analyze in terms of a correlation between themselves and popularity.

- In the initial dataset there were 130,663 songs.  22,106 of these scored a 0 and 1 for popularity.  I thought this was very interesting, and could not wrap my mind around how 17% of songs would be this low.  I found it hard to believe that even the worst of the worst songs would still be considered a 0 or a 1.  I decided after careful consideration to omit these.  My thoughts are that they could have possibly been NaNs initially at some point.  This omition slimmed the dataset down to 106,040 songs.

![attribute_dists](/images/attribute_dists.png)

## Exploration

- I plotted the remaining song's attributes against popularity to try to get a visual to see where any correlations might be.  To better visualize the correlation, I decided to break the dataset into smaller datasets based on popularity rating.  The main set I was looking for was the most popular songs, the best of the best.  After exploring the popularity, I settled on selecting the top 0.13% of the songs as the most popular.  What was very interesting was that this small percentage covered popularity ratings from 86 to 100, 138 songs in all.  This set was given the name df_86.

- With the remaining data, I wanted to distribute it fairly evenly into similar sized groups.  My group selections were based on the following popularity ratings:

| Subset   | Songs  | Percent of Data | Popularity   |
| :------: | :----: | :-------------: | :----------: |
| df_86    | 138    |        0.13%    | > 86         |
| df_52    | 13,680 |       12.9%     | > 52, <= 86  |
| df_41    | 13,267 |       12.51%    | > 41, <= 52  |
| df_33    | 12,794 |       12.07%    | > 33, <= 41  |
| df_26    | 14,363 |       13.54%    | > 26, <= 33  |
| df_20    | 13,562 |       12.79%    | > 20, <= 26  |
| df_14    | 14,268 |       13.46%    | > 14, <= 20  |
| df_7     | 14,447 |       13.62%    | > 7, <= 14   |
| df_1     |  9,521 |       8.98%     | > 1, <= 7    |

- I plotted the distributions of each subset together for each song attribute against popularity.  This gave a very nice clear view of some possible correlations.  The distributions that visually stood out to me the most were loudness, energy, and danceability.  I think the plots of these distributions clearly show that there is some sort of correlation with popularity.

## popularity: A measure from 0 to 100 that represents a song's popularity on Spotify

### time_seconds: The duration of the track in seconds.
![time_seconds](/images/time_seconds.png)

### acousticness: A confidence measure from 0.0 to 1.0 of whether the track is acoustic.
![acousticness](/images/acousticness.png)

### danceability: How suitable a track is for dancing. A value of 0.0 is least danceable and 1.2. is most danceable.
![danceability](/images/danceability.png)

### energy: A measure from 0.0 to 1.0 that represents a perceptual measure of intensity and activity.
![energy](/images/energy.png)

### liveness: Detects the presence of an audience in the recording from 0.0 to 1.0.
![liveness](/images/liveness.png)

### loudness: The overall loudness of a track in decibels (dB) between -60 and 0 db.
![loudness](/images/loudness.png)

### tempo: The overall estimated tempo of a track in beats per minute (BPM).
![tempo](/images/tempo.png)

### valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track.
![valence](/images/valence.png)



- To look into these correlations further, I decided to use the Spearman Correlation testing method to assess how well the relationship between two attributes can be described.  I found the following correlations with popularity:

| Attribute    | Correlation | P-Value    |
| :----------: | :---------: | :--------: |
| loudness     | 0.263       | 0.000e+00  |
| danceability | 0.183       | 0.000e+00  |
| energy       | 0.123       | 0.000e+00  |
| valence      | 0.056       | 2.658e-73  |
| tempo        | 0.038       | 2.186e-35  |
| time_seconds | -0.009      | 5.598e-03  |
| liveness     | -0.024      | 4.102e-15  |
| acousticness | -0.099      | 1.229e-228 |

![attribute_heat_map](/images/attribute_heat_map.png)

## Conclusion

Even though the correlation between popularity and every attribute is statistically significant, I wondered about the practical significance. The correlation between loudness and popularity stands out the most. I am also interested in the time aspect of a song. I know that people have a short attention span, and was assuming I would see more of a correlation between popularity increasing as a song's length was shorter.

## Further Exploration

I hope to further investigate the relationships between loudness, danceability, energy and tempo.  These four attributes seem like they all work together in some way.

I also hope to pull in some data on possibly location of where common listeners are located.  I think it would be interesting to see how different parts of the country prefer their music.

## References


