from .redis_keys import REDIS_KEYS

# NOTE: New keyspaces in the source code require configuration here.
keyspaces = {
    REDIS_KEYS.ACCOUNT: 0,
    REDIS_KEYS.SAVED_KEY_IMPORT_IDS: 0,
    REDIS_KEYS.SAVED_KEYS: 0,
    REDIS_KEYS.TOP_ARTISTS: 0,
    REDIS_KEYS.ARTIST_FAVED: 0,
    REDIS_KEYS.ARTISTS_FAVED_COUNT: 0,
    REDIS_KEYS.TOP_ARTISTS_RECENTLY: 0,
    REDIS_KEYS.ARTISTS_RECENTLY_FAVED_COUNT: 0,
    REDIS_KEYS.RANDOM_ARTIST_KEYS: 0,
    REDIS_KEYS.NON_DISCORD_ARTIST_KEYS: 0,
    REDIS_KEYS.NON_DISCORD_ARTISTS: 0,
    REDIS_KEYS.ARTISTS_BY_SERVICE: 0,
    REDIS_KEYS.ARTIST: 0,
    REDIS_KEYS.ARTIST_POST_COUNT: 0,
    REDIS_KEYS.ARTIST_LAST_UPDATED: 0,
    REDIS_KEYS.ARTISTS_BY_UPDATE_TIME: 0,
    REDIS_KEYS.UNAPPROVED_DMS: 0,
    REDIS_KEYS.DMS: 0,
    REDIS_KEYS.ALL_DMS: 0,
    REDIS_KEYS.ALL_DMS_COUNT: 0,
    REDIS_KEYS.ALL_DMS_BY_QUERY: 0,
    REDIS_KEYS.ALL_DMS_BY_QUERY_COUNT: 0,
    REDIS_KEYS.DMS_COUNT: 0,
    REDIS_KEYS.FAVORITE_ARTISTS: 0,
    REDIS_KEYS.FAVORITE_POSTS: 0,
    REDIS_KEYS.ARTIST_FAVORITED: 0,
    REDIS_KEYS.POST_FAVORITED: 0,
    REDIS_KEYS.POSTS_BY_FAVORITED_ARTISTS: 0,
    REDIS_KEYS.NOTIFICATIONS_FOR_ACCOUNT: 0,
    REDIS_KEYS.RANDOM_POST_KEYS: 0,
    REDIS_KEYS.ALL_POST_KEYS: 0,
    REDIS_KEYS.POST: 0,
    REDIS_KEYS.COMMENTS: 0,
    REDIS_KEYS.POSTS_BY_ARTIST: 0,
    REDIS_KEYS.ARTIST_POSTS_OFFSET: 0,
    REDIS_KEYS.IS_POST_FLAGGED: 0,
    REDIS_KEYS.NEXT_POST: 0,
    REDIS_KEYS.PREVIOUS_POST: 0,
    REDIS_KEYS.IMPORTER_LOGS: 0,
    REDIS_KEYS.RATELIMIT: 0,
    REDIS_KEYS.ALL_POSTS: 0,
    REDIS_KEYS.ALL_POSTS_FOR_QUERY: 0,
    REDIS_KEYS.GLOBAL_POST_COUNT: 0,
    REDIS_KEYS.GLOBAL_POST_COUNT_FOR_QUERY: 0,
    REDIS_KEYS.LOCK: 0,
    REDIS_KEYS.LOCK_SIGNAL: 0,
    REDIS_KEYS.IMPORTS: 0,
    REDIS_KEYS.RUNNING_IMPORTS: 0,
}
