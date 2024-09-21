#Course: CIS 103
#Instructor: Md Ali
#Student: Sahar Iqbal
#Date: 09/20/2024

# Part: 03 Real-World Scenario: Movie Database

# Create a dictionary with movie titles and directors names:
Movies = {'Inception': 'Christopher Nolan', 'Pulp Fiction': 'Quentin Tarantino', 'The Godfather':
'Francis Ford Coppola', 'The Dark Knight': 'Christopher Nolan'}
  
# Add two new movies:'Interstellar' by 'Christopher Nolan' and 'Kill Bill' by 'Quentin Tarantino'
Movies['Interstellar'] = 'Christopher Nolan'
Movies['Kill Bill'] = 'Quentin Tarantino'

# Update the director of 'The Godfather' directed by 'Sofia Coppola' in the dictionary 
Movies['The Godfather'] = 'Sofia Coppola'

# Print the entire updated movie database
print("Updated Movie Database:")
for title, director in Movies.items():
    print(f"{title}: {director}")

# Challenge: Print all movies directed by 'Christopher Nolan'
print("\nMovies directed by Christopher Nolan:")
for title, director in Movies.items():
    if director == 'Christopher Nolan':
        print(title)











