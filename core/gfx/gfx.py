import pygame

def draw(screen, x, y, w, h):
    """
    Simple drawing function that simplifies pygame's.

    Args:
        screen  (pygame.Surface): The initial value
        x       (int)           : The x position
        y       (int)           : The y position
        w       (int)           : The width
        h       (int)           : The height

    Returns:
        None: Draws a pygame Rect
    """
    pygame.draw.rect(screen, pygame.Color(255,0,255), pygame.Rect(x,y,w,h))


def drawRect(screen, rect):
    """
    Draw a Rect

    Args:
        screen  (pygame.Surface): The screen to draw to
        rect    (pygame.Rect)   : The Rect to draw

    Returns:
        None: Draws a pygame Rect
    """
    pygame.draw.rect(screen, pygame.Color(255,0,255), rect)


def drawBlock(screen, block):
    """
    Draw a block

    Args:
        screen  (pygame.Surface): The screen to draw to
        block   (core.block)    : The Block to draw

    Returns:
        None: Draws a Block
    """
    pygame.draw.rect(screen,
                     pygame.Color(block.r, block.g,block.b),
                     pygame.Rect(block.x, block.y, block.width, block.height)
                     )


def drawGrid(screen, grid):
    """
    Draw a grid

    Args:
        screen  (pygame.Surface): The screen to draw to
        grid   (core.block)     : The grid to draw

    Returns:
        None: Draws a grid
    """
    for row in grid:
        for block in row:
            pygame.draw.rect(screen,
                             pygame.Color(block.r, block.g,block.b),
                             pygame.Rect(block.x, block.y, block.width, block.height)
                             )

def drawSprite(screen, sprite):
    """
    Draw a sprite

    Args:
        screen  (pygame.Surface): The screen to draw to
        sprite  (core.gfx)      : The sprite to draw

    Returns:
        None: Draws a sprite to the screen
    """
    screen.blit(sprite.image, (sprite.x, sprite.y))


