from mrjob.job import MRJob
from mrjob.step import MRStep


class MostPopularMovie(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings)
            , MRStep(reducer=self.reducer_most_ratings)
        ]

    def mapper_get_ratings(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield movieID, 1

    def reducer_count_ratings(self, key, values):
        yield 1, (sum(values), key)

    def reducer_most_ratings(self, key, values):
        yield max(values)


if __name__ == '__main__':
    MostPopularMovie.run()
