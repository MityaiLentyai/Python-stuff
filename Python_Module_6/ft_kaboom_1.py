import alchemy.grimoire.dark_spellbook

print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION: ")

print(
    f"{alchemy.grimoire.dark_spellbook.dark_spell_record('Fantasy', 'Earth')}")
