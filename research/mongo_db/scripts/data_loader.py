import pickle
import random

from db_manager import MongoDBManager
from generate_data import DBDataGenerator
from pymongo.database import Collection
from pymongo.errors import CollectionInvalid
from tqdm import tqdm

from settings import DBCollections, research_settings


def get_ids(filename: str, count: int):
    dg = DBDataGenerator()
    ids = []

    try:
        with open(filename, 'rb') as file:
            ids = pickle.load(file)

    except FileNotFoundError:
        ids = dg.gen_ids(count)
        with open(filename, 'wb') as file:
            pickle.dump(ids, file)

    finally:
        return ids


user_ids = get_ids(research_settings.user_id_fn, research_settings.n_users)
movie_ids = get_ids(research_settings.movie_id_fn, research_settings.n_movies)


def get_random_movie_ids(movie_list: list, movie_count):
    start_index = random.randint(0, research_settings.n_movies - movie_count - 1)
    for i in range(start_index, start_index + movie_count):
        yield movie_list[i]


def generate_likes(collection: Collection, u_ids: list, f_ids: list):
    dg = DBDataGenerator()

    for user_id in tqdm(u_ids):
        user_movie_count = random.randint(
            research_settings.n_likes_min, research_settings.n_likes_max
        )
        if user_movie_count:
            collection.insert_many(
                [
                    dg.generate_like_doc(user_id=user_id, movie_id=movie_id)
                    for movie_id in get_random_movie_ids(
                        movie_list=f_ids, movie_count=user_movie_count
                    )
                ]
            )


def main():
    mongodb_manager = MongoDBManager(
        research_settings.db_url, research_settings.db_name
    )

    try:
        like_collection = mongodb_manager.create_collection(
            DBCollections.LIKES
        )
    except CollectionInvalid:
        like_collection = mongodb_manager.db.get_collection(
            DBCollections.LIKES
        )

    generate_likes(like_collection, user_ids, movie_ids)

    like_collection.create_index([('movie_id', 1)])
    like_collection.create_index([('user_id', 1)])


if __name__ == '__main__':
    main()
