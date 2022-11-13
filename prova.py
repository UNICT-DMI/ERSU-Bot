from module.data.user_settings import UserSettings

if __name__ == "__main__" :
    table = UserSettings()

    table.setup()
    table.insert_user(218012)
    table.insert_user(122131)
    table.setMeal(218012,"tuesday", "lunch")
    table.setMeal(218012,"tuesday", "dinner")