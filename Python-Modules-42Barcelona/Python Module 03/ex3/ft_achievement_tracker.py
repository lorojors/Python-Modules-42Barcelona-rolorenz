def main():
    print("=== Achievement Tracker System ===")
    
    # Sample achievement sets for different players
    player_alice = set(["first_kill", "level_10", "treasure_hunter", "speed_demon"])
    player_bob = set(["first_kill", "level_10", "boss_slayer", "collector"])
    player_charlie = set(["level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"])
    
    players = {
        "alice": player_alice,
        "bob": player_bob,
        "charlie": player_charlie
    }
    
    # Display player achievements
    for name, achievements in players.items():
        print(f"Player {name} achievements: {achievements}")
    
    print("=== Achievement Analytics ===")
    
    # Union: All unique achievements across all players
    all_achievements = player_alice.union(player_bob, player_charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")
    
    # Intersection: Achievements that all players have
    common_all = player_alice.intersection(player_bob, player_charlie)
    print(f"Common to all players: {common_all}")
    
    # Find rare achievements (only one player has them)
    alice_unique = player_alice.difference(player_bob, player_charlie)
    bob_unique = player_bob.difference(player_alice, player_charlie)
    charlie_unique = player_charlie.difference(player_alice, player_bob)
    rare_achievements = alice_unique.union(bob_unique, charlie_unique)
    
    if rare_achievements:
        print(f"Rare achievements (1 player): {rare_achievements}")
    
    # Pairwise intersections
    alice_bob = player_alice.intersection(player_bob)
    if alice_bob:
        print(f"Alice vs Bob common: {alice_bob}")
    
    # Individual unique achievements
    if alice_unique:
        print(f"Alice unique: {alice_unique}")
    if bob_unique:
        print(f"Bob unique: {bob_unique}")
    if charlie_unique:
        print(f"Charlie unique: {charlie_unique}")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()