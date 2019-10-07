CREATE TABLE IF NOT EXISTS movie_metadata(color VARCHAR(16)
						, director_name VARCHAR(32)
						, num_critic_for_reviews INT(3)
						, duration INT(3)
						, director_facebook_likes INT(5)
						, actor_3_facebook_likes INT(5)
						, actor_2_name VARCHAR(28)
						, actor_1_facebook_likes INT(6)
						, gross INT(9)
						, genres VARCHAR(64)
						, actor_1_name VARCHAR(27)
						, movie_title VARCHAR(87)
						, num_voted_users INT(7)
						, cast_total_facebook_likes INT(6)
						, actor_3_name VARCHAR(29)
						, facenumber_in_poster INT(2)
						, plot_keywords VARCHAR(149)
						, movie_imdb_link VARCHAR(52)
						, num_user_for_reviews INT(4)
						, movie_language VARCHAR(10)
						, country VARCHAR(20)
						, content_rating VARCHAR(9)
						, budget BIGINT(14)
						, title_year INT(4)
						, actor_2_facebook_likes INT(6)
						, imdb_score DECIMAL(4,2)
						, aspect_ratio DECIMAL(4,2)
						, movie_facebook_likes INT(6));

CREATE VIEW IF NOT EXISTS director AS 
( 
         SELECT   director_name, 
                  gross, 
                  budget, 
                  gross-budget AS profit 
         FROM     movie_metadata 
         WHERE    gross IS NOT NULL 
         AND      budget IS NOT NULL 
         ORDER BY director_name 
);