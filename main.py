from serie import Serie
from videogame import Videogame


# Create the videogames array
def videogames_array():
    game1 = Videogame("The Legend of Zelda: Breath of the Wild", 40, 'Adventure', 'Nintendo')
    game2 = Videogame("Dishonored", 20, 'Action-Adventure', 'Bethesda')
    game3 = Videogame("The Binding of Isaac", 100, "Roguelike", "Nicalis")
    game4 = Videogame("Pokemon: Red", 30, 'RPG', 'Nintendo')
    game5 = Videogame("Resident Evil", 30, 'Horror', 'Capcom')

    return [game1, game2, game3, game4, game5]


def series_array():
    serie1 = Serie('The Boys', 2, 'Superheroes', 'PrimeVideo')
    serie2 = Serie('Mandalorian', 1, 'Fantasy', 'Disney+')
    serie3 = Serie('Dark', 3, 'Mistery', 'Netflix')
    serie4 = Serie('The Fresh Prince of Bel-Air', 6, 'Comedy', 'NBC')
    serie5 = Serie('Friends', 10, 'Comedy', 'NBC')

    return [serie1, serie2, serie3, serie4, serie5]


def deliver(obj):
    obj[1].deliver()
    obj[3].deliver()
    obj[5].deliver()
    obj[7].deliver()
    obj[9].deliver()


def check_delivered(videogames, series):
    delivered_videogames = list(filter(Videogame.is_delivered, videogames))
    delivered_series = list(filter(Serie.is_delivered, series))

    print(f"Delivered videogames: {len(delivered_videogames)}")
    print(f"Delivered series: {len(delivered_series)}")

    for game in delivered_videogames:
        game.take_back()
    for series in delivered_series:
        series.take_back()


def check_longer(array):
    longer = ""
    for count, value in enumerate(array):
        if count == 0:
            longer = value
        if value.compare_to(longer):
            longer = value
    return longer


def show_longer(videogames, series):
    longer_game = check_longer(videogames)
    longer_serie = check_longer(series)

    print(f"Longer videogame: {longer_game.__str__()}")
    print(f"Longer serie: {longer_serie.__str__()}")


def run():
    videogames = videogames_array()
    series = series_array()
    deliver(videogames + series)
    check_delivered(videogames, series)
    show_longer(videogames, series)


if __name__ == '__main__':
    run()
