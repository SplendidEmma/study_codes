# Add a movie to the watchlist (Title,genre,year)
# Mark a movie as watched
# Show all movies
# Show unique genres
# Show a summary
# Quit

watchlist = []
watched = []
genres = set()
while True:
    print("Enter option")
    print("1. Add a movie to the watchlist")
    print("2. Mark a movie as watched")
    print("3. Show all movies")
    print("4. Show unique genres")
    print("5. Show a summary")
    print("6. quit")

    choice = input("Choose: ").strip()

    if choice == "1":
        title = input("Title: ").strip()
        genre = input("Genre: ").strip()
        year = int(input("Year: ").strip())

        if year < 1888 or year > 2026:
            print("Enter year btw 1888 - 2026")
        else:
            movie = (title,genre,year) # tuple: once saved, it becomes immutable
            watchlist.append(movie)
            genres.add(genre)
            print("Movie Added!")
    
    # Mark movies as watched
    elif choice == "2":
        #Don't go if there's no movie yet
        if len(watchlist) == 0:
            print("No movies yet")
        else:
            #Input title you want to mark
            title = input("Enter title to mark: ").strip()
            #Create an empty variable to hold the movie when found
            found = None
            #Use the for loop to go through the watchlist
            for movie in watchlist:
                #check if the title matches
                if movie[0] == title: #movie - (title (0),genre(1),year(2))
                    #If title matches - update the found variable and break the loop.
                    found = movie
                    break
            #Update the lists (Both watched and watchlist)
            if found:
                watched.append(found)
                watchlist.remove(found)
                print("Movie marked as watched")   
            else:
                #If not found - print this
                print("Movie not found")
    
    elif choice == "3":
        if len(watched)== 0 and len(watchlist) == 0:
            print("No movies yet")
        else:
            #lets find a way to print the full movie list.
            #For watched.
            if len(watched) == 0:
                print("No watched movies yet")
            else:
                print(f"Watched Movies: {watched}")
            #For watchlist
            if len(watchlist) == 0:
                print("No movie added yet!")
            else:
                print(f"Watchlist: {watchlist} ")
    
    elif choice == "4":
        if len(genres) == 0:
            print("No genres yet")
        else:
            print(f"All genres: {genres}")
    
    elif choice == "5":
        #Show summary
        #Total movies
        print(f"Total Movies: {len(watched) + len(watchlist)}")
        #Total Watched
        print(f"No. of watched: {len(watched)}")
        #Total Watchlist
        print(f"No. of watchlist: {len(watchlist)}")
        #Total Genres
        print(f"No. of genres: {len(genres)}")

    elif choice == "6":
        print("Good bye!")
        break