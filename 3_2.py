def month_to_season(month):
    season_ranges = {
        (12, 1, 2): 'Winter',
        (3, 4, 5): 'Spring',
        (6, 7, 8): 'Summer',
        (9, 10, 11): 'Autumn'
    }

    season = None

    for key, value in season_ranges.items():
        if month in key:
            season = value
            break

    return season

print(month_to_season(1))
print(month_to_season(5))
print(month_to_season(8))
print(month_to_season(9))
print(month_to_season(12))
print(month_to_season(999))