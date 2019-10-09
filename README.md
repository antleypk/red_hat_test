# red_hat_test  
A demonstration of python3 and database skills.   

This repo is my solution for a test to showcase programming ability.  

To easy install this application on a fresh rhel server run: "install_wizard.sh"  

Otherwise, clone the repo to the machine and run "install.sh"  

Operational Instructions:  
--To run a python file: "python3 file_name.py"  
-  -The output will print to console  
-  -None of the .py file take input to function  
-  -Run the python file from the dir that it lives in; relative file paths are present    
    
--The unit tests can be run at all TIMES by running "python3 master_ut.py".    
-  -Individual unit tests can be run via "python3 file_ut.py"   
-  -The output will print to console  

--File Index:  

--"install_wizard.sh" 
-  -Installs git  
-  -Clones the repo with the source code  
-  -Runs the install script to install and run the application


--"install.sh" 
-  -Installs all dev tools  
-  -python3 and its packages  
-  -mariadb, the database, its tables, and creates service user  
-  -loads the data into the respective tables  


--"movie_metadata.sql"
-  -Contains the database setup functions  


--"svc_user.sql"
-  -Creates a service user too allow remote connection  


--"data_loader.py"
-  -Loads the csv into an instance of mariadb  


--"top_ten_actors.py"
-  -Extracts data on all of the movies  
-  -Transforms the data into an actor table  
-  -Loads the data into an actor table  
-  -Prints off the top ten actors  


--"top_ten_genres.py" 
-  -Returns the top ten most profitable genres of movies  
--"top_ten_directors.py"
-  -Returns the top 10 most profitable directors  


--"top_ten_imdb_pairs.py"
-  -Returns the top ten Director, Actor according to IMDB  


--"top_ten_teams_with_multiple_films" 
-  -Returns the top ten teams of Actor/Director that had more than movie togteher  


--"config.py" 
-  -Has configureation settings for the application  


--"movie_metadata.csv" 
-  -Source data for the db  


--"test_movie_metadata.csv" 
-  -A subset of data stored for unit testing  


--"unit_test_util.py" 
-  -Has shared functions used by multiple test scripts  


--"master_ut.py" 
-  -Orchestrates the running of all tests together  


--"db_ut.py" 
-  -Tests that DB is properly installed with all resources  


--"data_loader_ut.py" 
- -Unit tests data_loader.py  


--"top_ten_directors_ut.py" 
-  -Unit tests top_ten_directors.py  


--"top_ten_actors_ur.py" 
-  -Unit tests top_ten_actors.py  


--"top_ten_genres_ut.py" 
-  -Unit tests top_ten_genres.py  


--"top_ten_imdb_pairs_ut.py" 
-  -Unit tests top_ten_imdb_pairs.py 


--"top_ten_teams_with_multiple_films_ut" 
-  -Unit tests top_ten_teams_with_multiple_films.py  


--"start_log" 
-  -Contains logs from running install_wizard.sh, the logs are output from install.sh  


--"conn.sh" 
-  -Connects to the database via root connection through mysql terminal  
  
--Developer Note:  
1. If I would have had more time I would have:  
2. Added more comments  
3. Added doc strings  
4. Deployed the solution via Docker  
5. Added more unit tests  
          
--Assumptions:  
-  -This project was developed on an amazon ec2; with Red Hat Enterprise Linux release 8.0 Ootpa.  

-  -This project has some development tools on it. Example tmux and nano.. They are   
    on here for development purposes but might not be included if deployment speed  
    was an important factor. Lean is fast.  
    

  
