import pygame

def draw(screen, x, y, w, h):
    """Wrapper for pygame drawing"""
    pygame.draw.rect(screen, pygame.Color(255,0,255), pygame.Rect(x,y,w,h))

def drawRect(screen, rect):
    """Draw a pygame.Rect abstraction"""
    pygame.draw.rect(screen, pygame.Color(255,0,255), rect)
