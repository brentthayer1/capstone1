# Capstone1

Capstone 1 Project for Galvanize Data Science Immersive

## Topics

- How can attributes of a recorded song be analyzed, and how do these different attribute affect the popularity of a song on a streaming service like Spotify?

## Description

- I am curious as to how songs can be analyzed to look for trends and formulate a way to predict the success of a song on Spotify.
- I plan to do a comparative analysis on attribute's rankings using the Spearman Correlation testing method.
- As an audio engineer, there are a few key attributes that I really want to explore, the main one being loudness.

## Data Source

- This is a dataset which was obtained using Spotify's web API.  This dataset was discovered on [Kaggle](https://www.kaggle.com/tomigelo/spotify-audio-features/home?select=SpotifyAudioFeaturesNov2018.csv "Title").

## Data Description

- Each song is classified by 14 qualities.
    - Acousticness: A confidence measure from 0.0 to 1.0 of whether the track is acoustic.
    - Danceability: How suitable a track is for dancing. A value of 0.0 is least danceable and 1.2. is most danceable.
	- Duration_ms: The duration of the track in milliseconds.
    - Energy: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity.
	- Instrumentalness: Predicts whether a track contains no vocals from 0.0 to 1.0
    - Key: The estimated overall key of the track using standard Pitch Class notation.
	- Liveness: Detects the presence of an audience in the recording from 0.0 to 1.0.
    - Loudness: The overall loudness of a track in decibels (dB) between -60 and 0 db.
	- Mode: Mode indicates the modality (major or minor) of a track. Major is represented by 1 and minor is 0.
	- Speechiness: Speechiness detects the presence of spoken words in a track from 0 - 1.
	- Tempo: The overall estimated tempo of a track in beats per minute (BPM).
	- Time_signature: An estimated overall time signature of a track.
	- Valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track.
	- Popularity: A measure of a song's popularity measured from 0-100.

- For this project, I have ommitted Instrumentalness, Speechiness, Time Signature, Key, and Mode.  These attributes were relatively distributed evenly across the dataset, leaving for little to analyze in terms of a correlation between themselves and popularity.

- In the initial dataset there were 130,663 songs.  22,106 of these scored a 0 and 1 for popularity.  I thought this was very interesting, and could not wrap my mind around how 17% of songs would be this low.  I found it hard to believe that even the worst of the worst songs would still be considered a 0 or a 1.  I decided after careful consideration to omit these.  My thoughts are that they could have possibly been NaNs initially at some point.  This omition slimmed the dataset down to 106,040 songs.

## Exploration

- I plotted the remaining song's attributes against popularity to try to get a visual to see where any correlations might be.  To better visualize the correlation, I decided to break the dataset into smaller datasets based on popularity rating.  The main set I was looking for was the most popular songs, the best of the best.  After exploring the popularity, I settled on selecting the top 0.13% of the songs as the most popular.  What was very interesting was that this small percentage covered popularity ratings from 86 to 100, 138 songs in all.  This set was given the name df_86.

- With the remaining data, I wanted to distribute it fairly evenly into similar sized groups.  My group selections were based on the following popularity ratings:
    -   df_52:  13,680 songs
        12.24% percent of the dataset.   52 < Popularity >= 86
    -   df_41:  13,267 songs
        11.87% percent of the dataset.   41 < Popularity >= 52
    -   df_33:  12,794 songs
        11.45% percent of the dataset.   33 < Popularity >= 41
    -   df_26:  14,363 songs
        12.85% percent of the dataset.    26 < Popularity >= 33
    -   df_20:  13,562 songs
        12.13% percent of the dataset.     20 < Popularity >= 26
    -   df_14:  14,268 songs
        12.77% percent of the dataset.    14 < Popularity >= 20
    -   df_7:   14,447 songs
        12.93% percent of the dataset.   7 < Popularity >= 14
    -   df_1:    9,521 songs
        8.52% percent of the dataset.   1 < Popularity >= 7

- I plotted the distributions of each subset together for each song attribute against popularity.  This gave a very nice clear view of some possible correlations.  The distributions that visually stood out to me the most were loudness, energy, and danceability.  I think the plots of these distributions clearly show that there is some sort of correlation with popularity.


![time_seconds_cdf](/images/time_seconds_cdf.png) ![time_seconds_cdf](/images/time_seconds_pdf.png)


- To look into this further, I decided to use the Spearman Correlation testing method to assesses how well the relationship between two attributes can be described.  I found the following correlations with popularity:

    - Loudness-
        - Correlation of 0.263, with a p-value of 0.0.
        - As a song gets louder than its popularity will go up.
    - Danceability-
        - Correlation of 0.183, with a p-value of 0.0.
        - As a song's danceability value increases than its popularity will go up.
    - Energy-
        - Correlation of 0.123, with a p-value of 0.0.
        - As a song's energy increases than its popularity will go up.
    - Valence-
        - Correlation of 0.056, with a p-value of 2.658326249179174e-73.
        - As a song's valence increases than its popularity will go up.
    - Tempo-
        - Correlation of 0.038, with a p-value of 2.185627825374629e-35.
        - As a song's tempo increases than its popularity will go up.
    - Time-
        - Correlation of -0.009, with a p-value of 0.0055977699952641236.
        - As a song's length increases than its popularity will go down.
    - Liveness-
        - Correlation of -0.024, with a p-value of 4.101749967807702e-15.
        - As a song's sense of liveness increases than its popularity will go down.
    - Acousticness-
        - Correlation of -0.099, with a p-value of 1.2290236449990221e-228.
        - As a song's acousticness value increases than its popularity will go down.

## Conclusion

Even though the correlation between popularity and every attribute is statistically significant, one has to wonder about the practical significance. The correlation between loudness and popularity is the most interesting to me. I am also interested in the time aspect of a song. I know that people have a short attention span, and was assuming I would see more of a correlation between popularity increasing as a song's length was shorter.
