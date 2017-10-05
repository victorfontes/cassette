# This rather useless module is needed to prevent cyclical imports


import contextlib


@contextlib.contextmanager
def unpatched_httplib_context(cassette_library):
    """Create a context in which httplib is unpatched."""

    from cassette.patcher import patch, unpatch

    unpatch()
    yield
    patch(cassette_library)
