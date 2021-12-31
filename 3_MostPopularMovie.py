from mrjob.job import MRJob
from mrjob.step import MRStep

class MostPopularMovie(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings)
            ,
            MRStep(reducer = self.reducer_find_max)
        ]

    def mapper_get_ratings(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield movieID, 1

    def reducer_count_ratings(self, key, values):
        # set the key as identical so we can aggregate late
        # max(key, sum(values)) wont get the most rate movie, but the one with biggest movie id
        yield None, (sum(values), key)

    def reducer_find_max(self, key, values):
        yield max(values)

if __name__ == '__main__':
    MostPopularMovie.run()
