from . import models
from . import wizards
<<<<<<< HEAD
from . import hooks

def post_load_hook(cr, registry):
    from .hooks import update_detailed_type_after_load
    update_detailed_type_after_load(cr, registry)
=======
# from . import hooks

# def post_load_hook(cr, registry):
#     from .hooks import update_detailed_type_after_load
#     update_detailed_type_after_load(cr, registry)
>>>>>>> 4491c27 (Initial import (neteja menús, event_views off, hooks fora))
