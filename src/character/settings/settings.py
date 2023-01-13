LIST_CLASSES = [["duelist", "mage", "assassin"], ["warrior", "mage", "warden"]]


def read(name, file):
    with open(
        f"static/context_info/{name}/{file}.txt", mode="r+", encoding="utf-8"
    ) as file:
        return "\r".join(file.readlines())


INFO_HERALDRY = {
    "dark-elf": read("dark", "heraldry"),
    "forest-elf": read("forest", "heraldry"),
    "grey-elf": read("grey", "heraldry"),
}

INFO_SKILLS = {
    "dark-elf-duelist": read("dark", "duelist"),
    "dark-elf-mage": read("dark", "mage"),
    "dark-elf-assassin": read("dark", "assassin"),
    "forest-elf-warrior": read("forest", "warrior"),
    "forest-elf-mage": read("forest", "mage"),
    "forest-elf-warden": read("forest", "warden"),
    "grey-elf-warrior": read("grey", "warrior"),
    "grey-elf-mage": read("grey", "mage"),
    "grey-elf-warden": read("grey", "warden"),
}
