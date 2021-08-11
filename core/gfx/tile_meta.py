class TileMeta(object):
    """
    TileMeta objects hold all of the information than an AnimatedSprite needs to
    run all of the different animations.
    """
    def __init__(self):
        self.meta = {
            'idle' : {
                'start_frame' : 1,
                'max_frames' : 6,
            },
            'running' : {
                'start_frame' : 2,
                'max_frames' : 6,
            },
        }

    def has(self, meta_name):
        """
        Check if a specific meta name is available.

        Args:
            meta_name (str): The name of the meta to find.

        Returns:
            Bool
        """
        if meta_name in self.meta:
            return True
        else:
            return False

    def add(self, new_meta):
        """
        Add a new, non default meta to the TileMeta object.

        Args:
            meta_name (Dict): A dictionary of new tile meta.

        Returns:
            None
        """
        self.meta_name = new_meta
