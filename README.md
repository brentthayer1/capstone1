# Capstone1
Capstone 1 Project for Galvanize Data Science Immersive

## Topics:
- How can qualities of a song be quantified, and could this process be applied to song writing techniques to achieve the status of a 'Hit' song?

## Description:
- I am curious as to how songs can be vectorized and analyzed to look for trends and formulate a way to predict the success of a song on Spotify.


## Data Source
- This is a dataset which was obtained using Spotify's web API.  This dataset was discovered on Kaggle, and can be found on [GitHub](https://github.com/fortytwo102/the-spotify-hit-predictor-dataset "Title")


## Data Description
- This data is organized by decade, from 1960 - 2019.  This data has no information on plays, streams, or units sold.
- Each data point is classified as either a 'Hit' or a 'Flop'.  A song is classified as a 'Flop' if:
    - The song does not appear in the 'hit' list of that decade.
    - The track's artist does not appear in the 'hit' list of that decade.
    - The track belongs to a genre that could be considered non-mainstream and / or avant-garde.
    - The track's genre does not have a song in the 'hit' list.
    - The track does not have 'US' as one of its markets.

- Each song is classified by 17 qualities.
    1. Danceability: How suitable a track is for dancing. A value of 0.0 is least danceable and 1.2. is most danceable.
	3. Energy: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity.
	4. Key: The estimated overall key of the track using standard Pitch Class notation.
	5. Loudness: The overall loudness of a track in decibels (dB) between -60 and 0 db.
	6. Mode: Mode indicates the modality (major or minor) of a track. Major is represented by 1 and minor is 0.
	7. Speechiness: Speechiness detects the presence of spoken words in a track from 0 - 1.
	8. Acousticness: A confidence measure from 0.0 to 1.0 of whether the track is acoustic.
	9. Instrumentalness: Predicts whether a track contains no vocals from 0.0 to 1.0
	10. Liveness: Detects the presence of an audience in the recording from 0.0 to 1.0.
	11. Valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track.
	12. Tempo: The overall estimated tempo of a track in beats per minute (BPM).
	13. Duration_ms: The duration of the track in milliseconds.
	14. Time_signature: An estimated overall time signature of a track.
	15. Chorus_hit: This the the author's best estimate of when the chorus would start for the track.
	16. Sections: The number of sections the particular track has.
	17. Target: The target variable for the track.

