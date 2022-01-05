use foodmart;
create view if not exists avgRatingView AS
select movie_id, count(*) counts, sum(rating) ratings, sum(rating)/count(movie_id) avgRatings from movie_ratings
group by movie_id
order by avgRatings desc;

select m.movie_title,r.avgratings,r.counts from avgRatingView r
join movie_details m on r.movie_id = m.movie_id
where r.ratings>100;
