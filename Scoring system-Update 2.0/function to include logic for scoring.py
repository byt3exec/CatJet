def check_score(pipes, score, can_score):
    if pipes:
        for pipe in pipes:
            if 95 < pipe.centerx < 105 and can_score:
                score += 1
                can_score = False
            if pipe.centerx < 0:
                can_score = True
    return can_score

def display_score(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (screen_width / 2, 100))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        pass
