import math
import sys
import pygame

class LSystem():
    def __init__(self, axiom, rules, dtheta, start_pos, start_rot, length, ratio, visualise):
        self.axiom = axiom
        self.rules = rules
        self.start_rot = start_rot
        self.theta = math.radians(self.start_rot)
        self.dtheta = dtheta
        self.start_pos = start_pos
        self.x, self.y = start_pos
        self.length = length
        self.ratio = ratio
        self.positions = []
        self.visualise = visualise

    def __str__(self):
        return self.axiom

    def generate(self):
        if self.axiom == '' or self.rules == '':
            return ''
        self.x, self.y = self.start_pos
        self.theta = math.radians(self.start_rot)
        self.length *= self.ratio
        newStr = ""
        for char in self.axiom:
            if char in self.rules:
                newStr += self.rules[char]
            else:
                newStr += char
        
        self.axiom = newStr

    def draw(self, screen):
        try:
            color = 0
            dcolor = 255 / len(self.axiom)
            for char in self.axiom:
                if char == "F" or char == "G":
                    x2 = self.x - self.length * math.cos(self.theta)
                    y2 = self.y - self.length * math.sin(self.theta)
                    pygame.draw.line(screen, (255 - color, color, 125 + dcolor / 2), (self.x, self.y), (x2, y2))
                    self.x, self.y = x2, y2
                elif char == "+":
                    self.theta += self.dtheta
                elif char == "-":
                    self.theta -= self.dtheta
                elif char == "[":
                    self.positions.append({"x": self.x, "y": self.y, "theta": self.theta})
                elif char == "]":
                    pos = self.positions.pop()
                    self.x, self.y, self.theta = pos["x"], pos["y"], pos["theta"]
                color += dcolor
                
                if self.visualise == 1:
                    pygame.display.flip()
        except Exception as e:
            print(e)
            print("Error in draw method")


def main():
    l_sys_text = sys.argv[1]
    print(l_sys_text)
    pygame.init()
    size = (int(sys.argv[2]), int(sys.argv[3]))
    start_pos = (int(sys.argv[4]), int(sys.argv[5]))
    start_rot = (float(sys.argv[6]))
    length = int(sys.argv[7])
    ratio = float(sys.argv[8])
    visualise = int(sys.argv[9])
    screen = pygame.display.set_mode(size)

    with open(l_sys_text, "r") as f:
        axiom = f.readline().strip()
        numRules = int(f.readline().strip())
        rules = {}
        for i in range(numRules):
            rule = f.readline().strip().split(" ")
            rules[rule[0]] = rule[1]
        
        dtheta = math.radians(int(f.readline().strip()))
        system = LSystem(axiom, rules, dtheta, start_pos, start_rot, length, ratio, visualise)

    running = True
    clock = pygame.time.Clock()
    iterations = 0
    font = pygame.font.SysFont("Arial", 24)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        if iterations < int(sys.argv[10]):
            screen.fill((0, 0, 0))

            # Draw current iteration to top left of screen
            text = font.render("Iteration: " + str(iterations+1) + "/" + sys.argv[10], True, (255, 255, 255))
            screen.blit(text, (20, 0))

            # Draw current rules to the top right of the screen
            text = font.render("Rules:", True, (255, 255, 255))
            screen.blit(text, (size[0] - text.get_width() - 20, 0))
            for i, rule in enumerate(system.rules):
                text = font.render(rule + " -> " + system.rules[rule], True, (255, 255, 255))
                screen.blit(text, (size[0] - text.get_width() - 20, (i+1) * text.get_height()))

            # Draw current dtheta to the bottom right of the screen
            text = font.render("dtheta: " + str(round(math.degrees(system.dtheta))), True, (255, 255, 255))
            screen.blit(text, (size[0] - text.get_width() - 20, size[1] - text.get_height()))

            # Draw rules key to the top left of the screen
            text = font.render("Key:", True, (255, 255, 255))
            screen.blit(text, (20, text.get_height()))
            text = font.render("F or G -> Draw line forward", True, (255, 255, 255))
            screen.blit(text, (20, text.get_height() * 2))
            text = font.render("+ -> Rotate clockwise", True, (255, 255, 255))
            screen.blit(text, (20, text.get_height() * 3))
            text = font.render("- -> Rotate anti-clockwise", True, (255, 255, 255))
            screen.blit(text, (20, text.get_height() * 4))
            text = font.render("[ -> Save current position and rotation", True, (255, 255, 255))
            screen.blit(text, (20, text.get_height() * 5))
            text = font.render("] -> Restore saved position and rotation", True, (255, 255, 255))
            screen.blit(text, (20, text.get_height() * 6))

            system.draw(screen)
            system.generate()
            iterations += 1
            scaled_screen = pygame.Surface((size[0]*15, size[1]*15))
            scaled_screen = scaled_screen.convert()
            scaled_screen.blit(screen, (0,0))
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
