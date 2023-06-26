conn = new Mongo();
db = conn.getDB("ugc");

db.createCollection("likes");

db.likes.createIndex({ film_id: 1, user_id: 1 }, { unique: true });
