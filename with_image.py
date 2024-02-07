import pygame
import time

class WordGuessingGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Word Guessing Game")
        self.clock = pygame.time.Clock()

        # Define colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 128, 0)
        self.ORANGE = (255, 165, 0)
        self.RED = (255, 0, 0)

        # Size of the screen
        self.SIZE = [1000, 800]
        self.screen = pygame.display.set_mode(self.SIZE)

        # Load images and sounds
        self.load_resources()

        # Initialize game variables
        self.word_guess = "salut"
        self.guessed_characters = []
        self.guessed_characters_position = []
        self.guessed_characters_not_position = []
        self.guessed_characters_not_in_word = []
        self.input_character = ""
        self.word = ""
        self.message_text = ""
        self.message_color = ""
        self.x_text = 810
        self.y_text = 90
        self.input_active = False

        self.font = pygame.font.Font("arabic.ttf", 30)
        self.font_error = pygame.font.Font("arabic.ttf", 15)

    def load_resources(self):
        self.background_image = pygame.image.load("general image.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, (1000, 800))

        # self.sound = pygame.mixer.Sound("gamesound.mp3")

    def blit_character(self, word):
        x_positions = [810, 708, 606, 504, 402, 300]
        y_position = 90

        for x in x_positions:
            text_surface = self.font.render(word, True, self.WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y_position)
            self.screen.blit(text_surface, text_rect)

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.process_entered_text()
                elif event.key == pygame.K_BACKSPACE:
                    self.remove_last_character()
                else:
                    self.process_input_character(event.unicode)

        return False

    def process_entered_text(self):
        print("Entered text:", self.word)
        if len(self.word) != 5:
            self.show_error_message("Word must have exactly 5 letters")
            return

        for i, character in enumerate(self.word):
            if character == self.word_guess[i]:
                self.guessed_characters_position.append(character)
                self.guessed_characters.append(character)
            elif character in self.word_guess:
                self.guessed_characters_not_position.append(character)
                self.guessed_characters.append(character)

        print("Correctly Guessed Characters (Position):", self.guessed_characters_position)
        print("Correctly Guessed Characters (Not Position):", self.guessed_characters_not_position)

        for character in self.word:
            if character not in self.guessed_characters:
                self.guessed_characters.append(character)

        print("Guessed Characters:", self.guessed_characters)

        self.y_text += 80
        self.x_text = 810
        self.word = ""

    def remove_last_character(self):
        if len(self.word) > 0:
            self.word = self.word[:-1]
            self.x_text += 102
            print(self.word)

    def process_input_character(self, input_character):
        self.word += input_character
        if len(self.word) < 5:
            self.input_character = input_character
            self.x_text -= 102

    def show_error_message(self, message):
        self.message_text = message
        self.message_color = self.RED
        message_surface = self.font_error.render(self.message_text, True, self.RED)
        message_pos = (510, 290)
        self.x_text = 810
        self.y_text = 90
        self.screen.blit(message_surface, message_pos)
        pygame.display.flip()
        time.sleep(1)
        print(self.message_text)
        self.screen.blit(self.background_image, [0, 0])
        pygame.display.flip()

    def draw_text_input(self):
        if set(self.guessed_characters_position) >= set(self.word_guess):
            text_surface = self.font.render(self.input_character[::-1], True, self.GREEN)  # Reverse the text for right-to-left rendering
        elif self.input_character in self.word_guess and self.input_character not in self.guessed_characters_position:
            text_surface = self.font.render(self.input_character[::-1], True, self.ORANGE)  # Reverse the text for right-to-left rendering
        else:
            text_surface = self.font.render(self.input_character[::-1], True, self.WHITE)  # Reverse the text for right-to-left rendering

        text_width = text_surface.get_width()  # Get the width of the rendered text
        text_pos = (self.x_text - text_width, self.y_text)  # Calculate the adjusted rendering position
        self.screen.blit(text_surface, text_pos)

        cursor_surface = self.font.render("|", True, self.WHITE)
        cursor_pos = (text_pos[0] + text_width, text_pos[1])  # Calculate the adjusted cursor position
        self.screen.blit(cursor_surface, cursor_pos)

    def run(self):
        self.sound.play()

        done = False

        while not done:
            self.screen.blit(self.background_image, [0, 0])

            done = self.handle_events()

            self.draw_text_input()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

game = WordGuessingGame()
game.run()



