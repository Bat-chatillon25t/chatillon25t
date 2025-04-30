__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


class GlobSearchError(Exception):
    """Raised if the glob search results in an error."""
class UnsuccessfulHttpRequestError(Exception):
    """Raised if an http access results returns a response with status code which does not indicate success (>=300)."""