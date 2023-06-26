conn = new Mongo();
db = conn.getDB("ugc");

db.createCollection("likes");
db.createCollection("bookmarks");

db.likes.createIndex({ movie_id: 1, user_id: 1 }, { unique: true });
db.bookmarks.createIndex({ movie_id: 1, user_id: 1 }, { unique: true });
