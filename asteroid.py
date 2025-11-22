import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Always kill original asteroid
        self.kill()

        # If too small to split, stop here
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Log the split event
        log_event("asteroid_split")

        # Generate split angle between 20° and 50°
        angle = random.uniform(20, 50)

        # Create two new vectors pointing outward
        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-angle)

        # New radius reduced by ASTEROID_MIN_RADIUS
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Spawn two new asteroids
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Make them move slightly faster (1.2x)
        a1.velocity = velocity1 * 1.2
        a2.velocity = velocity2 * 1.2
