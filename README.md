# Capstone1
Capstone 1 Project for Galvanize Data Science Immersive

## Topics:
- How can qualities of a song be quantified, and how do these quantifications affect the popularity of a song?

## Description:
- I am curious as to how songs can be analyzed to look for trends and formulate a way to predict the success of a song on Spotify.
- After some initial exploration, I really started digging into a song's loudness, tempo, and song length.  These three categories are very objective and not open to interpretation.  After exploring these, the other attributes will be explored.
- I plan to do a comparative analysis on attributes rankings with Mann Whitney U tests.

## Data Source
- This is a dataset which was obtained using Spotify's web API.  This dataset was discovered on [Kaggle](https://www.kaggle.com/tomigelo/spotify-audio-features/home?select=SpotifyAudioFeaturesNov2018.csv "Title").

## Data Description
- Each song is classified by 14 qualities.
    1. Acousticness: A confidence measure from 0.0 to 1.0 of whether the track is acoustic.
    2. Danceability: How suitable a track is for dancing. A value of 0.0 is least danceable and 1.2. is most danceable.
	3. Duration_ms: The duration of the track in milliseconds.
    4. Energy: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity.
	5. Instrumentalness: Predicts whether a track contains no vocals from 0.0 to 1.0
    6. Key: The estimated overall key of the track using standard Pitch Class notation.
	7. Liveness: Detects the presence of an audience in the recording from 0.0 to 1.0.
    8. Loudness: The overall loudness of a track in decibels (dB) between -60 and 0 db.
	9. Mode: Mode indicates the modality (major or minor) of a track. Major is represented by 1 and minor is 0.
	10. Speechiness: Speechiness detects the presence of spoken words in a track from 0 - 1.
	11. Tempo: The overall estimated tempo of a track in beats per minute (BPM).
	12. Time_signature: An estimated overall time signature of a track.
	13. Valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track.
	14. Popularity: A measure of a song's popularity measured from 0-100.

- For this project, I have ommitted instrumentalness, speechiness, time_signature, key, and mode.  A lot of this information is similar through the data set.  For example, the majority of the time_signatures are 4/4.

