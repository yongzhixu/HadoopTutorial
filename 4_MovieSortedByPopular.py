from mrjob.job import MRJob
from mrjob.step import MRStep


class MostPopularMovie(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings)
            ,
            MRStep(reducer=self.reducer_movie_sort)
        ]

    def mapper_get_ratings(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        # key set here will server as a elbow point for the reducer later involved
        yield movieID, 1

    def reducer_count_ratings(self, key, values):
        # set the key as identical so we can aggregate late
        # max(key, sum(values)) wont get the most rate movie, but the one with biggest movie id
        yield str(sum(values)).zfill(6), key

    def reducer_movie_sort(self, counts, movies):
        for movie in movies:
            yield movie, counts


if __name__ == '__main__':
    MostPopularMovie.run()
