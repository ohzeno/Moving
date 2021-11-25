import requests
import pprint
import pandas as pd
import argparse
import os
import time
import logging.config


with open('tmdbapi.txt') as f:
    lines = f.readlines()
    api_key = lines[0].strip()


def get_youtube_link(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={api_key}'
    response = requests.get(url).json()
    # plogger.info.plogger.info(response)
    results = response['results']
    if len(results):
        for re in results:
            if re['site'] == 'YouTube':
                aa = re['key']
                youtube_link = f'https://www.youtube.com/watch?v={aa}'
                return youtube_link
        else:
            return 0
    else:
        return 0


def get_detail(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url).json()
    if response:
        try:
            # logger.info(response['title'])
            # plogger.info.plogger.info(response)
            genres = response['genres']
            gen = [genres[i]['name'] for i in range(len(genres))]
            d_li = [
                'genres', 'backdrop_path', 'id', 'overview', 'poster_path',
                'release_date', 'runtime', 'title', 'vote_average',
            ]
            df = pd.DataFrame([(0 for _ in range(9))], columns=d_li)
            for d in d_li:
                if d != 'genres':
                    df[d][0] = response[d]
                    # df.at[0, d] = response[d]
                    if d == 'release_date':
                        if int(df['release_date'][0][0:4]) < 1990:
                            return 0
                    if df.loc[0][d] == 0:
                        return 0
                else:
                    df[d][0] = gen
                    # df.at[df.index[0], d] = gen
                    if df.loc[0][d] == 0:
                        return 0

            df = df.set_index(df['id'])
            df = df.drop(['id'], axis=1)
            return df
        except Exception as err:
            logger.info(f'{movie_id}_에러: {err}')
            logger.info(response)
            return 0
    else:
        logger.info('response가 없습니다.')
        return 0


def get_credit(movie_id):
    """
    return[0]: 배우목록
    return[1]: 감독목록
    """
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}'
    response = requests.get(url).json()
    cast_li = response['cast']
    crew_li = response['crew']
    if len(cast_li) == 0 or len(crew_li) == 0:
        return 0
    actor_li = []
    director_li = []
    for ca in cast_li:
        if ca['known_for_department'] == 'Acting':
            if len(actor_li) == 10:
                break
            actor_li.append(ca['name'])
    for cr in crew_li:
        if cr['job'] == 'Director':
            director_li.append(cr['name'])
    # pprint.info.pprint.info(response2)
    # logger.info(actor_li)
    # logger.info(director_li)
    return [actor_li, director_li]


if __name__ == "__main__":
    os.environ["NUMEXPR_MAX_THREADS"] = "24"

    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=10000)
    args = parser.parse_args()

    str_log_file_name = f"log/get_movies_tmdb{args.start}.log"
    logging.config.fileConfig("logging.conf", disable_existing_loggers=False,
                              defaults={"str_log_file_name": str_log_file_name})
    logger = logging.getLogger("log03")

    dfs = []
    i = 1
    for num in range(args.start, args.start+30000):
        if os.path.exists(f'data/movies_{args.start:>6}_{i:>2}.csv'):
            logger.info(f'movies_{args.start:>6}_{i:>2}.csv 는 이미 존재한다.')
        else:
            df_1 = get_detail(num)
            if type(df_1) != int:
                logger.info(f'{num}_detail 성공')
                y_link = get_youtube_link(num)
                if y_link != 0:
                    df_1['youtube_link'] = y_link
                    logger.info(f'{num}_youtube 성공')
                    credit = get_credit(num)
                    if credit == 0:
                        logger.info(f'{num}_credit 실패')
                        continue
                    df_1['actors'] = 0
                    df_1['director'] = 0
                    # a = credit[0]
                    # logger.info(df_1['actors'])
                    # logger.info(df_1['actors'][df_1.index[0]])
                    # logger.info(df_1['actors'][0])
                    try:
                        df_1['actors'][df_1.index[0]] = credit[0]
                        df_1['director'][df_1.index[0]] = credit[1]
                    except Exception as err:
                        logger.info(err)
                        continue
                    dfs.append(df_1)
                    logger.info(f'{num}_credit 성공')
                    if len(dfs) == 500:
                        logger.info(len(dfs))
                        df_fin = pd.concat(dfs)
                        df_fin = df_fin.sort_index()
                        df_fin.to_csv(f'data/movies_{args.start:>6}_{i:>2}.csv')
                        dfs = []
                        i += 1
                        continue
                else:
                    logger.info(f'{num}_youtube 실패')
                    pass
            else:
                logger.info(f'{num}_detail 실패')
                continue

    if len(dfs):
        df_fin = pd.concat(dfs)
        df_fin = df_fin.sort_index()
        df_fin.to_csv(f'data/movies_{args.start:>6}_{i:>2}.csv')
